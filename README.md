# Documentation for labs
## Lab 1 - Python Experiments
### 1.1 Install different tools/packages on Ubuntu DEVASC-LABVM:
-	Python 3.8 and PIP
-	Visual Studio Code
-	Jupyter Notebook
-	Python IDLE

#### •	Task preparation and implementation:
1.	Update & grade to prevent errors:  sudo apt upgrade && sudo apt upgrade
2.	Install python & pip3(already done): sudo apt install python3 python3-pip
3.	Install vscode(already done): sudo snap install –classic code
4.	Install jupyter notebook: sudo pip3 install jupyter
5.	Install idle: sudo apt install idle3

### •	Task troubleshooting:
Sudo apt upgrade && update prevents errors from occuring

### •	Task verification:  
	Lab 1 - Python Experiments/Task1_Verification_1.png 
	

### 1.2 Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (1.1):
-	timedate.py
-	geopy-geocoders_location.py
-	location.py

### •	Task preparation and implementation:
1.	Clone repo: git clone https://github.com/wleppens/PythonExperiments
2.	Run scripts > python3 <script>

### •	Task troubleshooting:
	Geopy: No module named folium, geopy 
1.	Pip3 install geopy
2.	Pip3 install folium

### •	Task verification:    
	Lab 1 - Python Experiments/Task2_Verification_1.png



1.3 Install different tools/packages on Windows OS (deep dive exercise) ++


-	Python 3.8 and PIP

-	Visual Studio Code

-	Jupyter Notebook

-	Python IDLE

Investigate the compatibility of the tools with Windows OS and explain briefly if necessary.

Document your findings in 3 steps:

•	Task preparation and implementation:
1.	Download python with installer for windows: (x86 executable installer)
From: https://www.python.org/downloads/release/python-380/
2.	Download visual studio code for windows
From: https://code.visualstudio.com/download
3.	Download jupyter notebook
Pip install jupyter
4.	Download idle:
Pip install idle


•	Task troubleshooting:
Jupyter gives errors if installed using pip install jupyter
Use:  python -m pip install --upgrade pip
	Then python -m pip install jupyter
	

•	Task verification:
     
1.4 Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++


-	Python 3.8 and PIP

-	Visual Studio Code

-	Jupyter Notebook

-	Python IDLE

Document your findings in 3 steps:

•	Task preparation and implementation: 
Download 22.04.1 iso:
https://old-releases.ubuntu.com/releases/22.04.1/
Install the VM
1.	Update & upgrade to prevent errors: Sudo apt update && upgrade
2.	Install snap for vscode: Sudo apt install snapd
Sudo snap install –classic code
3.	Install python & pip: Sudo apt install python3 python3-pip
4.	Install jupyter: Pip install jupyter
5.	Install idle: Sudo apt install idle


•	Task troubleshooting: sudo apt upgrade && update 
Jupyter: pip doesn’t work, sudo apt install jupyter

•	Task verification: 
## Lab 2 - Explore rest apis with API-simulator and postman
A
## Lab 3 - Python Review - Development tools and Classes
a
## Lab 4 - Network Infrastructure and troubleshooting
a
## Lab 5 - Software Development and Design Content
a
## Lab 6 - Python Network automation with netmiko

