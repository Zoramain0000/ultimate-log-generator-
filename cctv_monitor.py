import random
import time
import csv
from datetime import datetime, timedelta

# --- 1. Configuration & Databases ---

countries_data = [
    {"name": "Afghanistan", "code": "+93", "city": "Kabul", "port": 80, "type": "cctv"},
    {"name": "Albania", "code": "+355", "city": "Tirana", "port": 8080, "type": "cctv"},
    {"name": "Algeria", "code": "+213", "city": "Algiers", "port": 443, "type": "cctv"},
    {"name": "Andorra", "code": "+376", "city": "Andorra la Vella", "port": 80, "type": "cctv"},
    {"name": "Angola", "code": "+244", "city": "Luanda", "port": 8000, "type": "cctv"},
    {"name": "Argentina", "code": "+54", "city": "Buenos Aires", "port": 80, "type": "cctv"},
    {"name": "Armenia", "code": "+374", "city": "Yerevan", "port": 8080, "type": "cctv"},
    {"name": "Australia", "code": "+61", "city": "Sydney", "port": 443, "type": "cctv"},
    {"name": "Austria", "code": "+43", "city": "Vienna", "port": 80, "type": "cctv"},
    {"name": "Azerbaijan", "code": "+994", "city": "Baku", "port": 8080, "type": "cctv"},
    {"name": "Bahamas", "code": "+1", "city": "Nassau", "port": 443, "type": "cctv"},
    {"name": "Bahrain", "code": "+973", "city": "Manama", "port": 80, "type": "cctv"},
    {"name": "Bangladesh", "code": "+880", "city": "Dhaka", "port": 8080, "type": "cctv"},
    {"name": "Barbados", "code": "+1", "city": "Bridgetown", "port": 80, "type": "cctv"},
    {"name": "Belarus", "code": "+375", "city": "Minsk", "port": 80, "type": "cctv"},
    {"name": "Belgium", "code": "+32", "city": "Brussels", "port": 443, "type": "cctv"},
    {"name": "Belize", "code": "+501", "city": "Belmopan", "port": 8080, "type": "cctv"},
    {"name": "Benin", "code": "+229", "city": "Porto-Novo", "port": 80, "type": "cctv"},
    {"name": "Bhutan", "code": "+975", "city": "Thimphu", "port": 80, "type": "cctv"},
    {"name": "Bolivia", "code": "+591", "city": "Sucre", "port": 8080, "type": "cctv"},
    {"name": "Bosnia and Herzegovina", "code": "+387", "city": "Sarajevo", "port": 80, "type": "cctv"},
    {"name": "Botswana", "code": "+267", "city": "Gaborone", "port": 80, "type": "cctv"},
    {"name": "Brazil", "code": "+55", "city": "São Paulo", "port": 443, "type": "cctv"},
    {"name": "Brunei", "code": "+673", "city": "Bandar Seri Begawan", "port": 8080, "type": "cctv"},
    {"name": "Bulgaria", "code": "+359", "city": "Sofia", "port": 80, "type": "cctv"},
    {"name": "Burkina Faso", "code": "+226", "city": "Ouagadougou", "port": 80, "type": "cctv"},
    {"name": "Burundi", "code": "+257", "city": "Gitega", "port": 80, "type": "cctv"},
    {"name": "Cabo Verde", "code": "+238", "city": "Praia", "port": 8080, "type": "cctv"},
    {"name": "Cambodia", "code": "+855", "city": "Phnom Penh", "port": 80, "type": "cctv"},
    {"name": "Cameroon", "code": "+237", "city": "Yaoundé", "port": 8080, "type": "cctv"},
    {"name": "Canada", "code": "+1", "city": "Toronto", "port": 443, "type": "cctv"},
    {"name": "Central African Republic", "code": "+236", "city": "Bangui", "port": 80, "type": "cctv"},
    {"name": "Chad", "code": "+235", "city": "N'Djamena", "port": 80, "type": "cctv"},
    {"name": "Chile", "code": "+56", "city": "Santiago", "port": 8080, "type": "cctv"},
    {"name": "China", "code": "+86", "city": "Beijing", "port": 80, "type": "cctv"},
    {"name": "Colombia", "code": "+57", "city": "Bogotá", "port": 443, "type": "cctv"},
    {"name": "Comoros", "code": "+269", "city": "Moroni", "port": 80, "type": "cctv"},
    {"name": "Congo", "code": "+242", "city": "Brazzaville", "port": 8080, "type": "cctv"},
    {"name": "Costa Rica", "code": "+506", "city": "San José", "port": 80, "type": "cctv"},
    {"name": "Croatia", "code": "+385", "city": "Zagreb", "port": 80, "type": "cctv"},
    {"name": "Cuba", "code": "+53", "city": "Havana", "port": 8080, "type": "cctv"},
    {"name": "Cyprus", "code": "+357", "city": "Nicosia", "port": 80, "type": "cctv"},
    {"name": "Czech Republic", "code": "+420", "city": "Prague", "port": 443, "type": "cctv"},
    {"name": "Democratic Republic of the Congo", "code": "+243", "city": "Kinshasa", "port": 80, "type": "cctv"},
    {"name": "Denmark", "code": "+45", "city": "Copenhagen", "port": 80, "type": "cctv"},
    {"name": "Djibouti", "code": "+253", "city": "Djibouti", "port": 8080, "type": "cctv"},
    {"name": "Dominica", "code": "+1", "city": "Roseau", "port": 80, "type": "cctv"},
    {"name": "Dominican Republic", "code": "+1", "city": "Santo Domingo", "port": 443, "type": "cctv"},
    {"name": "Ecuador", "code": "+593", "city": "Quito", "port": 80, "type": "cctv"},
    {"name": "Egypt", "code": "+20", "city": "Cairo", "port": 8080, "type": "cctv"},
    {"name": "El Salvador", "code": "+503", "city": "San Salvador", "port": 80, "type": "cctv"},
    {"name": "Equatorial Guinea", "code": "+240", "city": "Malabo", "port": 80, "type": "cctv"},
    {"name": "Eritrea", "code": "+291", "city": "Asmara", "port": 80, "type": "cctv"},
    {"name": "Estonia", "code": "+372", "city": "Tallinn", "port": 8080, "type": "cctv"},
    {"name": "Eswatini", "code": "+268", "city": "Mbabane", "port": 80, "type": "cctv"},
    {"name": "Ethiopia", "code": "+251", "city": "Addis Ababa", "port": 80, "type": "cctv"},
    {"name": "Fiji", "code": "+679", "city": "Suva", "port": 8080, "type": "cctv"},
    {"name": "Finland", "code": "+358", "city": "Helsinki", "port": 80, "type": "cctv"},
    {"name": "France", "code": "+33", "city": "Paris", "port": 443, "type": "cctv"},
    {"name": "Gabon", "code": "+241", "city": "Libreville", "port": 80, "type": "cctv"},
    {"name": "Gambia", "code": "+220", "city": "Banjul", "port": 80, "type": "cctv"},
    {"name": "Georgia", "code": "+995", "city": "Tbilisi", "port": 8080, "type": "cctv"},
    {"name": "Germany", "code": "+49", "city": "Berlin", "port": 80, "type": "cctv"},
    {"name": "Ghana", "code": "+233", "city": "Accra", "port": 80, "type": "cctv"},
    {"name": "Greece", "code": "+30", "city": "Athens", "port": 8080, "type": "cctv"},
    {"name": "Grenada", "code": "+1", "city": "St. George's", "port": 80, "type": "cctv"},
    {"name": "Guatemala", "code": "+502", "city": "Guatemala City", "port": 80, "type": "cctv"},
    {"name": "Guinea", "code": "+224", "city": "Conakry", "port": 8080, "type": "cctv"},
    {"name": "Guinea-Bissau", "code": "+245", "city": "Bissau", "port": 80, "type": "cctv"},
    {"name": "Guyana", "code": "+592", "city": "Georgetown", "port": 80, "type": "cctv"},
    {"name": "Haiti", "code": "+509", "city": "Port-au-Prince", "port": 8080, "type": "cctv"},
    {"name": "Honduras", "code": "+504", "city": "Tegucigalpa", "port": 80, "type": "cctv"},
    {"name": "Hungary", "code": "+36", "city": "Budapest", "port": 80, "type": "cctv"},
    {"name": "Iceland", "code": "+354", "city": "Reykjavik", "port": 8080, "type": "cctv"},
    {"name": "India", "code": "+91", "city": "Mumbai", "port": 443, "type": "cctv"},
    {"name": "Indonesia", "code": "+62", "city": "Jakarta", "port": 80, "type": "cctv"},
    {"name": "Iran", "code": "+98", "city": "Tehran", "port": 8080, "type": "cctv"},
    {"name": "Iraq", "code": "+964", "city": "Baghdad", "port": 80, "type": "cctv"},
    {"name": "Ireland", "code": "+353", "city": "Dublin", "port": 80, "type": "cctv"},
    {"name": "Israel", "code": "+972", "city": "Jerusalem", "port": 443, "type": "cctv"},
    {"name": "Italy", "code": "+39", "city": "Rome", "port": 80, "type": "cctv"},
    {"name": "Jamaica", "code": "+1", "city": "Kingston", "port": 8080, "type": "cctv"},
    {"name": "Japan", "code": "+81", "city": "Tokyo", "port": 80, "type": "cctv"},
    {"name": "Jordan", "code": "+962", "city": "Amman", "port": 80, "type": "cctv"},
    {"name": "Kazakhstan", "code": "+7", "city": "Almaty", "port": 8080, "type": "cctv"},
    {"name": "Kenya", "code": "+254", "city": "Nairobi", "port": 80, "type": "cctv"},
    {"name": "Kiribati", "code": "+686", "city": "Tarawa", "port": 80, "type": "cctv"},
    {"name": "Kuwait", "code": "+965", "city": "Kuwait City", "port": 8080, "type": "cctv"},
    {"name": "Kyrgyzstan", "code": "+996", "city": "Bishkek", "port": 80, "type": "cctv"},
    {"name": "Laos", "code": "+856", "city": "Vientiane", "port": 80, "type": "cctv"},
    {"name": "Latvia", "code": "+371", "city": "Riga", "port": 8080, "type": "cctv"},
    {"name": "Lebanon", "code": "+961", "city": "Beirut", "port": 80, "type": "cctv"},
    {"name": "Lesotho", "code": "+266", "city": "Maseru", "port": 80, "type": "cctv"},
    {"name": "Liberia", "code": "+231", "city": "Monrovia", "port": 80, "type": "cctv"},
    {"name": "Libya", "code": "+218", "city": "Tripoli", "port": 8080, "type": "cctv"},
    {"name": "Liechtenstein", "code": "+423", "city": "Vaduz", "port": 80, "type": "cctv"},
    {"name": "Lithuania", "code": "+370", "city": "Vilnius", "port": 80, "type": "cctv"},
    {"name": "Luxembourg", "code": "+352", "city": "Luxembourg City", "port": 8080, "type": "cctv"},
    {"name": "Madagascar", "code": "+261", "city": "Antananarivo", "port": 80, "type": "cctv"},
    {"name": "Malawi", "code": "+265", "city": "Lilongwe", "port": 80, "type": "cctv"},
    {"name": "Malaysia", "code": "+60", "city": "Kuala Lumpur", "port": 443, "type": "cctv"},
    {"name": "Maldives", "code": "+960", "city": "Malé", "port": 80, "type": "cctv"},
    {"name": "Mali", "code": "+223", "city": "Bamako", "port": 8080, "type": "cctv"},
    {"name": "Malta", "code": "+356", "city": "Valletta", "port": 80, "type": "cctv"},
    {"name": "Marshall Islands", "code": "+692", "city": "Majuro", "port": 80, "type": "cctv"},
    {"name": "Mauritania", "code": "+222", "city": "Nouakchott", "port": 80, "type": "cctv"},
    {"name": "Mauritius", "code": "+230", "city": "Port Louis", "port": 8080, "type": "cctv"},
    {"name": "Mexico", "code": "+52", "city": "Mexico City", "port": 80, "type": "cctv"},
    {"name": "Micronesia", "code": "+691", "city": "Palikir", "port": 80, "type": "cctv"},
    {"name": "Moldova", "code": "+373", "city": "Chișinău", "port": 8080, "type": "cctv"},
    {"name": "Monaco", "code": "+377", "city": "Monaco", "port": 80, "type": "cctv"},
    {"name": "Mongolia", "code": "+976", "city": "Ulaanbaatar", "port": 80, "type": "cctv"},
    {"name": "Montenegro", "code": "+382", "city": "Podgorica", "port": 80, "type": "cctv"},
    {"name": "Morocco", "code": "+212", "city": "Rabat", "port": 8080, "type": "cctv"},
    {"name": "Mozambique", "code": "+258", "city": "Maputo", "port": 80, "type": "cctv"},
    {"name": "Myanmar", "code": "+95", "city": "Naypyidaw", "port": 80, "type": "cctv"},
    {"name": "Namibia", "code": "+264", "city": "Windhoek", "port": 80, "type": "cctv"},
    {"name": "Nauru", "code": "+674", "city": "Yaren", "port": 80, "type": "cctv"},
    {"name": "Nepal", "code": "+977", "city": "Kathmandu", "port": 8080, "type": "cctv"},
    {"name": "Netherlands", "code": "+31", "city": "Amsterdam", "port": 80, "type": "cctv"},
    {"name": "New Zealand", "code": "+64", "city": "Wellington", "port": 443, "type": "cctv"},
    {"name": "Nicaragua", "code": "+505", "city": "Managua", "port": 80, "type": "cctv"},
    {"name": "Niger", "code": "+227", "city": "Niamey", "port": 80, "type": "cctv"},
    {"name": "Nigeria", "code": "+234", "city": "Lagos", "port": 8080, "type": "cctv"},
    {"name": "North Macedonia", "code": "+389", "city": "Skopje", "port": 80, "type": "cctv"},
    {"name": "Norway", "code": "+47", "city": "Oslo", "port": 80, "type": "cctv"},
    {"name": "Oman", "code": "+968", "city": "Muscat", "port": 8080, "type": "cctv"},
    {"name": "Pakistan", "code": "+92", "city": "Karachi", "port": 80, "type": "cctv"},
    {"name": "Palau", "code": "+680", "city": "Ngerulmud", "port": 80, "type": "cctv"},
    {"name": "Palestine", "code": "+970", "city": "Ramallah", "port": 80, "type": "cctv"},
    {"name": "Panama", "code": "+507", "city": "Panama City", "port": 80, "type": "cctv"},
    {"name": "Papua New Guinea", "code": "+675", "city": "Port Moresby", "port": 8080, "type": "cctv"},
    {"name": "Paraguay", "code": "+595", "city": "Asunción", "port": 80, "type": "cctv"},
    {"name": "Peru", "code": "+51", "city": "Lima", "port": 80, "type": "cctv"},
    {"name": "Philippines", "code": "+63", "city": "Manila", "port": 443, "type": "cctv"},
    {"name": "Poland", "code": "+48", "city": "Warsaw", "port": 80, "type": "cctv"},
    {"name": "Portugal", "code": "+351", "city": "Lisbon", "port": 80, "type": "cctv"},
    {"name": "Qatar", "code": "+974", "city": "Doha", "port": 8080, "type": "cctv"},
    {"name": "Romania", "code": "+40", "city": "Bucharest", "port": 80, "type": "cctv"},
    {"name": "Russia", "code": "+7", "city": "Moscow", "port": 443, "type": "cctv"},
    {"name": "Rwanda", "code": "+250", "city": "Kigali", "port": 80, "type": "cctv"},
    {"name": "Saint Kitts and Nevis", "code": "+1", "city": "Basseterre", "port": 8080, "type": "cctv"},
    {"name": "Saint Lucia", "code": "+1", "city": "Castries", "port": 80, "type": "cctv"},
    {"name": "Saint Vincent and the Grenadines", "code": "+1", "city": "Kingstown", "port": 80, "type": "cctv"},
    {"name": "Samoa", "code": "+685", "city": "Apia", "port": 80, "type": "cctv"},
    {"name": "San Marino", "code": "+378", "city": "San Marino", "port": 80, "type": "cctv"},
    {"name": "Sao Tome and Principe", "code": "+239", "city": "São Tomé", "port": 8080, "type": "cctv"},
    {"name": "Saudi Arabia", "code": "+966", "city": "Riyadh", "port": 80, "type": "cctv"},
    {"name": "Senegal", "code": "+221", "city": "Dakar", "port": 80, "type": "cctv"},
    {"name": "Serbia", "code": "+381", "city": "Belgrade", "port": 8080, "type": "cctv"},
    {"name": "Seychelles", "code": "+248", "city": "Victoria", "port": 80, "type": "cctv"},
    {"name": "Sierra Leone", "code": "+232", "city": "Freetown", "port": 80, "type": "cctv"},
    {"name": "Singapore", "code": "+65", "city": "Singapore", "port": 443, "type": "cctv"},
    {"name": "Slovakia", "code": "+421", "city": "Bratislava", "port": 80, "type": "cctv"},
    {"name": "Slovenia", "code": "+386", "city": "Ljubljana", "port": 80, "type": "cctv"},
    {"name": "Solomon Islands", "code": "+677", "city": "Honiara", "port": 80, "type": "cctv"},
    {"name": "Somalia", "code": "+252", "city": "Mogadishu", "port": 8080, "type": "cctv"},
    {"name": "South Africa", "code": "+27", "city": "Cape Town", "port": 80, "type": "cctv"},
    {"name": "South Korea", "code": "+82", "city": "Seoul", "port": 443, "type": "cctv"},
    {"name": "South Sudan", "code": "+211", "city": "Juba", "port": 80, "type": "cctv"},
    {"name": "Spain", "code": "+34", "city": "Madrid", "port": 80, "type": "cctv"},
    {"name": "Sri Lanka", "code": "+94", "city": "Colombo", "port": 8080, "type": "cctv"},
    {"name": "Sudan", "code": "+249", "city": "Khartoum", "port": 80, "type": "cctv"},
    {"name": "Suriname", "code": "+597", "city": "Paramaribo", "port": 80, "type": "cctv"},
    {"name": "Sweden", "code": "+46", "city": "Stockholm", "port": 80, "type": "cctv"},
    {"name": "Switzerland", "code": "+41", "city": "Bern", "port": 8080, "type": "cctv"},
    {"name": "Syria", "code": "+963", "city": "Damascus", "port": 80, "type": "cctv"},
    {"name": "Tajikistan", "code": "+992", "city": "Dushanbe", "port": 80, "type": "cctv"},
    {"name": "Tanzania", "code": "+255", "city": "Dodoma", "port": 8080, "type": "cctv"},
    {"name": "Thailand", "code": "+66", "city": "Bangkok", "port": 80, "type": "cctv"},
    {"name": "Timor-Leste", "code": "+670", "city": "Dili", "port": 80, "type": "cctv"},
    {"name": "Togo", "code": "+228", "city": "Lomé", "port": 80, "type": "cctv"},
    {"name": "Tonga", "code": "+676", "city": "Nuku'alofa", "port": 80, "type": "cctv"},
    {"name": "Trinidad and Tobago", "code": "+1", "city": "Port of Spain", "port": 8080, "type": "cctv"},
    {"name": "Tunisia", "code": "+216", "city": "Tunis", "port": 80, "type": "cctv"},
    {"name": "Turkey", "code": "+90", "city": "Ankara", "port": 443, "type": "cctv"},
    {"name": "Turkmenistan", "code": "+993", "city": "Ashgabat", "port": 80, "type": "cctv"},
    {"name": "Tuvalu", "code": "+688", "city": "Funafuti", "port": 80, "type": "cctv"},
    {"name": "Uganda", "code": "+256", "city": "Kampala", "port": 80, "type": "cctv"},
    {"name": "Ukraine", "code": "+380", "city": "Kyiv", "port": 8080, "type": "cctv"},
    {"name": "United Arab Emirates", "code": "+971", "city": "Abu Dhabi", "port": 80, "type": "cctv"},
    {"name": "United Kingdom", "code": "+44", "city": "London", "port": 443, "type": "cctv"},
    {"name": "United States", "code": "+1", "city": "New York", "port": 80, "type": "cctv"},
    {"name": "Uruguay", "code": "+598", "city": "Montevideo", "port": 80, "type": "cctv"},
    {"name": "Uzbekistan", "code": "+998", "city": "Tashkent", "port": 8080, "type": "cctv"},
    {"name": "Vanuatu", "code": "+678", "city": "Port Vila", "port": 80, "type": "cctv"},
    {"name": "Vatican City", "code": "+379", "city": "Vatican City", "port": 80, "type": "cctv"},
    {"name": "Venezuela", "code": "+58", "city": "Caracas", "port": 80, "type": "cctv"},
    {"name": "Vietnam", "code": "+84", "city": "Hanoi", "port": 8080, "type": "cctv"},
    {"name": "Yemen", "code": "+967", "city": "Sana'a", "port": 80, "type": "cctv"},
    {"name": "Zambia", "code": "+260", "city": "Lusaka", "port": 80, "type": "cctv"},
    {"name": "Zimbabwe", "code": "+263", "city": "Harare", "port": 8080, "type": "cctv"}
]

