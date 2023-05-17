from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": "class",
}

interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2"]

commands = [
    "description Configured on through netmiko",
    "switchport mode access",
    "switchport access vlan 20",
]

with ConnectHandler(**device) as connection:
    connection.enable()

    for interface in interfaces:
        config_commands = [f"interface {interface}"] + commands + ["exit"]
        output = connection.send_config_set(config_commands)
        print(output)
    connection.save_config()