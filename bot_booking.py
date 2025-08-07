login_url = "https://web.tarc.edu.my/portal/loginProcess.jsp"
booking_url = "https://web.tarc.edu.my/portal/facilityBooking/AJAXBooking.jsp"

def login_as(session, username, password):
    
    credentials = {"username": username, "password": password}
    response = session.post(login_url, data=credentials)

    if "Dashboard" in response.text:
        print("Login successful.")
    else:
        print("Login failed.")
        raise Exception("Login failed")

    return session

def book_venue(session, payload):
    response = session.post(booking_url, data=payload)
    try:
        if "success" in response.text.lower():
            print("Booking successful")
        else:
            print("Booking failed")
            print("Server response:")
            print(response.text)
    except Exception as e:
        print(f"Error checking booking status: {e}")