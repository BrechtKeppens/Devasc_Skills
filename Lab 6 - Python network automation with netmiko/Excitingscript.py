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


commands = [
    'show interfaces',
    'show ip route',
    'show arp'
]


print("Select a device:")
for i, device in enumerate(devices, start=1):
    print(f"{i}. {device['ip']}")
device_choice = int(input("Enter the number of the device: ")) - 1


print("\nSelect a show command:")
for i, command in enumerate(commands, start=1):
    print(f"{i}. {show_command}")
command_choice = int(input("Enter the number of the show command: ")) - 1


selected_device = devices[device_choice]
net_connect = ConnectHandler(**selected_device)

selected_command = show_commands[command_choice]
output = net_connect.send_command(selected_command)

print(f"\nOutput of '{selected_command}':")
print(output)

net_connect.disconnect()
