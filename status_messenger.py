def status_message(code):
    if code == 200:
        print("OK - Request succeeded")
    elif code == 404:
        print("Not Found - Resource does not exist")
    elif code == 500:
        print("Internal Server Error - Something went wrong on the server")
    else:
        print("Unknown Status")

status_message(200)
status_message(404)
status_message(500)
status_message(999)