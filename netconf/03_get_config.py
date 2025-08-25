from config.router_config import get_router_connection, print_connection_info, host, port, username

# * --------- Connection Message ---------
print_connection_info()

try:
    Router = get_router_connection()

    print("Get Configuration from Router..........")

    # Get Config
    config = Router.get_config("running")
    print(config)

    Router.close_session()

except Exception as e:
    print(f"Failed to connect {host}:{port}")
    print(f"Error: {e}")
