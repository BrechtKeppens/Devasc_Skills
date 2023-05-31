
### ! Disclaimer: all images are made using links and are not copy pasted as instructed, Lab 7 uses regular links !
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
`curl -X DELETE "http://library.demo.local/api/v1/books/4" -H "accept: application/json" -H "X-API-KEY: cisco|7F8RljSITKTpnaa_YJp8fCcgkUrmauZ4wlx6vopD1yk"`

#### Post book response
We post a book reponse, we get code 200 success and it is now visible in Our books

### Task troubleshooting: curl api call wasn’t working -> worked after restart & sudo apt update

### Task verification:  
#### API calls: <br>
#### GUI:
![GUI Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/GUIVerification.png)<br>
#### Curl: 
![Curl Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/CurlVerification.png)
#### Response:
![Response Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/ResponseVerification.png)
#### Delete book:
![Deleted Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/DeletedVerification.png)
## 2.2 Use Postman to make API calls to the API simulator
###	Task preparation and implementation: 
We make POST request with the api key

![Post Request](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/PostRequest.png)


### • Task troubleshooting: 
Method not allowed but was using get instead of post when trying to retrieve API Key

### • Task verification: 
Confirmation of POST request, id 4 is back in there now. We removed it in the last excercise :
![Post Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/PostVerification.png)
## 2.3 Use python to add 100 books to the API simulator
### • Task preparation and implementation:
We will be using the following script to add 100 random books to to the API
Let's look at what it does.
1. Here we can see faker being imported, along with requests and json. `Faker` is used to generate fake data and will be used to generate the 100 random books. `json` provides functions to work with JSON data, `requests` is used for API requests
```
#!/usr/bin/env python3

import requests
import json
from faker import Faker
```
2. We define the variables APIHOST and LOGIN & PASSWORD to authenticate to the API
```
APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"
```
3. We define the getAuthToken function sends a POST request to the API to obtain an authentication token.
If the status code is 200 it returns the token, otherwise it raises an exception.
```
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")
```
4. We define the addBook() function, this sends a POST request to add a book to the API, using the api key and book details as arguments. The book is converted to JSON format and sent as the requests data. If the status code is 200 the function prints a message, otherwise it raises an exception.
```
def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")
```
5. We use our getAuthToken() function to store an auth token in the apiKey variable.
```
apiKey = getAuthToken()
```
6. Now we generate 100 random books using faker, each with a unique id and a random title, author and isbn. Then we add it to the API.
```
fake = Faker()
for i in range(4, 105):
    fakeTitle = fake.catch_phrase()
    fakeAuthor = fake.name()
    fakeISBN = fake.isbn13()
    book = {"id":i, "title": fakeTitle, "author": fakeAuthor, "isbn": fakeISBN}
    addBook(book, apiKey) 

```
### • Task troubleshooting:
None needed
### • Task verification:
[add100books.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/add100RandomBooks.py)
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
[IfElif.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/ifelif.py)<br>
[List.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/list.py)<br>
[MethodInClass.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/methodinclass.py)<br>
[While.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/while.py)<br>
## 3.2 Explore Python Development Tools
### • Task preparation and implementation:
#### Check python version <br>
`python3 -V`
#### See local python environment <br>
`which python3`
#### Create a python virtual environment <br>
`python3 -m venv <name> `
#### Activate the python environment, your prompt will now change <br>
`source <name>/bin/activate`
#### Verify the packages that are installed in the virtual environment <br> 
`pip3 freeze`
#### Install a package in the virtual environment <br>
`pip3 install <package name>`
#### Deactivate the virtual environment <br>
`deactivate` 
#### Verify the packages that are installed in the system environment
`python3 -m pip freeze`
#### Sharing a virtual environment
1. Verify that the virtual environment is active: `source <name>/bin/activate`
2. Send the output of the pip3 freeze command to a text file called requirements.txt: `pip3 freeze > requirements.txt`
3. Deactivate the current environment: `deactivate`
4. Create and activate a new python virtual environment: `python3 -m venv <newname>`&&`source <newname>/bin/activate`
5. Install the same packages in the new virtual environment: `pip3 install -r requirements.txt`
6. Verify the packages are installed: `pip3 freeze`
### • Task Troubleshooting:
None needed
### • Task Verification:
![Lab3_Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab3_Verification.png)
## 3.3 Explore Python Classes

