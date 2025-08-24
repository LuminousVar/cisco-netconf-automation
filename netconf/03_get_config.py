from config.router_config import get_router_connection, host, port, username

# * --------- Connection Message ---------
print(f"Connecting to {host}:{port}")
print(f"Username: {username}\n\n")


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
