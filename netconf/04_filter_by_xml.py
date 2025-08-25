from config.router_config import get_router_connection, host, port, username

# * --------- Connection Message ---------
print(f"Connecting to {host}:{port}")
print(f"Username: {username}\n\n")

try:
    print("Filter By XML..............")
    Router = get_router_connection()
    print("Connection Success")

    # Use XPath for filtering
    xpath_filter = ("xpath", "/native/interface")

    filter_by = Router.get_config(source="running", filter=xpath_filter)
    print("Filter Success")
    print(filter_by)

    Router.close_session()

except Exception as e:
    print(f"Failed to connect or filter from {host}:{port}")
    print(f"Failed: {e}")