# Databases
browsers = [
    {"name": "Chrome", "versions": ["114.0.5748.166", "115.0.5749.167", "116.0.5845.96", "117.0.5938.92", "118.0.5993.88"]},
    {"name": "Firefox", "versions": ["114.0.2", "115.0.3", "116.0.1", "117.0", "118.0"]},
    {"name": "Safari", "versions": ["15.1", "15.4", "15.5", "16.0", "16.4", "16.5", "17.0"]},
    {"name": "Edge", "versions": ["114.0.1863.57", "115.0.1901.103", "116.0.1938.76", "117.0.2046.61"]},
    {"name": "Opera", "versions": ["88.0.4410.0", "89.0.4448.0", "90.0.4359.0", "91.0.4472.0"]},
    {"name": "Samsung Internet", "versions": ["18.2", "19.0", "19.1", "19.2"]}
]

os_versions = {
    "windows": ["10.0; Win64; x64", "10.0; Win64; x86", "11.0; Win64; x64", "11.0; Win64; x86"],
    "mac": ["Macintosh; Intel Mac OS X 10_15_7", "Macintosh; Intel Mac OS X 11_6", "Macintosh; Intel Mac OS X 13_0", "Macintosh; Intel Mac OS X 14_0"],
    "linux": ["X11; Linux x86_64", "X11; Linux arm64", "X11; Linux i686"],
    "android": ["Linux; Android 10", "Linux; Android 11", "Linux; Android 12", "Linux; Android 13", "Linux; Android 14"],
    "ios": ["iPhone; CPU iPhone OS 14_4 like Mac OS X", "iPhone; CPU iPhone OS 15_0 like Mac OS X", "iPhone; CPU iPhone OS 15_1 like Mac OS X", "iPhone; CPU iPhone OS 16_0 like Mac OS X", "iPhone; CPU iPhone OS 17_0 like Mac OS X"]
}

