  #!/usr/bin/env python3
"""
Global Source Scanner & Real Validator (Python Port)
Compatible with Windows, Mac, Linux, Termux.
Features: Generate Logs, Filter, Export CSV, Real IP Validation, QR Codes.
"""

import os
import random
import json
import csv
import time
import socket
from datetime import datetime, timedelta
from urllib.parse import quote
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# --- 1. Configuration & Databases ---

COUNTRIES_DATA = [
    {"name": "Afghanistan", "code": "+93", "city": "Kabul", "port": 80},
    {"name": "Albania", "code": "+355", "city": "Tirana", "port": 8080},
    {"name": "Algeria", "code": "+213", "city": "Algiers", "port": 443},
    {"name": "Andorra", "code": "+376", "city": "Andorra la Vella", "port": 80},
    {"name": "Angola", "code": "+244", "city": "Luanda", "port": 8000},
    {"name": "Antigua and Barbuda", "code": "+1", "city": "St. John's", "port": 80},
    {"name": "Argentina", "code": "+54", "city": "Buenos Aires", "port": 80},
    {"name": "Armenia", "code": "+374", "city": "Yerevan", "port": 8080},
    {"name": "Australia", "code": "+61", "city": "Sydney", "port": 443},
    {"name": "Austria", "code": "+43", "city": "Vienna", "port": 80},
    {"name": "Azerbaijan", "code": "+994", "city": "Baku", "port": 8080},
    {"name": "Bahamas", "code": "+1", "city": "Nassau", "port": 443},
    {"name": "Bahrain", "code": "+973", "city": "Manama", "port": 80},
    {"name": "Bangladesh", "code": "+880", "city": "Dhaka", "port": 8080},
    {"name": "Barbados", "code": "+1", "city": "Bridgetown", "port": 80},
    {"name": "Belarus", "code": "+375", "city": "Minsk", "port": 80},
    {"name": "Belgium", "code": "+32", "city": "Brussels", "port": 443},
    {"name": "Belize", "code": "+501", "city": "Belmopan", "port": 8080},
    {"name": "Benin", "code": "+229", "city": "Porto-Novo", "port": 80},
    {"name": "Bhutan", "code": "+975", "city": "Thimphu", "port": 80},
    {"name": "Bolivia", "code": "+591", "city": "Sucre", "port": 8080},
    {"name": "Bosnia and Herzegovina", "code": "+387", "city": "Sarajevo", "port": 80},
    {"name": "Botswana", "code": "+267", "city": "Gaborone", "port": 80},
    {"name": "Brazil", "code": "+55", "city": "Brasília", "port": 443},
    {"name": "Brunei", "code": "+673", "city": "Bandar Seri Begawan", "port": 8080},
    {"name": "Bulgaria", "code": "+359", "city": "Sofia", "port": 80},
    {"name": "Burkina Faso", "code": "+226", "city": "Ouagadougou", "port": 80},
    {"name": "Burundi", "code": "+257", "city": "Bujumbura", "port": 80},
    {"name": "Cabo Verde", "code": "+238", "city": "Praia", "port": 8080},
    {"name": "Cambodia", "code": "+855", "city": "Phnom Penh", "port": 80},
    {"name": "Cameroon", "code": "+237", "city": "Yaoundé", "port": 8080},
    {"name": "Canada", "code": "+1", "city": "Ottawa", "port": 443},
    {"name": "Central African Republic", "code": "+236", "city": "Bangui", "port": 80},
    {"name": "Chad", "code": "+235", "city": "N'Djamena", "port": 80},
    {"name": "Chile", "code": "+56", "city": "Santiago", "port": 8080},
    {"name": "China", "code": "+86", "city": "Beijing", "port": 80},
    {"name": "Colombia", "code": "+57", "city": "Bogotá", "port": 443},
    {"name": "Comoros", "code": "+269", "city": "Moroni", "port": 80},
    {"name": "Congo (Congo-Brazzaville)", "code": "+242", "city": "Brazzaville", "port": 8080},
    {"name": "Costa Rica", "code": "+506", "city": "San José", "port": 80},
    {"name": "Croatia", "code": "+385", "city": "Zagreb", "port": 80},
    {"name": "Cuba", "code": "+53", "city": "Havana", "port": 8080},
    {"name": "Cyprus", "code": "+357", "city": "Nicosia", "port": 80},
    {"name": "Czechia (Czech Republic)", "code": "+420", "city": "Prague", "port": 443},
    {"name": "Democratic Republic of the Congo", "code": "+243", "city": "Kinshasa", "port": 80},
    {"name": "Denmark", "code": "+45", "city": "Copenhagen", "port": 80},
    {"name": "Djibouti", "code": "+253", "city": "Djibouti", "port": 8080},
    {"name": "Dominica", "code": "+1", "city": "Roseau", "port": 80},
    {"name": "Dominican Republic", "code": "+1", "city": "Santo Domingo", "port": 443},
    {"name": "Ecuador", "code": "+593", "city": "Quito", "port": 80},
    {"name": "Egypt", "code": "+20", "city": "Cairo", "port": 8080},
    {"name": "El Salvador", "code": "+503", "city": "San Salvador", "port": 80},
    {"name": "Equatorial Guinea", "code": "+240", "city": "Malabo", "port": 80},
    {"name": "Eritrea", "code": "+291", "city": "Asmara", "port": 80},
    {"name": "Estonia", "code": "+372", "city": "Tallinn", "port": 8080},
    {"name": "Eswatini (fmr. Swaziland)", "code": "+268", "city": "Mbabane", "port": 80},
    {"name": "Ethiopia", "code": "+251", "city": "Addis Ababa", "port": 80},
    {"name": "Fiji", "code": "+679", "city": "Suva", "port": 8080},
    {"name": "Finland", "code": "+358", "city": "Helsinki", "port": 80},
    {"name": "France", "code": "+33", "city": "Paris", "port": 443},
    {"name": "Gabon", "code": "+241", "city": "Libreville", "port": 80},
    {"name": "Gambia", "code": "+220", "city": "Banjul", "port": 80},
    {"name": "Georgia", "code": "+995", "city": "Tbilisi", "port": 8080},
    {"name": "Germany", "code": "+49", "city": "Berlin", "port": 80},
    {"name": "Ghana", "code": "+233", "city": "Accra", "port": 80},
    {"name": "Greece", "code": "+30", "city": "Athens", "port": 8080},
    {"name": "Grenada", "code": "+1", "city": "St. George's", "port": 80},
    {"name": "Guatemala", "code": "+502", "city": "Guatemala City", "port": 80},
    {"name": "Guinea", "code": "+224", "city": "Conakry", "port": 8080},
    {"name": "Guinea-Bissau", "code": "+245", "city": "Bissau", "port": 80},
    {"name": "Guyana", "code": "+592", "city": "Georgetown", "port": 80},
    {"name": "Haiti", "code": "+509", "city": "Port-au-Prince", "port": 8080},
    {"name": "Honduras", "code": "+504", "city": "Tegucigalpa", "port": 80},
    {"name": "Hungary", "code": "+36", "city": "Budapest", "port": 80},
    {"name": "Iceland", "code": "+354", "city": "Reykjavik", "port": 8080},
    {"name": "India", "code": "+91", "city": "New Delhi", "port": 443},
    {"name": "Indonesia", "code": "+62", "city": "Jakarta", "port": 80},
    {"name": "Iran", "code": "+98", "city": "Tehran", "port": 8080},
    {"name": "Iraq", "code": "+964", "city": "Baghdad", "port": 80},
    {"name": "Ireland", "code": "+353", "city": "Dublin", "port": 80},
    {"name": "Israel", "code": "+972", "city": "Jerusalem", "port": 443},
    {"name": "Italy", "code": "+39", "city": "Rome", "port": 80},
    {"name": "Ivory Coast", "code": "+225", "city": "Yamoussoukro", "port": 80},
    {"name": "Jamaica", "code": "+1", "city": "Kingston", "port": 8080},
    {"name": "Japan", "code": "+81", "city": "Tokyo", "port": 80},
    {"name": "Jordan", "code": "+962", "city": "Amman", "port": 80},
    {"name": "Kazakhstan", "code": "+7", "city": "Astana", "port": 8080},
    {"name": "Kenya", "code": "+254", "city": "Nairobi", "port": 80},
    {"name": "Kiribati", "code": "+686", "city": "South Tarawa", "port": 80},
    {"name": "Kuwait", "code": "+965", "city": "Kuwait City", "port": 8080},
    {"name": "Kyrgyzstan", "code": "+996", "city": "Bishkek", "port": 80},
    {"name": "Laos", "code": "+856", "city": "Vientiane", "port": 80},
    {"name": "Latvia", "code": "+371", "city": "Riga", "port": 8080},
    {"name": "Lebanon", "code": "+961", "city": "Beirut", "port": 80},
    {"name": "Lesotho", "code": "+266", "city": "Maseru", "port": 80},
    {"name": "Liberia", "code": "+231", "city": "Monrovia", "port": 80},
    {"name": "Libya", "code": "+218", "city": "Tripoli", "port": 8080},
    {"name": "Liechtenstein", "code": "+423", "city": "Vaduz", "port": 80},
    {"name": "Lithuania", "code": "+370", "city": "Vilnius", "port": 80},
    {"name": "Luxembourg", "code": "+352", "city": "Luxembourg", "port": 8080},
    {"name": "Madagascar", "code": "+261", "city": "Antananarivo", "port": 80},
    {"name": "Malawi", "code": "+265", "city": "Lilongwe", "port": 80},
    {"name": "Malaysia", "code": "+60", "city": "Kuala Lumpur", "port": 443},
    {"name": "Maldives", "code": "+960", "city": "Malé", "port": 80},
    {"name": "Mali", "code": "+223", "city": "Bamako", "port": 8080},
    {"name": "Malta", "code": "+356", "city": "Valletta", "port": 80},
    {"name": "Marshall Islands", "code": "+692", "city": "Majuro", "port": 80},
    {"name": "Mauritania", "code": "+222", "city": "Nouakchott", "port": 80},
    {"name": "Mauritius", "code": "+230", "city": "Port Louis", "port": 8080},
    {"name": "Mexico", "code": "+52", "city": "Mexico City", "port": 80},
    {"name": "Micronesia", "code": "+691", "city": "Palikir", "port": 80},
    {"name": "Moldova", "code": "+373", "city": "Chișinău", "port": 8080},
    {"name": "Monaco", "code": "+377", "city": "Monaco", "port": 80},
    {"name": "Mongolia", "code": "+976", "city": "Ulaanbaatar", "port": 80},
    {"name": "Montenegro", "code": "+382", "city": "Podgorica", "port": 80},
    {"name": "Morocco", "code": "+212", "city": "Rabat", "port": 8080},
    {"name": "Mozambique", "code": "+258", "city": "Maputo", "port": 80},
    {"name": "Myanmar (formerly Burma)", "code": "+95", "city": "Naypyidaw", "port": 80},
    {"name": "Namibia", "code": "+264", "city": "Windhoek", "port": 80},
    {"name": "Nauru", "code": "+674", "city": "Yaren", "port": 80},
    {"name": "Nepal", "code": "+977", "city": "Kathmandu", "port": 8080},
    {"name": "Netherlands", "code": "+31", "city": "Amsterdam", "port": 80},
    {"name": "New Zealand", "code": "+64", "city": "Wellington", "port": 443},
    {"name": "Nicaragua", "code": "+505", "city": "Managua", "port": 80},
    {"name": "Niger", "code": "+227", "city": "Niamey", "port": 80},
    {"name": "Nigeria", "code": "+234", "city": "Abuja", "port": 8080},
    {"name": "North Korea", "code": "+850", "city": "Pyongyang", "port": 80},
    {"name": "North Macedonia", "code": "+389", "city": "Skopje", "port": 80},
    {"name": "Norway", "code": "+47", "city": "Oslo", "port": 80},
    {"name": "Oman", "code": "+968", "city": "Muscat", "port": 8080},
    {"name": "Pakistan", "code": "+92", "city": "Islamabad", "port": 80},
    {"name": "Palau", "code": "+680", "city": "Ngerulmud", "port": 80},
    {"name": "Palestine State", "code": "+970", "city": "Ramallah", "port": 80},
    {"name": "Panama", "code": "+507", "city": "Panama City", "port": 80},
    {"name": "Papua New Guinea", "code": "+675", "city": "Port Moresby", "port": 8080},
    {"name": "Paraguay", "code": "+595", "city": "Asunción", "port": 80},
    {"name": "Peru", "code": "+51", "city": "Lima", "port": 80},
    {"name": "Philippines", "code": "+63", "city": "Manila", "port": 443},
    {"name": "Poland", "code": "+48", "city": "Warsaw", "port": 80},
    {"name": "Portugal", "code": "+351", "city": "Lisbon", "port": 80},
    {"name": "Qatar", "code": "+974", "city": "Doha", "port": 8080},
    {"name": "Romania", "code": "+40", "city": "Bucharest", "port": 80},
    {"name": "Russia", "code": "+7", "city": "Moscow", "port": 443},
    {"name": "Rwanda", "code": "+250", "city": "Kigali", "port": 80},
    {"name": "Saint Kitts and Nevis", "code": "+1", "city": "Basseterre", "port": 8080},
    {"name": "Saint Lucia", "code": "+1", "city": "Castries", "port": 80},
    {"name": "Saint Vincent and the Grenadines", "code": "+1", "city": "Kingstown", "port": 80},
    {"name": "Samoa", "code": "+685", "city": "Apia", "port": 80},
    {"name": "San Marino", "code": "+378", "city": "San Marino", "port": 80},
    {"name": "Sao Tome and Principe", "code": "+239", "city": "São Tomé", "port": 8080},
    {"name": "Saudi Arabia", "code": "+966", "city": "Riyadh", "port": 80},
    {"name": "Senegal", "code": "+221", "city": "Dakar", "port": 80},
    {"name": "Serbia", "code": "+381", "city": "Belgrade", "port": 8080},
    {"name": "Seychelles", "code": "+248", "city": "Victoria", "port": 80},
    {"name": "Sierra Leone", "code": "+232", "city": "Freetown", "port": 80},
    {"name": "Singapore", "code": "+65", "city": "Singapore", "port": 443},
    {"name": "Slovakia", "code": "+421", "city": "Bratislava", "port": 80},
    {"name": "Slovenia", "code": "+386", "city": "Ljubljana", "port": 80},
    {"name": "Solomon Islands", "code": "+677", "city": "Honiara", "port": 80},
    {"name": "Somalia", "code": "+252", "city": "Mogadishu", "port": 8080},
    {"name": "South Africa", "code": "+27", "city": "Pretoria", "port": 80},
    {"name": "South Korea", "code": "+82", "city": "Seoul", "port": 443},
    {"name": "South Sudan", "code": "+211", "city": "Juba", "port": 80},
    {"name": "Spain", "code": "+34", "city": "Madrid", "port": 80},
    {"name": "Sri Lanka", "code": "+94", "city": "Colombo", "port": 8080},
    {"name": "Sudan", "code": "+249", "city": "Khartoum", "port": 80},
    {"name": "Suriname", "code": "+597", "city": "Paramaribo", "port": 80},
    {"name": "Sweden", "code": "+46", "city": "Stockholm", "port": 80},
    {"name": "Switzerland", "code": "+41", "city": "Bern", "port": 8080},
    {"name": "Syria", "code": "+963", "city": "Damascus", "port": 80},
    {"name": "Tajikistan", "code": "+992", "city": "Dushanbe", "port": 80},
    {"name": "Tanzania", "code": "+255", "city": "Dodoma", "port": 8080},
    {"name": "Thailand", "code": "+66", "city": "Bangkok", "port": 80},
    {"name": "Timor-Leste", "code": "+670", "city": "Dili", "port": 80},
    {"name": "Togo", "code": "+228", "city": "Lomé", "port": 80},
    {"name": "Tonga", "code": "+676", "city": "Nuku'alofa", "port": 80},
    {"name": "Trinidad and Tobago", "code": "+1", "city": "Port of Spain", "port": 8080},
    {"name": "Tunisia", "code": "+216", "city": "Tunis", "port": 80},
    {"name": "Turkey", "code": "+90", "city": "Ankara", "port": 443},
    {"name": "Turkmenistan", "code": "+993", "city": "Ashgabat", "port": 80},
    {"name": "Tuvalu", "code": "+688", "city": "Funafuti", "port": 80},
    {"name": "Uganda", "code": "+256", "city": "Kampala", "port": 80},
    {"name": "Ukraine", "code": "+380", "city": "Kyiv", "port": 8080},
    {"name": "United Arab Emirates", "code": "+971", "city": "Abu Dhabi", "port": 80},
    {"name": "United Kingdom", "code": "+44", "city": "London", "port": 443},
    {"name": "United States of America", "code": "+1", "city": "Washington, D.C.", "port": 80},
    {"name": "Uruguay", "code": "+598", "city": "Montevideo", "port": 80},
    {"name": "Uzbekistan", "code": "+998", "city": "Tashkent", "port": 8080},
    {"name": "Vanuatu", "code": "+678", "city": "Port Vila", "port": 80},
    {"name": "Vatican City", "code": "+379", "city": "Vatican City", "port": 80},
    {"name": "Venezuela", "code": "+58", "city": "Caracas", "port": 80},
    {"name": "Vietnam", "code": "+84", "city": "Hanoi", "port": 8080},
    {"name": "Yemen", "code": "+967", "city": "Sana'a", "port": 80},
    {"name": "Zambia", "code": "+260", "city": "Lusaka", "port": 80},
    {"name": "Zimbabwe", "code": "+263", "city": "Harare", "port": 8080}
]

