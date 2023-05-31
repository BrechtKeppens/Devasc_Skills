from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": "class",
}

try:
    connection = ConnectHandler(**device)
    print("Connection gelukt.")
except Exception as e:
    print("Connection mislukt:", str(e))

if connection:
    output = connection.send_command("show version")
    print(output)
else:
    print("Kan commando niet uitvoeren, geen connection")

if connection:
    connection.disconnect()
    print("Verbinding verbroken.")
else:
    print("Geen verbinding om te verbreken")
