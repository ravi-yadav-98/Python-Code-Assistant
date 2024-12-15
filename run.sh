#!/bin/bash

# Path to your virtual environment's activation script
VENV_PATH="venv/Scripts/activate"

# Function to log messages with timestamps
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Check if Git is installed
if ! command -v git >/dev/null 2>&1; then
    echo "Error: Git is not installed or not in the PATH."
    exit 1
fi

# Step 1: Activate the virtual environment
log_message "Activating the virtual environment..."
if source "$VENV_PATH"; then
    log_message "Virtual environment activated successfully."
else
    log_message "Error: Failed to activate the virtual environment. Check the path: $VENV_PATH"
    exit 1
fi

# Step 2: Run the Python file
log_message "Starting script execution: code_assistant.py..."
if python code_assistant.py; then
    log_message "Successfully executed code_assistant.py."
else
    log_message "Error: Failed to execute code_assistant.py."
    exit 1  # Exit if the script fails
fi

# Step 3: Add all changes to Git
log_message "Adding changes to Git..."
if git add .; then
    log_message "Changes added to Git successfully."
else
    log_message "Error: Failed to add changes to Git."
    exit 1  # Exit if the git add fails
fi

# Step 4: Commit changes with a timestamp
COMMIT_MESSAGE="Automated commit - $(date '+%Y-%m-%d %H:%M:%S')"
log_message "Committing changes with message: '$COMMIT_MESSAGE'..."
if git commit -m "$COMMIT_MESSAGE"; then
    log_message "Changes committed successfully."
else
    log_message "Error: Failed to commit changes."
    exit 1  # Exit if the git commit fails
fi

# Step 5: Push changes to the remote repository
log_message "Pushing changes to the remote repository..."
if git push; then
    log_message "Changes pushed to remote repository successfully."
else
    log_message "Error: Failed to push changes to remote repository."
    exit 1  # Exit if the git push fails
fi

log_message "Automation process completed successfully!"
