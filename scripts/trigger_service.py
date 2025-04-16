import json
import time
import subprocess
from datetime import datetime

# File paths
SESSION_LOG_PATH = '/workspaces/codespace-tracker/tracker/.codespace-tracker/session_logs.json'
TOTAL_RUNTIME_PATH = '/workspaces/codespace-tracker/tracker/.codespace-tracker/total_runtime.json'

# Backup threshold time (in seconds)
BACKUP_THRESHOLD = 3600  # 1 hour = 3600 seconds

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def perform_backup():
    """Trigger the backup process."""
    print("Performing backup...")
    # Example backup command (replace this with your actual backup command)
    subprocess.run(["bash", "/workspaces/codespace-tracker/scripts/backup.sh"])

def check_runtime():
    """Check the total runtime and trigger backup if threshold is crossed."""
    # Load total runtime data
    total_runtime = load_json(TOTAL_RUNTIME_PATH)
    if 'total_runtime' not in total_runtime:
        total_runtime['total_runtime'] = 0
        with open(TOTAL_RUNTIME_PATH, 'w') as file:
            json.dump(total_runtime, file)

    print(f"Total Runtime: {total_runtime['total_runtime']} seconds")

    # Check if backup should be triggered based on the total runtime
    if total_runtime['total_runtime'] >= BACKUP_THRESHOLD:
        perform_backup()

if __name__ == "__main__":
    # Continuously check runtime every minute (or any interval)
    while True:
        check_runtime()
        time.sleep(60)  # Check every 60 seconds
