
### ! Disclaimer: all images are made using links and are not copy pasted as instructed !
# Lab 1 - Python Experiments

## 1.1 Install different tools/packages on Ubuntu DEVASC-LABVM:
- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

### • Task preparation and implementation:
First install devasc VM, then
1. Update & upgrade to prevent errors: `sudo apt update && sudo apt upgrade`
2. Install Python & PIP: `sudo apt install python3 python3-pip`
3. Install Visual Studio Code: `sudo snap install --classic code`
4. Install Jupyter Notebook: `sudo pip3 install jupyter`
5. Install Python IDLE: `sudo apt install idle3`

### • Task troubleshooting:
Running `sudo apt upgrade && update` prevents errors from occurring.

### • Task verification:
![Lab 1 - Python Experiments Task Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task1_Verification_1.png)
## 1.2 Run geopy and timedate Python Scripts on the DEVASC-LABVM using the tools above (1.1):
- timedate.py
- geopy-geocoders_location.py
- location.py

### • Task preparation and implementation:
1. Clone repo: `git clone https://github.com/wleppens/PythonExperiments`
2. Run scripts using: `python3 <script>.py`

### • Task troubleshooting:
- Geopy: No module named folium, geopy
    `pip3 install geopy`
    `pip3 install folium`

### • Task verification:
![Lab 1 - Python Experiments Task 2 Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task2_Verification_1.png)

## 1.3 Install different tools/packages on Windows OS (deep dive exercise) ++
- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

Investigate the compatibility of the tools with Windows OS and explain briefly if necessary.

