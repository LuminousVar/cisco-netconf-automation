from config.router_config import get_router_connection, print_connection_info, host, port, username

# * ------------ Connection Message ------------
print_connection_info()

configuration = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>testing-coba-coba123</hostname>
    </native>
</config>
"""

try:
    print("Configuring Hostname.........")
    Router = get_router_connection()

    config = Router.edit_config(config=configuration, target="running")
    print(config)

    Router.close_session()

except Exception as e:
    print(f"Failed to connect to {host}:{port}")
    print(f"Error: {e}")
