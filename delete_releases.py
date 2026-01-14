import subprocess
import json

def run_command(args):
    try:
        subprocess.run(args, check=True, cwd="us-constitution-evolution")
    except subprocess.CalledProcessError as e:
        print(f"Failed: {' '.join(args)} -> {e}")

def main():
    # List releases
    result = subprocess.run(["gh", "release", "list", "--json", "tagName"], cwd="us-constitution-evolution", capture_output=True, text=True)
    releases = json.loads(result.stdout)
    
    print(f"Deleting {len(releases)} releases...")
    for rel in releases:
        tag = rel['tagName']
        print(f"Deleting release {tag}...")
        run_command(["gh", "release", "delete", tag, "-y"])

    print("All releases deleted. You can now run create_releases.py")

if __name__ == "__main__":
    main()