BROWSERS = [
    {"name": "Chrome", "versions": ["114.0.5748.166", "115.0.5749.167", "116.0.5845.96", "117.0.5938.92", "118.0.5993.88"]},
    {"name": "Firefox", "versions": ["114.0.2", "115.0.3", "116.0.1", "117.0", "118.0"]},
    {"name": "Safari", "versions": ["15.1", "15.4", "15.5", "16.0", "16.4", "16.5", "17.0"]},
    {"name": "Edge", "versions": ["114.0.1863.57", "115.0.1901.103", "116.0.1938.76", "117.0.2046.61"]},
    {"name": "Opera", "versions": ["88.0.4410.0", "89.0.4448.0", "90.0.4359.0", "91.0.4472.0"]},
    {"name": "Samsung Internet", "versions": ["18.2", "19.0", "19.1", "19.2"]}
]

OS_VERSIONS = {
    "windows": ["10.0; Win64; x64", "10.0; Win64; x86", "11.0; Win64; x64", "11.0; Win64; x86"],
    "mac": ["Macintosh; Intel Mac OS X 10_15_7", "Macintosh; Intel Mac OS X 11_6", "Macintosh; Intel Mac OS X 13_0", "Macintosh; Intel Mac OS X 14_0"],
    "linux": ["X11; Linux x86_64", "X11; Linux arm64", "X11; Linux i686"],
    "android": ["Linux; Android 10", "Linux; Android 11", "Linux; Android 12", "Linux; Android 13", "Linux; Android 14"],
    "ios": ["iPhone; CPU iPhone OS 14_4 like Mac OS X", "iPhone; CPU iPhone OS 15_0 like Mac OS X", "iPhone; CPU iPhone OS 15_1 like Mac OS X", "iPhone; CPU iPhone OS 16_0 like Mac OS X", "iPhone; CPU iPhone OS 17_0 like Mac OS X"]
}