devices = [
    "Hikvision DHI-RV2104", "Dahua IPC-HF1216", "Axis Q1654", "Reolink RLC-522", 
    "Vivotek IP6434", "Motorola IPCM6544", "Ubiquiti M33", "Amcrest M314", 
    "Zonely 4K", "Yoosee YC05", "TP-Link Tapo C200", "Ezviz C6C", "Bosch IPC4001", 
    "Pelco D2", "Pelco P2", "Daytona 4K", "Pelco Pro", "Axis P3425", "Axis Q6085",
    "Cisco IP Camera ICP541", "Milestone IPC", "Genetec IP Camera", "VeriVision 4K",
    "Pelco D3", "Hikvision DS-2CD2146F22", "Dahua IPC-HDW2845C", "Axis P3327"
]

common_ports = [80, 443, 8080, 8443, 554, 8554, 1935, 5000, 5001, 6000, 3000, 10080, 9000, 4443, 9443]
protocols = ["HTTP", "HTTPS", "RTSP", "RTP", "RTMP", "HLS", "FLV", "WEBRTC", "QUIC", "SRT"]
source_types = ["CCTV", "DVR", "NVR", "IP Camera", "Analog", "HD Camera", "4K Camera", "PTZ Camera", "Dome Camera", "Bullet Camera", "Industrial", "Factory", "Office", "Retail", "Public", "Traffic", "Private", "Encrypted", "Live Stream", "Backup", "Proxy"]

