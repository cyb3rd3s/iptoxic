![GitHub release (latest by date)](https://img.shields.io/github/v/release/cyb3rd3s/IPToxic?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/cyb3rd3s/IPToxic?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/cyb3rd3s/IPToxic?style=for-the-badge) ![Made For Badge](https://img.shields.io/badge/style-for--the--badge-green?logo=appveyor&style=for-the-badge)
# IP Toxic
IP Toxic scans your target IP with AbuseIPDB and Virus Total API.
## Usage
```
iptoxic.py [Target IP] [Days]
```
**Days** - How many days of history you want to check on AbuseIPDB.
## Example of output
```
-------AbuseIPDB------- 
Reports for last 30 days:
Reported: 301x
Score: 100 %
Country: China
Domain: niaoyun.com
ISP: Shenzhen Qianhai bird cloud computing Co. Ltd.
Last reported reason: Nov 17 11:56:18 db sshd[26112]: User root from 103.45.102.170 not allowed.
...

-------VirusTotal------- 
Results: Found 5 positive from 80 tested sources.
Reason of report: 
EmergingThreats: malicious site 
IPsum: malicious site 
GreenSnow: malicious site 
CyRadar: malicious site 
Threatsourcing: suspicious site 
BlockList: suspicious site 
CRDF: malicious site

Do you want to see complete VirusTotal report on website? (y/n)
```
## Requirements
### Pip dependencies
Necessary python dependencies should be installed with following command.
```
pip install -r requirements.txt
```
### Python 3.8
Whole script is written in Python 3.8., which is recommended for best functionality. Something might not work well in older versions. Python is free to download from [official website](https://www.python.org/downloads/) for all platforms.

## Help & issues
If you have any question, ideas or issues, you can report them through [Issues](https://github.com/cyb3rd3s/IPToxic/issues).
