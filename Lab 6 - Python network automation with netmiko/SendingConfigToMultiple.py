from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "host": "172.16.9.4",
        "username": "cisco",
        "password": "class",
        "secret": "cisco"
    },
    {
        "device_type": "cisco_ios",
        "host": "172.16.9.7",
        "username": "cisco",
        "password": "class",
        "secret": "cisco"
    }
]
commands = ["banner motd 'Unauthorized access is prohibited'"]
for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_config_set(commands)
    print(f"Commands uitgevoerd op: {device['host']}")
    print(output)


connection.disconnect()

