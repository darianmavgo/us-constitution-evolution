import subprocess
import os

def run_command(args):
    try:
        subprocess.run(args, check=True, cwd="us-constitution-evolution")
        print(f"Success: {' '.join(args)}")
    except subprocess.CalledProcessError as e:
        print(f"Failed: {' '.join(args)} -> {e}")

def main():
    # Get all tags sorted by date
    result = subprocess.run(["git", "tag", "--sort=creatordate"], cwd="us-constitution-evolution", capture_output=True, text=True)
    tags = result.stdout.strip().splitlines()

    print(f"Found {len(tags)} tags. Creating releases...")

    for tag in tags:
        # Determine title
        if tag == "v1.0":
            title = "1.0: First Public Release (1787)"
            notes = "The original signed US Constitution."
        else:
            # v1791-AmendmentI -> Amendment I (1791)
            parts = tag.split("-")
            year = parts[0][1:]
            name = parts[1]
            # Insert spaces before capital letters if needed, but simple is fine
            title = f"{name} ({year})"
            notes = f"Ratification of {name} in {year}."

        # gh release create <tag> --title <title> --notes <notes>
        cmd = ["gh", "release", "create", tag, "--title", title, "--notes", notes]
        run_command(cmd)

if __name__ == "__main__":
    main()
