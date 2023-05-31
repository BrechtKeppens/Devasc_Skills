from netmiko import ConnectHandler

def connect(device):
    connection = ConnectHandler(**device)
    return connection

def execute_command(connection, command):
    output = connection.send_command(command)
    return output

def disconnect(connection):
    connection.disconnect()

device = {
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": "class",
}

connection = connect(device)
print("Verbonden met device.")

output = execute_command(connection, "show version")
print(output)

disconnect(connection)
print("Verbinding verbroken")
