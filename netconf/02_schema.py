from config.router_config import get_router_connection, host, port, username

try:
    print(f"Connecting to {host}:{port}\n")
    Router = get_router_connection()

    print("Get Schema...........")
    schema = Router.get_schema("Cisco-IOS-XE-vlan")
    print(schema)

    Router.close_session()

except Exception as e:
    print(f"Error: {e}")
