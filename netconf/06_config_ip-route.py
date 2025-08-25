from config.router_config import get_router_connection, host, port, username, print_connection_info


# *-------- Message --------
print_connection_info()


configuration = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
            <route>
                <ip-route-interface-forwarding-list>
                    <prefix>192.168.160.0</prefix>
                    <mask>255.255.255.0</mask>
                    <fwd-list>
                        <fwd>192.168.1.1</fwd>
                    </fwd-list>
                </ip-route-interface-forwarding-list>
            </route>
        </ip>
    </native>
</config>
"""

try:
    print("Configuring IP Route.......")

    Router = get_router_connection()

    config = Router.edit_config(config=configuration, target="running")
    print(config)

    Router.close_session()

except Exception as e:
    print(f"Failed to connect to {host}:{port}")
    print(f"Error: {e}")