### • Task preparation and implementation:
Documented findings and important commands:
#### Define & call a function:
```
def new_function():
    print("Function called")

new_function()
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
[Function.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Function.py)<br>
[methodinclass.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/methodinclass.py)<br>


# Lab 4 - Network Infrastructure and troubleshooting
### • Task Preparation and implementation:
#### Install, configure and test the network infrastructure based on the network drawing	
![Network Plan](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Networkplan.png)

#### Proactively determine what is needed to ensure the continuity of the system and network infrastructure
- HSRP has been configured on the routers to ensure redundancy. This also supplies the netwerk with scalability for the routers.
```
interface g0/0.10
description Management vlan subinterface
encapsulation dot1q 10
ip address 172.16.9.4 255.255.255.240
standby version 2
standby 10 ip 172.16.9.1
standby 10 priority 150
exit
interface g0/0.40
description Data vlan subinterface
encapsulation dot1q 40
ip address 172.16.9.52 255.255.255.240
standby version 2
standby 40 ip 172.16.9.49
standby 40 priority 150
exit
```
- We configure a domain name using the following command:
`ip domain name pxl.be`

### Apply best practices to configuration and network security
- Vlans have been configured on the switch nfor best practice segmentation
```
vlan 10
name "Management Segment Student Rack 09"
exit
vlan 40
name "Data Users Segment Student Rack 09"
exit
vlan 99
name native
exit
```
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
#### Router:
```
en
conf t
interface g0/1
ip address 10.199.66.109 255.255.255.224
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 10.199.66.100
exit
copy tftp: running-config
>10.199.64.134
>lab-ra09-c-r03-confg
```
After retrieving the config, enter the following to ensure connectivity:
```
conf t
interface g0/1
no shutdown
interface g0/0
no shutdown
```
#### Switch:
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
>10.199.64.134
>lab-ra09-a-sw03-confg
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
#### Router config
[lab-ra09-c-r03-confg](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-ra09-c-r03-confg)
#### Switch config
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
See previous scripts, we always connect using a dictionary
- Execute a script with Functions or classes
[functionusage.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/functionusage.py)
- Execute a script with statements (if, ifelse, else)
[ifelse.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/ifelse.py)
## 6.4 Create an exciting script as a network engineer
This script allows us to choose a show command and a device to run it on. I believe this makes for an exciting script and i challenged myself.
[Excitingscript.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Excitingscript.py)

### • Task troubleshooting
Netmiko wasn't connecting with initial VM settings, set adapter to NAT and it worked
### • Task verification: Scripts above
# Lab 7 YANG, NETCONFIG and RESTCONFIG

## 7.1 Install CSR1000v VM
### • Task preparation and implementation
.IOVA && .iso file downloaded from the teachers onedrive
Install Vmware if needed, virtualbox will not work for this lab
1.	Import the .iova file to vmware
2.	Go to VM settings and click the first CD/DVD in the list, replace the current iso file with the one downloaded from your course instructor	
3.	Launch VM
4.	Ping Devasc machine to ensure connectivity
5.	Visit the CSR1000v webinterface (https://ip)
### • Task troubleshooting
1. We needed an ISO file which the teacher did not have access to but he ended up finding a downloadable version online. 
2. I checked Live CD/DVD which made me encounter some issues, these were resolved when I unchecked the option
3. I did not get an ip address assigned to my adapter in virtualbox, I switched to vmware and this solved the issue 
### • Task verification
[Lab7VM_Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%207%20-%20YANG%2C%20NETCONFIG%20and%20RESTCONFIG%0A/Lab7VM_Verification.png?raw=true)



## 7.2 YANG
### • Task preparation and implementation
We are now gonna review the yang code on the following link: <br>
https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1693/ietf-interfaces.yang <br>
Use this command to copy the yang file to your VM: <br>
`wget https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1693/ietf-interfaces.yang`<br>
Using this command we can view the yang code in the tree format, which is much more readable:
`pyang -f tree ietf-interfaces.yang`

### • Task troubleshooting
None needed
### • Task verification
[Lab7yang_Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%207%20-%20YANG%2C%20NETCONFIG%20and%20RESTCONFIG%0A/Lab7yang_Verification.png)
## 7.3 NETCONF
### • Task preparation and implementation
1.SSH to the vm using ssh cisco@ip and type Netconf-yang to start the daemon. You can also type this command in the vm directly.
2. Now we can connect to Netconf using the ssh command: ssh cisco@ip -p 830 -s netconf
3. Now we send a hello message to start a Netconf session, past the following code into the ssh prompt:
```
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
</capabilities>
</hello>
]]>]]>
Confirm the session using show Netconf-yang sessions
```
Now we’re gonna send a rpc get message:
```
<rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<get>
<filter>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
</get>
</rpc>
]]>]]>
```
We get an xml response, we prettify this using: https://jsonformatter.org/xml-pretty-print
This is way more readable.

To close our session we send the following rpc message:
```
<rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<close-session />
</rpc>
```
Now we’re gonna use ncclient for our connection, we verify it’s installed by running the following command on our VM: `pip3 list --format=columns | more`

1. We make a new dir in our devnet-src folder using mkdir Netconf
2. We make a new python file with the following code;
```
from ncclient import manager
m = manager.connect(
host="192.168.199.128",
port=830,
username="cisco",
password="cisco123!",
hostkey_verify=False
)
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
print(capability)
```
Now we save & run this file in vscode terminal
```
cd Netconf
Python3 filename (ncclient-netconf.py)
```
We replace the code after the m = statement with this:
```
netconf_reply = m.get_config(source="running")
print(netconf_reply)
```
Now we’re gonna prettify it using a python function:
```
import the module by adding this to the start of the script: 
import xml.dom.minidom
```

This is how we replace a hostname using ncclient:
```
netconf_hostname = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<hostname>NEWHOSTNAME</hostname>
</native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
```
Now we’re gonna configure a new loopback interface using ncclient:
```
netconf_loopback = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<Loopback>
<name>1</name>
<description>My first NETCONF loopback</description>
<ip>
<address>
<primary>
<address>10.1.1.1</address>
<mask>255.255.255.0</mask>
</primary>
</address>
</ip>
</Loopback>
</interface>
</native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```


### • Task troubleshooting 
None required
### • Task verification
[Lab7Netconf_Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%207%20-%20YANG%2C%20NETCONFIG%20and%20RESTCONFIG%0A/Lab7Netconf_Verification.png)


## 7.4 RESTCONF
### • Task preparation and implementation
First we verify connectivity by pinging 192.168.199.128 <br>
Then we ssh using ssh cisco@ip(192.168.199.128) <br> 
Verify the RestCONF daemons are running using:`show platform software yang-management process`
 
We enter `conf t` and then `restconf` to enable restconf <br>
Now we enter ip `http secure-server` to enable the https server <br>
And ip `http authentication local` to specify the server should use the local authentication database <br>

1. We go into postman settings, File>Settings>General> SSL certificate verification OFF
2. Now that we’ve configured postman. Lets go to the launchpad.
3. Click the + sign to open a GET untitled request
4. We enter `https://192.168.199.128/restconf/` in the enter request url field.
5. Now we click the authorization tab, next to params  
6. Select basic auth, username: cisco, password: cisco123!
7. Verify that content type key accept with application/yand-data+json is still there
We send the request and get this response:
```
{
	"ietf-restconf:restconf": {
		"data": {},
		"operations: {},
		"yang-library-version": "2016-06-21"
	}
}
```
Now we add: data/ietf-interfaces:interfaces after restconf/ in the url: `https://192.168.199.128/restconf/data/ietf-interfaces:interfaces`
This retrieves the interfaces information
We can try getting the information for a specific interface, by adding `/interfaces=<interface name>`
We use GigabitEthernet1 for the task verification.

