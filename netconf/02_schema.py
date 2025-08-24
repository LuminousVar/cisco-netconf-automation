from config.router_config import get_router_connection, host, port, username

print(f"Connecting to {host}:{port}")
print(f"Username: {username}\n\n")

try:
    Router = get_router_connection()

    print("Get Schema...........")
    schema = Router.get_schema("Cisco-IOS-XE-vlan")
    print(schema)

    Router.close_session()

except Exception as e:
    print(f"Failed to connected {host}:{port}")
    print(f"Error: {e}")
