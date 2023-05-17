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
output = connection.send_command('show interface desc')
print(output)
connection.disconnect()