We are now going to assign a static ip address to our interface instead of dhcp by using:
`ip address 192.168.199.128 255.255.255.0` in config mode for GE/1 interface

Now we will add a loopback interface with a PUT request, lets enter the following url: `https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback1` to address the loopback interface
We enter the following json code in BODY:
```
{
   "ietf-interfaces:interface": {
     "name": "Loopback1",  
     "description": "My first RESTCONF loopback",
     "type": "iana-if-type:softwareLoopback",
     "enabled": true,
     "ietf-ip:ipv4": {
       "address": [
         {
          "ip": "10.1.1.1",
          "netmask": "255.255.255.0"
         }
        ]
       },
    "ietf-ip:ipv6": {}
}
```
Click send, we get status 201: created

Now we are going to create a python script to make a GET request:
```
import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = https://192.168.199.128/restconf/data/ietf-interfaces:interfaces
headers = { "Accept": "application/yang-data+json",
"Content-type":"application/yang-data+json"
}
basicauth = ("cisco", "cisco123!")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)
response_json = resp.json()
print(json.dumps(response_json, indent=4))
```
We import the json and requests module and disable ssl cert warnings
We create the api url variable, and create the dictionary variable for the headers and basicauth for authentication purposes.

Python PUT request

We build a different script for this:
```
import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.199.128/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"
headers = { "Accept": "application/yang-data+json",
"Content-type":"application/yang-data+json"
}
basicauth = ("cisco", "cisco123!")
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth,
headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message:{}'.format(resp.status_code,resp.json()))
```
### • Task troubleshooting
None needed
### • Task verification
#### Postman GET
[Lab7PostmanGET_Verification](https://github.com/BrechtKeppens/Devasc_Skills/raw/main/Lab%207%20-%20YANG%2C%20NETCONFIG%20and%20RESTCONFIG/Lab7PostmanGET_Verification.png)

#### Python GET
[Lab7PythonGet_Verification](https://github.com/BrechtKeppens/Devasc_Skills/raw/main/Lab%207%20-%20YANG%2C%20NETCONFIG%20and%20RESTCONFIG/Lab7PythonGet_Verification.png)

#### Python PUT
![Lab7PythonPUT_Verification](https://github.com/BrechtKeppens/Devasc_Skills/raw/main/Lab%207%20-%20YANG%2C%20NETCONFIG%20and%20RESTCONFIG/Lab7PythonPUT_Verification.png)
![Lab 1 - Python Experiments Task Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task1_Verification_1.png)