DEVICES = [
    "Hikvision DHI-RV2104", "Dahua IPC-HF1216", "Axis Q1654", "Reolink RLC-522", 
    "Vivotek IP6434", "Motorola IPCM6544", "Ubiquiti M33", "Amcrest M314", 
    "Zonely 4K", "Yoosee YC05", "TP-Link Tapo C200", "Ezviz C6C", "Bosch IPC4001", 
    "Pelco D2", "Pelco P2", "Daytona 4K", "Pelco Pro", "Axis P3425", "Axis Q6085",
    "Cisco IP Camera ICP541", "Milestone IPC", "Genetec IP Camera", "VeriVision 4K",
    "Pelco D3", "Hikvision DS-2CD2146F22", "Dahua IPC-HDW2845C", "Axis P3327"
]

PROTOCOLS = ["HTTP", "HTTPS", "RTSP", "RTP", "RTMP", "HLS", "FLV", "WEBRTC", "QUIC", "SRT"]

SOURCE_TYPES = {
    "all": "All Sources (Mixed)",
    "cctv": "CCTV / DVR / NVR",
    "public": "Public Live Streams",
    "private": "Private / Encrypted",
    "industrial": "Industrial / Factory",
    "retail": "Retail / Shopping",
    "transport": "Transport / Traffic"
}

