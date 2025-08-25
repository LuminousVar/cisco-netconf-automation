from config.router_config import print_connection_info, get_router_connection, host, port, username, password

# * --------- Message Connection ----------
print_connection_info()


try:
    print("Saving configuration to XML file.......")
    Router = get_router_connection()

    output = Router.get_config("running")

    with open("netconf/router_running_config.xml", "w") as xml_file:
        xml_file.write(str(output))
        xml_file.close()

    Router.close_session()

except Exception as e:
    print(f"Failed to connect to {host}:{port}")
    print(f"Error: {e}")
