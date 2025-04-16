import json
import sys
from datetime import datetime

# Paths for session logs and total runtime
TRACKER_DIR = '/workspaces/codespace-tracker/tracker/.codespace-tracker'
SESSION_LOG_PATH = f'{TRACKER_DIR}/session_logs.json'
TOTAL_RUNTIME_PATH = f'{TRACKER_DIR}/total_runtime.json'


def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def calculate_runtime(start_time, end_time):
    """Calculate total time between start and end in seconds."""
    start_time = datetime.fromisoformat(start_time)
    end_time = datetime.fromisoformat(end_time)
    return (end_time - start_time).total_seconds()


def handle_start():
    """Handle the start of a new session."""
    # Record current start time in ISO format
    start_time = datetime.utcnow().isoformat()

    # Save start time to session logs (new session)
    session_logs = load_json(SESSION_LOG_PATH)
    session_logs['sessions'] = session_logs.get('sessions', [])
    session_logs['sessions'].append({'start_time': start_time, 'end_time': None})
    save_json(session_logs, SESSION_LOG_PATH)

    # Reset the total runtime (for testing purposes, can be removed later)
    save_json({'total_runtime': 0}, TOTAL_RUNTIME_PATH)

    print(f"Session started at {start_time}")
    return start_time


def handle_end(end_time):
    """Handle the end of a session and update runtime."""
    # Load session logs
    session_logs = load_json(SESSION_LOG_PATH)

    if 'sessions' not in session_logs or len(session_logs['sessions']) == 0:
        print("No session found!")
        return

    # Get the latest session (most recent one)
    latest_session = session_logs['sessions'][-1]

    # If the session hasn't been closed, set the end time
    if latest_session['end_time'] is None:
        latest_session['end_time'] = end_time
        save_json(session_logs, SESSION_LOG_PATH)

        # Calculate session duration
        session_duration = calculate_runtime(latest_session['start_time'], latest_session['end_time'])

        # Update total runtime
        total_runtime = load_json(TOTAL_RUNTIME_PATH)
        total_runtime['total_runtime'] += session_duration
        save_json(total_runtime, TOTAL_RUNTIME_PATH)

        print(f"Session ended at {end_time}")
        print(f"Session duration: {session_duration} seconds")
        print(f"Total runtime updated: {total_runtime['total_runtime']} seconds")
    else:
        print("Session already ended!")

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide 'start' or 'end' argument.")
        sys.exit(1)

    if sys.argv[1] == 'start':
        handle_start()
    elif sys.argv[1] == 'end':
        if len(sys.argv) < 3:
            print("Please provide end time (ISO format) for 'end' command.")
            sys.exit(1)
        handle_end(sys.argv[2])
    else:
        print("Invalid argument. Use 'start' or 'end'.")
        sys.exit(1)
