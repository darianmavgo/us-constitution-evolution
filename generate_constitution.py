import os
import subprocess
import json
import shutil
import datetime

REPO_NAME = "us-constitution-evolution"
CONTENT_DIR = "../content"  # Relative to repo dir after chdir

def run_git(args, date=None, env=None):
    """Runs a git command with optional date spoofing."""
    git_env = os.environ.copy()
    if env:
        git_env.update(env)
    
    if date:
        try:
             # Parse input date
            if "T" in date:
                event_dt = datetime.datetime.fromisoformat(date)
            else:
                event_dt = datetime.datetime.strptime(date, "%Y-%m-%d")
            
            # YEAR-TO-MINUTE SCALING
            # Request: "Creation the release of the us constitution 2026/1/1 00:00:00"
            # Anchor Historic: Sept 17, 1787 (Release/Signing)
            anchor_hist = datetime.datetime(1787, 9, 17)
            
            # Anchor Target: 2026-01-01 00:00:00 UTC
            anchor_target = datetime.datetime(2026, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
            
            # Calculate difference in years (float)
            delta_seconds_hist = (event_dt - anchor_hist).total_seconds()
            seconds_per_year_hist = 365.2425 * 24 * 3600
            
            diff_years = delta_seconds_hist / seconds_per_year_hist
            
            # Scale: 1 Year = 1 Minute (60 seconds)
            offset_seconds = diff_years * 60
            
            safe_dt = anchor_target + datetime.timedelta(seconds=offset_seconds)

            # Get timestamp (int)
            ts = int(safe_dt.timestamp())
            
            # Format: <timestamp> <offset>
            full_date = f"{ts} +0000"
            
            git_env["GIT_AUTHOR_DATE"] = full_date
            git_env["GIT_COMMITTER_DATE"] = full_date
        except ValueError as e:
            print(f"Warning: Could not parse date {date}: {e}")
    
    subprocess.run(["git"] + args, check=True, env=git_env)

def main():
    # 1. Initialize Repo
    if os.path.exists(REPO_NAME):
        shutil.rmtree(REPO_NAME)
    os.makedirs(REPO_NAME)
    os.chdir(REPO_NAME)
    
    run_git(["init"])
    # Set default branch to main
    run_git(["symbolic-ref", "HEAD", "refs/heads/main"])

    print(f"Initialized repo in {REPO_NAME}")

    # 2. Commit Draft 1: Virginia Plan
    print("Committing Virginia Plan...")
    shutil.copy(os.path.join(CONTENT_DIR, "Draft_1_Virginia_Plan.md"), "US_Constitution.md")
    run_git(["add", "US_Constitution.md"])
    run_git(["commit", "-m", "Draft 1: Virginia Plan (1787)"], date="1787-05-29")

    # 3. Commit Draft 2: Committee of Detail
    print("Committing Committee of Detail Draft...")
    shutil.copy(os.path.join(CONTENT_DIR, "Draft_2_Committee_of_Detail.md"), "US_Constitution.md")
    run_git(["add", "US_Constitution.md"])
    run_git(["commit", "-m", "Draft 2: Committee of Detail Report (1787)"], date="1787-08-06")

    # 4. Final Constitution
    print("Committing Final Constitution...")
    shutil.copy(os.path.join(CONTENT_DIR, "US_Constitution_1787.md"), "US_Constitution.md")
    run_git(["add", "US_Constitution.md"])
    run_git(["commit", "-m", "Final US Constitution - Signed (1787)"], date="1787-09-17")
    
    # Tag v1.0
    # Anchor to 2026-01-01 00:00:00 exactly
    ts_1787 = int(datetime.datetime(2026, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc).timestamp())
    tag_env = {"GIT_TAGGER_DATE": f"{ts_1787} +0000"}
    run_git(["tag", "-a", "v1.0", "-m", "Release 1.0: Original Signed Constitution"], env=tag_env)

    # 5. Amendments
    print("Applying Amendments...")
    with open(os.path.join(CONTENT_DIR, "amendments_metadata.json"), "r") as f:
        amendments = json.load(f)
    
    for i, amd in enumerate(amendments):
        date = amd["date"]
        title = amd["title"]
        text = amd["text"]
        
        # Determine Safe Filename
        # Logic: Amendment I -> Amendment_I.md
        safe_name = title.replace(" ", "_").replace(":", "")
        filename = f"{safe_name}.md"
        
        # Write separate file
        with open(filename, "w") as f:
            f.write(f"# {title}\n\n{text}\n")
        
        run_git(["add", filename])
        run_git(["commit", "-m", f"Ratified: {title}"], date=date)
        
        # Create Release Tag
        safe_title = title.replace(" ", "")
        year = date.split("-")[0]
        tag_name = f"v{year}-{safe_title}"
        
        event_dt = datetime.datetime.strptime(date, "%Y-%m-%d")
        
        # Calculate offset
        anchor_hist = datetime.datetime(1787, 9, 17)
        anchor_target = datetime.datetime(2026, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
        
        delta_seconds_hist = (event_dt - anchor_hist).total_seconds()
        seconds_per_year_hist = 365.2425 * 24 * 3600
        diff_years = delta_seconds_hist / seconds_per_year_hist
        
        offset_seconds = diff_years * 60
        safe_dt = anchor_target + datetime.timedelta(seconds=offset_seconds)
        
        ts = int(safe_dt.timestamp())
        
        tag_env = {"GIT_TAGGER_DATE": f"{ts} +0000"}
        run_git(["tag", "-a", tag_name, "-m", f"Release: {title} ratified on {date}"], env=tag_env)
        print(f"  Applied {title} ({date}) -> {safe_dt} (File: {filename})")

    print(f"\nSuccess! Repo generated in {os.path.abspath(REPO_NAME)}")
    print("To push to GitHub, create a repo 'us-constitution-evolution' on GitHub and run:")
    print(f"  cd {REPO_NAME}")
    print("  git remote add origin https://github.com/darianmavgo/us-constitution-evolution.git")
    print("  git push -u origin main --tags")

if __name__ == "__main__":
    main()
