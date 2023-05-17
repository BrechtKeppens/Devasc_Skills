from netmiko import ConnectHandler

cisco_01 = {
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": "class",
    "secret": "cisco"
}
connection = ConnectHandler(**cisco_01)
connection.enable() 
commands = ["vlan 20", "name testBK", "exit"]
output = connection.send_config_set(commands)
print(output)
connection.disconnect()

