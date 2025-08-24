from config.router_config import get_router_connection, host, port, username

print(f"Connecting to {host}:{port}")
print(f"Username: {username}\n\n")

try:
    print("NETCONF Connection.........")
    Router = get_router_connection()
    print("Connection Success")

    for capability in Router.server_capabilities:
        print(f" -- {capability}")

    Router.close_session()

except Exception as e:
    print(f"Failed to connect to {host}:{port}")
    print(f"Error: {e}")
