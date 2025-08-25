from ncclient import manager
from dotenv import load_dotenv
import os


# *  ---------------- Load Environment Variables ----------------
load_dotenv()


# *  ---------------- Initialize the Router ----------------
host = os.getenv("HOST_CSR1")
port = int(os.getenv("PORT_CSR1"))
username = os.getenv("USERNAME_CSR1")
password = os.getenv("PASSWORD_CSR1")


def get_router_connection():
    return manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={"name": "iosxe"},
        timeout=30,
        allow_agent=False,
        look_for_keys=False
    )


def print_connection_info():
    print(f"Connecting to router at {host}:{port}")
    print(f"Username: {username}\n\n")
