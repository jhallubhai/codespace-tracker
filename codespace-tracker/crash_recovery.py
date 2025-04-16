import json
from datetime import datetime

# File paths
SESSION_LOG_PATH = '/workspaces/codespace-tracker/codespace-tracker/.codespace-tracker/session_logs.json'
TOTAL_RUNTIME_PATH = '/workspaces/codespace-tracker/codespace-tracker/.codespace-tracker/total_runtime.json'

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def recover_session():
    """Handle recovery of session data if Codespace crashes or stops abruptly."""
    # Load the session logs
    session_logs = load_json(SESSION_LOG_PATH)

    if 'sessions' in session_logs:
        last_session = session_logs['sessions'][-1]
        # Check if the end time is missing (meaning the session was not closed properly)
        if last_session.get('end_time') is None:
            print("Session was interrupted. Attempting to recover session data...")
            # Set the end time to the current time if it's not set
            last_session['end_time'] = datetime.utcnow().isoformat()
            # Calculate session duration
            session_duration = (datetime.fromisoformat(last_session['end_time']) - datetime.fromisoformat(last_session['start_time'])).total_seconds()
            # Load and update total runtime
            total_runtime = load_json(TOTAL_RUNTIME_PATH)
            total_runtime['total_runtime'] = total_runtime.get('total_runtime', 0) + session_duration

            # Save updated session logs and total runtime
            with open(SESSION_LOG_PATH, 'w') as file:
                json.dump(session_logs, file, indent=4)
            with open(TOTAL_RUNTIME_PATH, 'w') as file:
                json.dump(total_runtime, file, indent=4)

            print("Session data recovered successfully.")

if __name__ == "__main__":
    recover_session()
