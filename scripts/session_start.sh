#!/bin/bash

# Set paths
TRACKER_DIR="/workspaces/codespace-tracker/tracker/.codespace-tracker"
SESSION_LOG="$TRACKER_DIR/session_logs.json"
TOTAL_RUNTIME="$TRACKER_DIR/total_runtime.json"
RUNTIME_SCRIPT="/workspaces/codespace-tracker/tracker/runtime_manager.py"

# Make sure tracker directory exists
mkdir -p "$TRACKER_DIR"

# Log current timestamp as session start
START_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Call Python script to handle logging
python3 "$RUNTIME_SCRIPT" start "$START_TIME"
