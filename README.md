# Documentation for labs

## Lab 1 - Python Experiments

### 1.1 Install different tools/packages on Ubuntu DEVASC-LABVM:
- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

#### • Task preparation and implementation:
1. Update & upgrade to prevent errors: `sudo apt update && sudo apt upgrade`
2. Install Python & PIP: `sudo apt install python3 python3-pip`
3. Install Visual Studio Code: `sudo snap install --classic code`
4. Install Jupyter Notebook: `sudo pip3 install jupyter`
5. Install Python IDLE: `sudo apt install idle3`

#### • Task troubleshooting:
Running `sudo apt upgrade && update` prevents errors from occurring.

#### • Task verification:
![Lab 1 - Python Experiments Task Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task1_Verification_1.png)

### 1.2 Run geopy and timedate Python Scripts on the DEVASC-LABVM using the tools above (1.1):
- timedate.py
- geopy-geocoders_location.py
- location.py

#### • Task preparation and implementation:
1. Clone repo: `git clone https://github.com/wleppens/PythonExperiments`
2. Run scripts: `python3 <script>`

#### • Task troubleshooting:
- Geopy: No module named folium, geopy
   1. Pip3 install geopy
   2. Pip3 install folium

#### • Task verification:
![Lab 1 - Python Experiments Task 2 Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task2_Verification_1.png)

### 1.3 Install different tools/packages on Windows OS (deep dive exercise) ++
- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

Investigate the compatibility of the tools with Windows OS and explain briefly if necessary.

#### • Task preparation and implementation:
1. Download Python with installer for Windows (x86 executable installer) from: [Python.org](https://www.python.org/downloads/release/python-380/)
2. Download Visual Studio Code for Windows from: [code.visualstudio.com](https://code.visualstudio.com/download)
3. Download Jupyter Notebook: `pip install jupyter`
4. Download IDLE: `pip install idle`

#### • Task troubleshooting:
If Jupyter gives errors when installed using `pip install jupyter`, try the following:
- Upgrade pip: `python -m pip install --upgrade pip`
- Then install Jupyter: `python -m pip install jupyter`

#### • Task verification:
![Lab 1 - Python Experiments Task 3 Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task3_Verification_1.png)

### 1.4 Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++

- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

Document your findings in 3 steps:

#### • Task preparation and implementation: 
Download 22.04.1 ISO from: [Ubuntu Releases](https://old-releases.ubuntu.com/releases/22.04.1/)
Install the VM
1. Update & upgrade to prevent errors: `sudo apt update && sudo apt upgrade`
2. Install Snap for Visual Studio Code: `sudo apt install snapd`
   - Then install Visual Studio Code: `sudo snap install --classic code`
3. Install Python & PIP: `sudo apt install python3 python3-pip`
4. Install Jupyter Notebook: `pip install jupyter`
5. Install Python IDLE: `sudo apt install idle`

#### • Task troubleshooting:
- Use `sudo apt upgrade && update` to prevent issues.
- If Jupyter doesn't work, try `sudo apt install jupyter` instead of using `pip`.

#### • Task verification:
![Lab 1 - Python Experiments Task 4 Verification](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%201%20-%20Python%20Expirements/Task4_Verification_1.png)
## Lab 2 - Explore rest APIs with API-simulator and postman
A

## Lab 3 - Python Review - Development tools and Classes
A

## Lab 4 - Network Infrastructure and troubleshooting
A

## Lab 5 - Software Development and Design Content
Useful commands:
### Part 1: Software Version Control with Git
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


## Lab 6 - Python Network automation with Netmiko

### Part 1: Connecting to a single iOS device
- Sending single show command

[SendingSingleShowCommand.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingSingleShowCommand.py)
- Sending multiple show commands

[SendingMultipleShowCommand.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingMultipleShowCommand.py)
- Send multiple configuration commands to a single device

[SendingMultipleConfigCommand.py](https://github.com/BrechtKeppens/Devasc_Skills/blob/main/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/SendingMultipleConfigCommand.py)

### Part 2: Connect to multiple IOS devices
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

### Part 4: Create an exciting script as a network engineer
- Create an exciting and challenging script that a network engineer in a programmable era would use every day. Surprise your lecturer!