# --- 2. Core Generators ---

def rand_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_ip():
    return f"{rand_int(1, 255)}.{rand_int(0, 255)}.{rand_int(0, 255)}.{rand_int(1, 254)}"

def random_date():
    year = 2022
    month = rand_int(1, 12)
    day = rand_int(1, 28)
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

def random_time():
    hour = rand_int(0, 23)
    minute = rand_int(0, 59)
    second = rand_int(0, 59)
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"

def generate_user_agent():
    os_type = rand_int(1, 5)
    os_strings = []
    if os_type == 1: os_strings = os_versions["windows"]
    elif os_type == 2: os_strings = os_versions["mac"]
    elif os_type == 3: os_strings = os_versions["linux"]
    elif os_type == 4: os_strings = os_versions["android"]
    elif os_type == 5: os_strings = os_versions["ios"]
    
    os_str = random.choice(os_strings)
    browser = random.choice(browsers)
    browser_ver = random.choice(browser["versions"])
    
    if browser["name"] == "Chrome" or browser["name"] == "Edge" or browser["name"] == "Opera":
        return f"Mozilla/5.0 ({os_str}) AppleWebKit/537.36 (KHTML, like Gecko) {browser['name']}/{browser_ver} Safari/537.36"
    elif browser["name"] == "Firefox":
        return f"Mozilla/5.0 ({os_str}; rv:{browser_ver}) Gecko/20100101 Firefox/{browser_ver}"
    elif browser["name"] == "Safari":
        return f"Mozilla/5.0 ({os_str}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{browser_ver} Safari/605.1.5"
    elif browser["name"] == "Samsung Internet":
        android_ver = random.choice(os_versions["android"])
        return f"Mozilla/5.0 (Linux; Android {android_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{browser_ver} Mobile Safari/537.36 SamsungBrowser/24.0"
    else:
        return f"Mozilla/5.0 ({os_str})"

