def status_message(code):
    """
    Print a human-readable message for a given HTTP status code.
 
    This function only handles a handful of common codes.
    Anything else falls back to a generic "Unknown Status" message.
    """
    if code == 200:
        print("200: OK - Request succeeded")
    elif code == 201:
        print("201: Created - New resource was created successfully")
    elif code == 400:
        print("400: Bad Request - The request was invalid")
    elif code == 401:
        print("401: Unauthorized - Authentication is required")
    elif code == 403:
        print("403: Forbidden - You don't have permission to access this")
    elif code == 404:
        print("404: Not Found - Resource does not exist")
    elif code == 500:
        print("500: Internal Server Error - Something went wrong on the server")
    elif code == 503:
        print("503: Service Unavailable - The server is temporarily down")
    else:
        print(f"{code}: Unknown Status - No message available for this code")
 
 
# A few examples to show how the function behaves
status_message(200)
status_message(201)
status_message(400)
status_message(401)
status_message(403)
status_message(404)
status_message(500)
status_message(503)
status_message(999)