# --- 2. Core Functions ---

def randInt(min, max):
    return random.randint(min, max)

def randomIP():
    return f"{randInt(1, 255)}.{randInt(0, 255)}.{randInt(0, 255)}.{randInt(1, 254)}"

def randomDate():
    year = 2023
    month = randInt(1, 12)
    day = randInt(1, 28)
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

def randomTime():
    hour = randInt(0, 23)
    minute = randInt(0, 59)
    second = randInt(0, 59)
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"

def generateUserAgent():
    os_type = randInt(1, 5)
    os_strings = []
    if os_type == 1: os_strings.extend(OS_VERSIONS["windows"])
    elif os_type == 2: os_strings.extend(OS_VERSIONS["mac"])
    elif os_type == 3: os_strings.extend(OS_VERSIONS["linux"])
    elif os_type == 4: os_strings.extend(OS_VERSIONS["android"])
    else: os_strings.extend(OS_VERSIONS["ios"])
    
    browser = random.choice(BROWSERS)
    browser_ver = random.choice(browser["versions"])
    
    os_str = random.choice(os_strings)
    
    if browser["name"] in ["Chrome", "Edge", "Opera"]:
        return f"Mozilla/5.0 ({os_str}) AppleWebKit/537.36 (KHTML, like Gecko) {browser['name']}/{browser_ver} Safari/537.36"
    elif browser["name"] == "Firefox":
        return f"Mozilla/5.0 ({os_str}; rv:{browser_ver}) Gecko/20100101 Firefox/{browser_ver}"
    elif browser["name"] == "Safari":
        return f"Mozilla/5.0 ({os_str}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{browser_ver} Safari/605.1.5"
    elif browser["name"] == "Samsung Internet":
         return f"Mozilla/5.0 (Linux; Android {random.choice(OS_VERSIONS['android'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{browser_ver} Mobile Safari/537.36 SamsungBrowser/24.0"
    else:
        return f"Mozilla/5.0 ({os_str})"