def generate_whatsapp_number(country_code):
    area_codes = {}
    if country_code == "+1":
        area_codes = ["212", "310", "404", "512", "602", "612", "713", "812", "916", "918"]
    elif country_code == "+44":
        area_codes = ["2071", "2081", "7700", "7710"]
    elif country_code == "+33":
        area_codes = ["1"]
    elif country_code == "+49":
        area_codes = ["30"]
    elif country_code == "+86":
        area_codes = ["10"]
    elif country_code == "+91":
        area_codes = ["20"]
    else:
        area_codes = [rand_int(1, 999)]
    
    area_code = random.choice(area_codes)
    line = str(rand_int(1000000, 99999999))
    return f"+{country_code} {area_code} {line}"

def generate_camera_model(source_type):
    base_models = devices
    filtered = base_models
    
    if source_type in ["cctv", "all", "industrial", "retail", "transport"]:
        filtered = base_models
    elif source_type == "public":
        filtered = ["Axis Q1654", "Reolink RLC-522", "Vivotek IP6434", "Ubiquiti M33"]
    elif source_type == "private":
        filtered = ["Cisco IP Camera ICP541", "Milestone IPC", "Genetec IP Camera", "VeriVision 4K"]
    
    return random.choice(filtered)

# --- 3. Main Loop & Event Simulation ---

