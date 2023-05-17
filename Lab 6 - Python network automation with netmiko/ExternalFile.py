from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": "class",
}

with open("config.txt", "r") as file:
    config_commands = file.read().splitlines()

with ConnectHandler(**device) as connection:
    connection.enable()

    output = connection.send_config_set(config_commands)
    print(output)

    connection.save_config()