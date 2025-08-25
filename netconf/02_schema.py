from config.router_config import get_router_connection, print_connection_info, host, port, username

# * ------------ Connection Message ------------
print_connection_info()

try:
    Router = get_router_connection()

    print("Get Schema...........")
    schema = Router.get_schema("Cisco-IOS-XE-vlan")
    print(schema)

    Router.close_session()

except Exception as e:
    print(f"Failed to connected {host}:{port}")
    print(f"Error: {e}")