# Configuration
BATCH_SIZE = 50
MAX_LOGS = 1000000
total_logs_generated = 0
all_entries = []
current_country_obj = None

# Database Lookup Cache
country_map = {c["name"]: c for c in countries_data}

def create_row(entry):
    # Simulating HTML creation
    return f"""
    IP: <span class="highlight-red">{entry['ip']}</span>
    Country: {entry['country']}
    City: {entry['city']}
    Port: {entry['port']}
    Protocol: {entry['protocol']}
    Date: {entry['date']}
    Time: {entry['time']}
    Device: <span class="highlight-cyan">{entry['device']}</span>
    User-Agent: <span style="font-size:11px; color:#ccc;">{entry['user_agent']}</span>
    WhatsApp ID: <span class="highlight-green">{entry['number']}</span>
    """

def generate_log_entry_for_country():
    # Simulates: generateLogEntryForCountry
    country_obj = current_country_obj
    return {
        "ip": random_ip(),
        "country": country_obj["name"],
        "city": country_obj["city"],
        "port": country_obj["port"],
        "protocol": random.choice(protocols),
        "date": random_date(),
        "time": random_time(),
        "user_agent": generate_user_agent(),
        "number": generate_whatsapp_number(country_obj["code"]),
        "device": generate_camera_model(source_type=country_obj["type"])
    }

