#!/bin/bash

# Set paths
TRACKER_DIR="/workspaces/codespace-tracker/codespace-tracker/.codespace-tracker"
SESSION_LOG="$TRACKER_DIR/session_logs.json"
TOTAL_RUNTIME="$TRACKER_DIR/total_runtime.json"
RUNTIME_SCRIPT="/workspaces/codespace-tracker/codespace-tracker/runtime_manager.py"

# Log current timestamp as session end
END_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Call Python script to handle logging
python3 "$RUNTIME_SCRIPT" end "$END_TIME"
