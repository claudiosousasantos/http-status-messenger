# HTTP Status Messenger

A simple Python function that prints a human-readable message for common HTTP status codes.

## How it works
- **200**: OK - Request succeeded
- **404**: Not Found - Resource does not exist
- **500**: Internal Server Error - Something went wrong on the server
- Any other code prints "Unknown Status" as a fallback

## How to run
```bash
python status_messenger.py
```

## What I learned
- Using `if / elif / else` to handle multiple specific cases with a fallback
- Basic familiarity with common HTTP status codes and what they represent