def load_more_logs():
    # Simulates: loadMoreLogs
    global total_logs_generated
    
    if total_logs_generated >= MAX_LOGS:
        print(f"\n[STATUS] Infinite Data Reached (Max {MAX_LOGS} rows). Refresh to continue.")
        return False
    
    print(f"\n[LOADING] Generating batch of {BATCH_SIZE}...")
    batch = []
    for _ in range(BATCH_SIZE):
        if total_logs_generated >= MAX_LOGS:
            break
        entry = generate_log_entry_for_country()
        all_entries.append(entry)
        batch.append(entry)
        total_logs_generated += 1
    
    # Display batch summary
    print(f"[RESULT] Added {len(batch)} rows. Total: {total_logs_generated}")
    return True

def filter_logs(search_term):
    if not search_term:
        print("[FILTER] Reset display to all rows.")
        return all_entries
    
    print(f"[FILTER] Searching for: '{search_term}'")
    filtered = [row for row in all_entries if search_term.lower() in row["ip"].lower() or search_term.lower() in row["country"].lower()]
    print(f"[RESULT] Found {len(filtered)} matching rows.")
    return filtered

def export_csv(filename=None):
    if not filename:
        filename = f"cctv_global_monitor_{current_country_obj['code']}.csv"
    
    if not all_entries:
        print("[EXPORT] No data to export. Generate logs first.")
        return
    
    header = ["Source IP", "Country", "City", "Port", "Protocol", "Date", "Time", "Device", "User-Agent", "WhatsApp ID"]
    rows = []
    for e in all_entries:
        rows.append([
            e['ip'],
            e['country'],
            e['city'],
            e['port'],
            e['protocol'],
            e['date'],
            e['time'],
            e['device'],
            e['user_agent'],
            e['number']
        ])
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    
    print(f"[EXPORT] Report saved to: {filename}")

