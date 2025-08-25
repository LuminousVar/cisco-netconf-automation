
from config.router_config import print_connection_info, get_router_connection, host, port, username, password

# * --------- Message Connection -----------
print_connection_info()


try:
    print("Saving configuration.........")
    Router = get_router_connection()

    config = Router.save_config()
    print(config)

    Router.close_session()

except Exception as e:
    print(f"Failed to connect to {host}:{port}")
    print(f"Error: {e}")
