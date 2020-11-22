#!/usr/bin/env python3
# Author: Roman Kulich @ 2020
# Version: v0.0.8

banner = ('''
  _____ _____    _______        _      
 |_   _|  __ \  |__   __|      (_)     
   | | | |__) |    | | _____  ___  ___ 
   | | |  ___/     | |/ _ \ \/ / |/ __|
  _| |_| |         | | (_) >  <| | (__ 
 |_____|_|         |_|\___/_/\_\_|\___|                                                                                                                                                                                            
v0.0.8
''')

import argparse
import requests
import webbrowser

Abuse_API = 'YOUR API KEY'
VirusTotal_API = 'YOUR API KEY'
list_of_scanners = ["Feodo Tracker",
"CLEAN MX","DNS8","MalSilo","NotMining","VX Vault","securolytics","Tencent","MalwarePatrol","MalBeacon","Comodo Valkyrie Verdict","PhishLabs","EmergingThreats","Sangfor",
"K7AntiVirus","Spam404","Virusdie External Site Scan","Artists Against 419","IPsum","Cyren","Quttera","AegisLab WebGuard","MalwareDomainList","Lumu","zvelo","Google Safebrowsing",
"Kaspersky","BitDefender","GreenSnow","G-Data","OpenPhish","Malware Domain Blocklist","AutoShun","Trustwave","Web Security Guard","Cyan","CyRadar","desenmascara.me","ADMINUSLabs",
"CINS Army","Dr.Web","AlienVault","Emsisoft","Spamhaus","malwares.com URL checker","Phishtank","EonScope","Malwared","Avira","Cisco Talos IP Blacklist","CyberCrime","Antiy-AVL",
"Forcepoint ThreatSeeker","SCUMWARE.org","Certego","URLhaus","Yandex Safebrowsing","ESET","Threatsourcing","BlockList","SecureBrain","Nucleon","PREBYTES","Sophos","Blueliv",
"Hoplite Industries","Netcraft","CRDF","ThreatHive","BADWARE.INFO","FraudScore","Quick Heal","Rising","StopBadware","Sucuri SiteCheck","Fortinet","StopForumSpam","ZeroCERT","Baidu-International","Phishing Database"]

TGREEN =  '\033[32m'
TWHITE = '\033[37m'
TRED = '\033[31m'

parser = argparse.ArgumentParser()
parser.add_argument('ip')
parser.add_argument('days')
args = parser.parse_args()

ip = (args.ip)
days = (args.days)
headers = {
    'Key': Abuse_API,
    'Accept': 'application/json',
}

params = (
    ('maxAgeInDays', days),
    ('verbose', ''),
    ('ipAddress', ip),
)

response_ab = requests.get('https://api.abuseipdb.com/api/v2/check', headers=headers, params=params)
json = response_ab.json()

print(banner)

if str(json['data']['totalReports']) == "0":
    print(TRED +"Sorry, this IP wasn't reported yet on AbuseIPDB.",TWHITE)
    print("")
else:
    print("")
    print(TGREEN + "-------AbuseIPDB-------",TWHITE)
    print(TGREEN + "Reports for last " + days + " days:")
    print(TGREEN + "Reported:", TWHITE + str(json['data']['totalReports']) + "x")
    print(TGREEN + "Score:", TWHITE + str(json['data']['abuseConfidenceScore']) + " %")
    print(TGREEN + "Country:", TWHITE + str(json['data']['countryName']))
    print(TGREEN + "Domain:", TWHITE + str(json['data']['domain']))
    print(TGREEN + "ISP:", TWHITE + str(json['data']['isp']))
    print(TGREEN + "Last reported reason:", TWHITE + str(json['data']['reports'][0]['comment']))
    print("")

url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey':VirusTotal_API,'resource':ip} 
response_vt = requests.get(url, params=params)
json = response_vt.json()

if str(json['response_code']) == "0":
    print(TRED +"Sorry, this IP wasn't reported yet on VirusTotal.",TWHITE)
else:
    print(TGREEN + "-------VirusTotal-------", TWHITE)
    print(TGREEN + "Results:", TWHITE + "Found " + TRED + str(json['positives']), TWHITE + "positive from " + str(json['total']) + " tested sources.")
    if str(json['positives']) !="0":
        print(TGREEN + "Reason of report:",TWHITE)
        for scanner in list_of_scanners:
            if str(json['scans'][(scanner)]['detected']) == "True" or str(json['scans'][(scanner)]['result']) == "suspicious site": 
                print((scanner) + ": " + TRED + str(json['scans'][(scanner)]['result']),TWHITE)
        searchsploit = input("Do you want to see complete VirusTotal report on website? (y/n) ")
        if searchsploit == "y":
            webbrowser.open(str(json['permalink']), new=0, autoraise=True)
        else:
            print("Finished")
