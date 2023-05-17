from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "host": "172.16.9.4",
        "username": "cisco",
        "password": "class",
    },
    {
        "device_type": "cisco_ios",
        "host": "172.16.9.5",
        "username": "cisco",
        "password": "class",
    }
]
for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_command("show running-config")

    filename = f"{device['host']}_config.txt"
    with open(filename, "w") as file:
        file.write(output)

connection.disconnect()
