#!/bin/bash

echo "🚀 Running setup.sh to initialize codespace-tracker environment..."

TRACKER_DIR="/workspaces/codespace-tracker/tracker/.codespace-tracker"
SESSION_LOG="$TRACKER_DIR/session_logs.json"
TOTAL_RUNTIME="$TRACKER_DIR/total_runtime.json"
LOG_DIR="/workspaces/codespace-tracker/logs"
DEBUG_LOG="$LOG_DIR/debug.log"
SESSION_START_FILE="$TRACKER_DIR/session_start.json"

# 1. Tracker Directory
if [ ! -d "$TRACKER_DIR" ]; then
    echo "📁 Creating tracker directory at $TRACKER_DIR"
    mkdir -p "$TRACKER_DIR"
else
    echo "✅ Tracker directory already exists!"
fi

if [ ! -f "$SESSION_START_FILE" ]; then
    echo "🆕 Creating empty session_start.json"
    echo '{}' > "$SESSION_START_FILE"
fi

# 2. Log Folder for Debug
mkdir -p "$LOG_DIR"
touch "$DEBUG_LOG"

# 3. JSON File Creation
if [ ! -f "$SESSION_LOG" ]; then
    echo "🆕 Creating $SESSION_LOG"
    echo "[]" > "$SESSION_LOG"
fi

if [ ! -f "$TOTAL_RUNTIME" ]; then
    echo "🆕 Creating $TOTAL_RUNTIME"
    echo '{"total_seconds": 0}' > "$TOTAL_RUNTIME"
fi

# 4. Validate JSON (Basic check)
python3 -c "import json; json.load(open('$SESSION_LOG'))" 2>/dev/null || echo "⚠️ session_logs.json is invalid!"
python3 -c "import json; json.load(open('$TOTAL_RUNTIME'))" 2>/dev/null || echo "⚠️ total_runtime.json is invalid!"

# 5. Make Shell Scripts Executable
chmod +x /workspaces/codespace-tracker/codespace-tracker/session_start.sh
chmod +x /workspaces/codespace-tracker/codespace-tracker/session_end_handler.sh

# 6. Optional: Install Python Requirements (future-proof)
REQ_FILE="/workspaces/codespace-tracker/codespace-tracker/requirements.txt"
if [ -f "$REQ_FILE" ]; then
    pip3 install -r "$REQ_FILE"
else
    echo "📦 No requirements.txt found. Skipping pip install."
fi

# 7. First Launch Log
echo "🕒 First launch time: $(date)" >> "$DEBUG_LOG"

echo "✅ setup.sh completed! System taiyaar hai, chalo ab aag lagaate hain 🔥"