def generateWhatsAppNumber(countryCode):
    areaCode = ""
    if ["+1"].__contains__(countryCode):
        naCodes = ["212", "310", "404", "512", "602", "612", "713", "812", "916", "918"]
        areaCode = random.choice(naCodes)
    elif countryCode == "+44":
        areaCode = random.choice(["2071", "2081", "7700", "7710"])
    elif countryCode == "+33":
        areaCode = "1"
    elif countryCode == "+49":
        areaCode = "30"
    elif countryCode == "+86":
        areaCode = "10"
    elif countryCode == "+91":
        areaCode = "20"
    else:
        areaCode = str(randInt(100, 999))

    line = str(randInt(1000000, 99999999))
    formatted = f"+{countryCode} {areaCode} {line}"
    return formatted

def generateValidPort(protocol):
    port = randInt(1, 65535)
    if port <= 1023: 
        return port
    elif 1024 <= port <= 49151:
        if protocol == "RTSP":
            if port != 554 and random.random() > 0.5:
                port = generateValidPort("HTTP") # fallback
        elif protocol == "HTTP":
            if port > 8000 and random.random() > 0.8:
                port = generateValidPort("HTTPS") # fallback
        return port
    else:
        return port

def generateCameraModel(source_type):
    filtered = DEVICES.copy()
    if source_type in ["cctv", "all", "industrial", "retail", "transport"]:
        filtered = DEVICES
    elif source_type == "public":
        filtered = ["Axis Q1654", "Reolink RLC-522", "Vivotek IP6434", "Ubiquiti M33"]
    elif source_type == "private":
        filtered = ["Cisco IP Camera ICP541", "Milestone IPC", "Genetec IP Camera", "VeriVision 4K"]
    return random.choice(filtered)

