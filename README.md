# HTTP Status Messenger
 
A simple Python function that prints a human-readable message for common HTTP status codes.
 
## How it works
The `status_message()` function takes a status code (a number) and prints back what it means:
 
| Code | Meaning |
|------|---------|
| 200  | OK - Request succeeded |
| 201  | Created - New resource was created successfully |
| 400  | Bad Request - The request was invalid |
| 401  | Unauthorized - Authentication is required |
| 403  | Forbidden - You don't have permission to access this |
| 404  | Not Found - Resource does not exist |
| 500  | Internal Server Error - Something went wrong on the server |
| 503  | Service Unavailable - The server is temporarily down |
 
Any code not listed above prints **"Unknown Status"** as a fallback, along with the code itself so you still know what was passed in.
 
## How to run
```bash
python status_messenger.py
```
 
You should see output like:
```
200: OK - Request succeeded
201: Created - New resource was created successfully
400: Bad Request - The request was invalid
401: Unauthorized - Authentication is required
403: Forbidden - You don't have permission to access this
404: Not Found - Resource does not exist
500: Internal Server Error - Something went wrong on the server
503: Service Unavailable - The server is temporarily down
999: Unknown Status - No message available for this code
```
 
## Try it yourself
Call the function with your own code at the bottom of the file:
```python
status_message(418)
```
 
## What I learned
- Using `if / elif / else` to handle multiple specific cases with a fallback
- Basic familiarity with common HTTP status codes and what they represent
- Using an f-string (`f"..."`) to include a variable's value inside a printed message