### • Task preparation and implementation:
1. Download Python with installer for Windows (x86 executable installer) from: [Python.org](https://www.python.org/downloads/release/python-380/)
2. Download Visual Studio Code for Windows from: [code.visualstudio.com](https://code.visualstudio.com/download)
3. Download Jupyter Notebook: `pip install jupyter`
4. Download IDLE: `pip install idle`

### • Task troubleshooting:
If Jupyter gives errors when installed using `pip install jupyter`, try the following:
- Upgrade pip: `python -m pip install --upgrade pip`
- Then install Jupyter: `python -m pip install jupyter`

### • Task verification:
![Lab 1 - Python Experiments Task 3 Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task3_Verification_1.png)

## 1.4 Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++

- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE


### • Task preparation and implementation: 
Download 22.04.1 ISO from: [Ubuntu Releases](https://old-releases.ubuntu.com/releases/22.04.1/)
Install the VM
1. Update & upgrade to prevent errors: `sudo apt update && sudo apt upgrade`
2. Install Snap for Visual Studio Code: `sudo apt install snapd`
   - Then install Visual Studio Code: `sudo snap install --classic code`
3. Install Python & PIP: `sudo apt install python3 python3-pip`
4. Install Jupyter Notebook: `pip install jupyter`
5. Install Python IDLE: `sudo apt install idle`

### • Task troubleshooting:
- Use `sudo apt upgrade && update` to prevent issues.
- If Jupyter doesn't work, try `sudo apt install jupyter` instead of using `pip`.

### • Task verification:
![Lab 1 - Python Experiments Task 4 Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task4_Verification_1.png)
# Lab 2 - Explore rest APIs with API-simulator and postman
## 2.1 Explore API Documentation Using the API Simulator
### •  Task preparation and implementation:
#### API call using GUI
We visit library.demo.local, it puts us in the Our Books tab. Then we click `Click here for API docs` and click /api/v1 > GET /books
Now we can make our first API call using the GET /books API (GUI) > Try it out > Execute:
#### API call using curl
We make our first API call with curl using `curl -X get "http://library.demo.local/api/v1/books?includeISBN=true" -H accept: application/json` this returns the books with ISBN true

Visible in our books now 
Also Get books shows these
#### Delete book using curl and API key
curl -X DELETE "http://library.demo.local/api/v1/books/4" -H "accept: application/json" -H "X-API-KEY: cisco|7F8RljSITKTpnaa_YJp8fCcgkUrmauZ4wlx6vopD1yk"

#### Post book response
We post a book reponse, we get code 200 success and it is now visible in Our books

###	Task troubleshooting: curl api call wasn’t working -> worked after restart & sudo apt update

###	Task verification:  
API calls:

Response:

Delete book:
## 2.2 Use Postman to make API calls to the API simulator
###	Task preparation and implementation: 
We make POST request with the api key





###	Task troubleshooting: 
Method not allowed but was using get instead of post when trying to retrieve API Key

###	Task verification: 
Confirmation of POST request, id 4 is back in there now. We removed it in the last excercise :






# Lab 3 - Python Review - Development tools and Classes
## 3.1 Python Programming Review

### • Task preparation and implementation:
Important commands:

#### Type(): Returns the variable type 
`string=”e” `
`type(string) => class’str’`

#### f{}: Input variable value in string
`f”The string contains {string}”` returns "The string contains e"

#### .2f : Decimals
`pi = “{:.2f}”.format(num) ` returns 3.14

#### List: [] List of items
`testlist = [“one”,”two”,”three”]`
`del testlist[x]` Removes list item at position x

#### Dictionary: {} Dictionary of items
`Routers: {“R1”:”10.1.1.1”,”R2”:10.2.2.1”}`

#### Len(): Number of items in list
`len(testlist)` returns 3

#### Input: Reads user input:
`input(“enter a value”)` asks for input with the prompt enter a value:

#### Print(“"): prints value to the console
`print(“test”)` prints test

#### if else/elif function example with input & print:
```
age = string(input(’Enter your age:”))
if age >=18:
	print(“You are 18 years of age or older”)
elif age >=16:
		print(“You are 16 years of age or older”)
	else:
		print(“You are under 16 years of age”)
```
You will be prompted to enter your age. It will display whether you are over 18, between 16-18 or under 16 years of age.

#### For loop example: print all items in a list
```
namelist[“Brecht”,”Rick”,”Gert”]

for name in namelist:
print(name)
``` 
Prints every name in namelist

#### While loop example
```
a = 10
b = 0
While a>b:
	print(b)
	b=b+1
```
counts to 10
	
#### Open(“") opens a file
`x = open(“test.txt”) opens a file named text.txt and stores it in x`
### • Task Troubleshooting
None needed
### • Task Verification
Code explained above
## 3.2 Explore Python Development Tools

### • Task preparation and implementation:
Documented findings and important commands:
#### Define & call a function:
```
Def Newfunction:
	Print(“Function called”)
Newfunction()
```
Here we define a function "Newfunction" and call it using Newfunction()
#### Define & call method in a class:
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
Brecht = Person("Brecht", "25")
print(Brecht.name)
print(Brecht.age)
```
Here we define a Person class with a constructor (__init__) that takes name and age parameters. An instance of the class is created with the name "Brecht" and age "25", and the name and age attributes are accessed and displayed.

### • Task Troubleshooting:
None needed

### • Task Verification:
Code explained above

# Lab 4 - Network Infrastructure and troubleshooting
## • Task Preparation and implementation:
#### Install, configure and test the network infrastructure based on the network drawing	
![Network Plan](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Networkplan.png)

#### Proactively determine what is needed to ensure the continuity of the system and network infrastructure
HSRP has been configured on the routers to ensure redundancy. This also supplies the netwerk with scalability for the routers.

We configure a domain name using the following command:
`ip domain name pxl.be`

### Apply best practices to configuration and network security
- Vlans have been configured for best practice segmentation
- For security reasons we chose to use SSH 2.0 using the following commands:
```
crypto key generate rsa 1024
ip ssh version 2
```
Then we made an ssh user:
```
username cisco password class.
```
- All unused ports are in down state and we put them in an unused vlan.
- Sticky mac adress on user ports
- 1:30min timeout exec
### Draw up an IP plan and document your solution
| DEVICE          | INTERFACE   | IP            | VLAN |
|-----------------|-------------|---------------|------|
| LAB-RA09-C-R03  | G0/0.10     | 172.16.9.4    | 10   |
|                 | G0/0.10HSRP | 172.16.9.1    | 10   |
|                 | G0/0.40     | 172.16.9.52   | 40   |
|                 | G0/0.40HSRP | 172.16.9.49   | 40   |
|                 | G0/1        | 10.199.66.109 | /    |
| LAB-RA09-A-SW03 | VLAN10      | 172.16.9.7    | 10   |
### Make sure you can backup and restore device configuration from a backup environment
Router:
```
en
conf t
interface g0/1
ip address 10.199.66.109 255.255.255.224
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 10.199.66.100
copy tftp: running-config
10.199.64.134
lab-ra09-c-r03-confg
interface g0/1
no shutdown
interface g0/0
no shutdown
```
Switch:
```
en
conf t
vlan 10
name "Management Segment Student Rack 09"
exit
interface vlan 10
description "Management Segment Student Rack 09"
ip address 172.16.9.7 255.255.255.240
no shutdown
exit
ip default-gateway 172.16.9.1
interface g0/1
switchport mode trunk
switchport trunk allowed vlan 10
switchport trunk native vlan 99
no shutdown
exit
copy tftp: running-config
10.199.64.134
lab-ra09-c-r03-confg
```


### • Task Troubleshooting:
---
#### - Problem 1: Unable to connect to teachers' switch.
##### Cause: Switch ports were down by default.
##### Solution: Enter no shutdown on the port in question.
---
#### - Problem 2: Unable to ping or tftp from router to remote pc
##### Cause: Routing issue caused the 10.199.66.X network to not route 
##### Solution:  Ping using router's subinterface (using vlan ip address)
##### the `ip tftp source-interface gigabitEthernet 0/0.10` command sets our vlan ip adress as the source for tftp.
---
#### - Problem 3: No connectivity, something changed in configs
##### Cause: Someone unplugged our cable and plugged it into a different port
##### Solution: Followed cables to find out who used our port, and replaced it.
---
#### - Problem 4: Router auto configured ACLs after erase & reload
##### Cause: Bug caused by exec-timeout
##### Solution: Disable exec timeout
---
### • Task Verification:
####Router config
[lab-ra09-c-r03-confg](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-ra09-c-r03-confg)
####Switch config
[lab-ra09-c-sw03-confg](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-ra09-c-sw03-confg)
# Lab 5 - Software Development and Design Content
## 5.1 Software Version Control with Git
#### • Task preparation & implementation
`git config –global {user.name/user.email} “email/name`

#### Explanation: Puts email/name in the git config.
`git config –list`

#### Explanation: Lists current config for git.
`git status`

#### Explanation: Displays the status of the git files in a directory.
`git add`

#### Explanation: Adds a file to the GitHub repository.
`git commit (-m "message")`

#### Explanation: Commits changes to the GitHub repository. Use -m to add a commit message.
`git log`

#### Explanation: Shows all commits in the branch.
`git diff`

#### Explanation: Compares two commits.
`git branch (name)`

#### Explanation: Adds a branch.
`git branch`

#### Explanation: Displays all branches for the repository.
`git branch -d`

#### Explanation: Deletes a branch.
`git checkout`

#### Explanation: Switches between branches.
`git merge`

#### Explanation: Merges the contents of two branches.
`git push`

#### Explanation: Pushes files to the GitHub repository.
`git remote add origin <url>`

#### Explanation: Adds a git URL as a remote alias.

`sed -I ‘s/word1/word2/’ filename`
#### Explanation: Replaces word1 with word2 in a file.

## 5.2 questions and the corresponding answers:
##### What unittest class do you use to create an individual unit of testing?
TestCase

##### How does the test runner know which methods are a test?
They start with “test_”

##### What command will list all of the command line options for unittest shown in the following output?
Python3 -m unittest --help

#### • Task troubleshooting: Authentication updated so we fixed it with personal access token creation: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

#### • Task verification: Code explained above + git working as you can see, we are using it to document

# Lab 6 - Python Network automation with Netmiko
### • Task Preperation and implementation
We need to setup our infrastructure, then connect using netmiko scripts as shown in the code:
```
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
```
## 6.1 Connecting to a single iOS device

- Sending single show command

[SendingSingleShowCommand.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingSingleShowCommand.py)
- Sending multiple show commands

[SendingMultipleShowCommand.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingMultipleShowCommand.py)
- Send multiple configuration commands to a single device

[SendingMultipleConfigCommand.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingMultipleConfigCommand.py)

## 6.2 Connect to multiple IOS devices
- Send show commands to multiple devices

[SendingShowToMultiple.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingShowToMultiple.py)
- Send configuration commands to multiple devices

[SendingConfigToMultiple.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingConfigToMultiple.py)
- Run show commands and save the output

[ShowCommandsSaveOutput.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/ShowCommandsSaveOutput.py)
- Backup the device configurations

[BackupDeviceconfigs.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/BackupDeviceconfigs.py)
- Configure a subset of Interfaces

[SubsetOfDevices.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SubsetOfDevices.py)
- Send device configuration using an external file

[ExternalFile.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/ExternalFile.py)
- Connect using a Python Dictionary
- Execute a script with Functions or classes
- Execute a script with statements (if, ifelse, else)

## 6.4 Create an exciting script as a network engineer
- Create an exciting and challenging script that a network engineer in a programmable era would use every day. Surprise your lecturer!
### • Task troubleshooting
Netmiko wasn't connecting with initial VM settings, set adapter to NAT and it worked
### • Task verification: Code explained above