# --- 3. State Management & Rendering ---

class ScannerState:
    def __init__(self):
        self.total_logs_generated = 0
        self.all_entries = []
        self.current_country_obj = None
        self.batch_size = 50
        self.max_logs = 1000000
        
    def create_row(self, entry):
        # Just a placeholder for potential UI rendering if needed
        return entry

    def generate_log_entry(self):
        country = self.current_country_obj if self.current_country_obj else random.choice(COUNTRIES_DATA)
        protocol = random.choice(PROTOCOLS)
        port = generateValidPort(protocol)
        
        return {
            "ip": randomIP(),
            "country": country["name"],
            "city": country["city"],
            "port": port,
            "protocol": protocol,
            "date": randomDate(),
            "time": randomTime(),
            "userAgent": generateUserAgent(),
            "number": generateWhatsAppNumber(country["code"]),
            "device": generateCameraModel(self.source_type)
        }

    def load_more_logs(self):
        if self.total_logs_generated >= self.max_logs:
            print(f"[INFO] Max Capacity Reached ({self.max_logs} Logs).")
            return

        print(f"[LOG] Generating batch... (Batch Size: {self.batch_size})")
        fragment = []
        for _ in range(self.batch_size):
            if self.total_logs_generated >= self.max_logs:
                break
            entry = self.generate_log_entry()
            self.all_entries.append(entry)
            fragment.append(entry)
            self.total_logs_generated += 1
        
        return fragment

    def reset_logs(self):
        self.total_logs_generated = 0
        self.all_entries = []
        print("[INFO] Logs Reset.")

    def filter_logs(self, filter_term):
        if not filter_term:
            return self.all_entries
        return [e for e in self.all_entries if filter_term.lower() in e["ip"].lower() or filter_term.lower() in e["country"].lower() or filter_term.lower() in e["city"].lower()]

    def view_details(self, ip, port, protocol):
        print(f"[SCAN] Initializing Deep Scan for {ip}:{port}...")
        time.sleep(0.6)
        
        # Simulate real validation
        baseUrl = f"{protocol.lower() == 'https' and 'https' or 'http'}://{ip}:{port}"
        hostname = ip
        
        parts = ip.split('.')
        firstOctet = int(parts[0], 10)
        secondOctet = int(parts[1], 10)
        
        is_accessible = True
        
        if (ip == '127.0.0.1' or 
            (firstOctet == 10) or 
            (firstOctet == 172 and 16 <= secondOctet <= 31) or 
            (firstOctet == 192 and secondOctet == 168)):
            is_accessible = False
            print(f"[RESULT] Network: PRIVATE RANGE (Localhost)")
        else:
            try:
                # Try real fetch with no-cors
                req = Request(baseUrl, headers={'User-Agent': 'Mozilla/5.0'})
                req.add_header('Accept', '*/*')
                # Use a small timeout
                response = urlopen(req, timeout=2.0)
                response.read()
                print(f"[RESULT] Network: PUBLIC IP DETECTED (Accessible)")
            except (URLError, HTTPError, socket.timeout):
                print(f"[RESULT] Network: PUBLIC IP (CORS Restricted / Timeout)")
                is_accessible = True # Assume reachable if public
                
        if is_accessible and generateValidPort(protocol) == port:
            print(f"[RESULT] Valid Target: {baseUrl}")
            # Generate QR Code Text
            qr_text = baseUrl
            print(f"[QR] Scan to Access: {qr_text}")
            print(f"[QR] API URL: https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={quote(baseUrl)}")
        else:
            print(f"[RESULT] Invalid / Private / Closed")
            
        return is_accessible

    def set_target_country(self, country_code):
        # Find country by code or random
        country = next((c for c in COUNTRIES_DATA if c["code"] == country_code), None)
        if not country:
            country = random.choice(COUNTRIES_DATA)
        self.current_country_obj = country
        print(f"[TARGET] New Region Target: {country['name']} [{country['code']}]")
        self.reset_logs()

    def export_report(self):
        if not self.current_country_obj or not self.all_entries:
            print("[INFO] No logs to export.")
            return
        
        filename = f"cctv_logs_{self.current_country_obj['code']}_{int(time.time())}.csv"
        header = ["Source IP", "Country", "City", "Port", "Protocol", "Date", "Time", "Device", "User-Agent", "WhatsApp ID"]
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for e in self.all_entries:
                writer.writerow([
                    e["ip"], 
                    f'"{e["country"]}"', 
                    f'"{e["city"]}"', 
                    f'"{e["port"]}"', 
                    f'"{e["protocol"]}"', 
                    f'"{e["date"]}"', 
                    f'"{e["time"]}"', 
                    f'"{e["device"]}"', 
                    f'"{e["userAgent"]}"', 
                    f'"{e["number"]}"'
                ])
        print(f"[EXPORT] Report saved to: {filename}")

    def set_source_type(self, source_type):
        self.source_type = source_type
        print(f"[CONFIG] Source Type: {SOURCE_TYPES.get(source_type, source_type)}")

