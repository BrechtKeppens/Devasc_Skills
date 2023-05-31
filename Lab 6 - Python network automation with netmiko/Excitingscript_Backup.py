from netmiko import ConnectHandler
import datetime



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


for device in devices:
    net_connect = ConnectHandler(**device)
    hostname = net_connect.send_command('show run | include hostname')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f'{hostname.strip()}_backup_{timestamp}.txt'
    backup_output = net_connect.send_command('show run')
    with open(backup_filename, 'w') as backup_file:
        backup_file.write(backup_output)
    print(f'Configuration backup saved for {hostname.strip()} in {backup_filename}')
    net_connect.disconnect()