# --- 4. Initialization & Interaction ---

def populate_countries():
    # Simulates: populateCountries
    print("[INIT] Populating Country List...")
    print("------------------------------------------------")
    for c in countries_data[:5]: # Print first 5 as example
        print(f"  - {c['name']} [{c['code']} - Port:{c['port']}]")
    print("------------------------------------------------")
    print(f"[INIT] Total Countries Loaded: {len(countries_data)}")

def main_menu():
    print("\n=== GLOBAL NETSEC MONITOR (Python v2.1) ===")
    print("1. Select Region")
    print("2. Select Source Type")
    print("3. Inject Data (Generate Logs)")
    print("4. Filter / Search")
    print("5. Export Report")
    print("6. Reset & Restart")
    print("0. Exit")
    
    choice = input("\nEnter Command [0-6]: ").strip()
    
    if choice == "1":
        print("\nAvailable Regions:")
        for i, c in enumerate(countries_data[:10]):
            print(f"{i+1}. {c['name']} ({c['code']})")
        print(f"   ... and {len(countries_data)-10} more.")
        try:
            idx = int(input("Select number: "))
            if 1 <= idx <= len(countries_data):
                global current_country_obj
                current_country_obj = countries_data[idx-1]
                print(f"[SELECT] Region Set: {current_country_obj['name']}")
            else:
                print("[ERROR] Invalid selection.")
        except ValueError:
            print("[ERROR] Please enter a number.")
    
    elif choice == "2":
        print("\nSource Types:")
        for i, t in enumerate(source_types[:8]):
            print(f"{i+1}. {t}")
        try:
            idx = int(input("Select number: "))
            if 1 <= idx <= len(source_types):
                print(f"[SELECT] Source Type: {source_types[idx-1]}")
            else:
                print("[ERROR] Invalid selection.")
        except ValueError:
            print("[ERROR] Please enter a number.")

    elif choice == "3":
        if not current_country_obj:
            print("[ERROR] Please select a region first (Command 1).")
            return
        load_more_logs()
        input("Press Enter to generate more...")
        load_more_logs()

    elif choice == "4":
        term = input("Enter Search Term (IP/Name/Num): ").strip()
        filter_logs(term)

    elif choice == "5":
        export_csv()

    elif choice == "6":
        print("[RESET] Clearing memory...")
        global total_logs_generated, all_entries
        total_logs_generated = 0
        all_entries = []
        print("[OK] Ready to restart.")

    elif choice == "0":
        print("[EXIT] Closing Session...")
        return

    else:
        print("[ERROR] Unknown command.")

    main_menu()

# --- Start ---

if __name__ == "__main__":
    populate_countries()
    # Initial Load Simulation
    print("[INIT] Starting Stream Simulation...")
    input("Press Enter to Start Injection...")
    
    if current_country_obj:
        load_more_logs()
    else:
        print("[WAIT] Select a region first, then press Enter.")
        input("Press Enter to continue...")
        load_more_logs()

    main_menu()