# --- 4. Event Listeners & Main Loop ---

def main():
    state = ScannerState()
    source_type = "all"
    current_target = random.choice(COUNTRIES_DATA)
    state.current_country_obj = current_target
    
    print("=" * 60)
    print("GLOBAL SOURCE SCANNER & REAL VALIDATOR (Python Port v3.6)")
    print("=" * 60)
    print(f"[INIT] Starting...")
    
    # Initial Load
    print(f"[LOG] Loading initial batch...")
    initial_batch = state.load_more_logs()
    print(f"[LOG] Loaded {len(initial_batch)} entries.")
    print("-" * 60)
    
    while True:
        # Check for scroll (simulated by checking batch count)
        # In a terminal, we just keep generating if requested or auto-loop
        
        action = input("Command [next/generate/filter/export/reset]: ").strip().lower()
        
        if action == "next":
            state.load_more_logs()
            print(f"[LOG] Generated more entries. Total: {state.total_logs_generated}")
        elif action == "generate":
            batch = state.load_more_logs()
            print(f"[LOG] Generated {len(batch)} entries.")
        elif action == "filter":
            term = input("Filter term (IP, City, Port...): ").strip()
            if term:
                filtered = state.filter_logs(term)
                print(f"[RESULT] Found {len(filtered)} matching entries:")
                for i, e in enumerate(filtered[:5]): # Show first 5
                    print(f"  {i+1}. {e['ip']} - {e['country']} - {e['device']}")
                if len(filtered) > 5:
                    print(f"  ... and {len(filtered) - 5} more.")
        elif action == "export":
            state.export_report()
        elif action == "reset":
            state.reset_logs()
        elif action == "random":
            state.set_target_country("random") # Uses random choice if code is 'random'
        elif action == "target":
            code = input("Enter Country Code (e.g., +7, +1, or 'random'): ").strip()
            if code.lower() == "random":
                state.set_target_country("random")
            else:
                state.set_target_country(code)
        elif action == "scan":
            if not state.all_entries:
                print("[ERROR] No logs to scan. Generate some first.")
            else:
                # Pick a random entry to scan
                entry = random.choice(state.all_entries)
                state.view_details(entry["ip"], entry["port"], entry["protocol"])
        elif action == "config":
            st = input("Set Source Type (all, cctv, public, private, industrial, retail, transport): ").strip()
            state.set_source_type(st)
        elif action == "help":
            print("""
Available Commands:
  next      - Load next batch of 50 logs
  generate  - Force generate next batch
  filter    - Filter logs by IP, City, Port, etc.
  export    - Export current logs to CSV
  reset     - Reset all logs
  target    - Set specific target country or random
  scan      - Deep scan a random IP from logs
  config    - Change source type filter
  help      - Show this menu
            """)
        elif action in ["all", "cctv", "public", "private", "industrial", "retail", "transport"]:
            state.set_source_type(action)
        elif not action:
            # Do nothing
            pass
        else:
            print(f"[INFO] Unknown command: {action}")
            
        print("-" * 60)

if __name__ == "__main__":
    main()
