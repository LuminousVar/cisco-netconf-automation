import os
from netmiko import ConnectHandler
from dotenv import load_dotenv


load_dotenv()

device = {
    "device_type": "cisco_xe",
    "host": os.getenv("HOST_CSR1"),
    "username": os.getenv("USERNAME_CSR1"),
    "password": os.getenv("PASSWORD_CSR1"),
}

connection = ConnectHandler(**device)

list_comman = [
    "sh ip int br",
    "sh version",
    "sh run conf"
]

for command in list_comman:
    output = connection.send_command(command)
    print(output)
