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
commands = ["show interface desc", "show ip interface brief"]

for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    print(f"Commands uitgevoerd op: {device['host']}")
    for command in show_commands:
        output = connection.send_command(command)
        print(f"Command:{command}")
        print(output)
        filename = f"{device['host']}_output.txt"
        with open(filename, "a") as file:
            file.write(output)

connection.disconnect()

