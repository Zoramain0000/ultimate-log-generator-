#!/usr/bin/env python3
"""
Infinite WhatsApp Log Generator (Real Numbers) (Python Port)
Compatible with Windows, Mac, Linux, Termux.
Features: Generate 10M Logs, Real Numbers, Real Cities/ISPs, Filter, Export CSV.
"""

import random
import csv
import time
from datetime import datetime, timedelta

# --- 1. Configuration & Databases ---

COUNTRY_DATA = [
    {"name": "United States", "code": "US", "dial": "+1"},
    {"name": "Canada", "code": "CA", "dial": "+1"},
    {"name": "United Kingdom", "code": "GB", "dial": "+44"},
    {"name": "Germany", "code": "DE", "dial": "+49"},
    {"name": "France", "code": "FR", "dial": "+33"},
    {"name": "Australia", "code": "AU", "dial": "+61"},
    {"name": "India", "code": "IN", "dial": "+91"},
    {"name": "Brazil", "code": "BR", "dial": "+55"},
    {"name": "Japan", "code": "JP", "dial": "+81"},
    {"name": "Russia", "code": "RU", "dial": "+7"},
    {"name": "China", "code": "CN", "dial": "+86"},
    {"name": "Mexico", "code": "MX", "dial": "+52"},
    {"name": "Italy", "code": "IT", "dial": "+39"},
    {"name": "South Korea", "code": "KR", "dial": "+82"},
    {"name": "Netherlands", "code": "NL", "dial": "+31"},
    {"name": "Spain", "code": "ES", "dial": "+34"},
    {"name": "Sweden", "code": "SE", "dial": "+46"},
    {"name": "Norway", "code": "NO", "dial": "+47"},
    {"name": "Poland", "code": "PL", "dial": "+48"},
    {"name": "Turkey", "code": "TR", "dial": "+90"},
    {"name": "South Africa", "code": "ZA", "dial": "+27"},
    {"name": "Argentina", "code": "AR", "dial": "+54"},
    {"name": "Belgium", "code": "BE", "dial": "+32"},
    {"name": "Switzerland", "code": "CH", "dial": "+41"},
    {"name": "New Zealand", "code": "NZ", "dial": "+64"},
    {"name": "Singapore", "code": "SG", "dial": "+65"},
    {"name": "Malaysia", "code": "MY", "dial": "+60"},
    {"name": "Thailand", "code": "TH", "dial": "+66"},
    {"name": "Indonesia", "code": "ID", "dial": "+62"},
    {"name": "Vietnam", "code": "VN", "dial": "+84"},
    {"name": "Ireland", "code": "IE", "dial": "+353"},
    {"name": "Czech Republic", "code": "CZ", "dial": "+420"},
    {"name": "Portugal", "code": "PT", "dial": "+351"},
    {"name": "Greece", "code": "GR", "dial": "+30"},
    {"name": "Finland", "code": "FI", "dial": "+358"},
    {"name": "Denmark", "code": "DK", "dial": "+45"},
    {"name": "Colombia", "code": "CO", "dial": "+57"},
    {"name": "Chile", "code": "CL", "dial": "+56"},
    {"name": "Egypt", "code": "EG", "dial": "+20"},
    {"name": "United Arab Emirates", "code": "AE", "dial": "+971"},
    {"name": "Saudi Arabia", "code": "SA", "dial": "+966"},
    {"name": "Israel", "code": "IL", "dial": "+972"},
    {"name": "Philippines", "code": "PH", "dial": "+63"},
    {"name": "Hungary", "code": "HU", "dial": "+36"},
    {"name": "Romania", "code": "RO", "dial": "+40"},
    {"name": "Ukraine", "code": "UA", "dial": "+380"},
    {"name": "Pakistan", "code": "PK", "dial": "+92"},
    {"name": "Bangladesh", "code": "BD", "dial": "+880"},
    {"name": "Morocco", "code": "MA", "dial": "+212"},
    {"name": "Algeria", "code": "DZ", "dial": "+213"},
    {"name": "Angola", "code": "AO", "dial": "+244"},
    {"name": "Armenia", "code": "AM", "dial": "+374"},
    {"name": "Austria", "code": "AT", "dial": "+43"},
    {"name": "Azerbaijan", "code": "AZ", "dial": "+994"},
    {"name": "Bahamas", "code": "BS", "dial": "+1"},
    {"name": "Bahrain", "code": "BH", "dial": "+973"},
    {"name": "Barbados", "code": "BB", "dial": "+1"},
    {"name": "Belarus", "code": "BY", "dial": "+375"},
    {"name": "Belize", "code": "BZ", "dial": "+501"},
    {"name": "Benin", "code": "BJ", "dial": "+229"},
    {"name": "Bhutan", "code": "BT", "dial": "+975"},
    {"name": "Bolivia", "code": "BO", "dial": "+591"},
    {"name": "Bosnia and Herzegovina", "code": "BA", "dial": "+387"},
    {"name": "Botswana", "code": "BW", "dial": "+267"},
    {"name": "Brunei", "code": "BN", "dial": "+673"},
    {"name": "Bulgaria", "code": "BG", "dial": "+359"},
    {"name": "Burkina Faso", "code": "BF", "dial": "+226"},
    {"name": "Burundi", "code": "BI", "dial": "+257"},
    {"name": "Cabo Verde", "code": "CV", "dial": "+238"},
    {"name": "Cambodia", "code": "KH", "dial": "+855"},
    {"name": "Cameroon", "code": "CM", "dial": "+237"},
    {"name": "Central African Republic", "code": "CF", "dial": "+236"},
    {"name": "Chad", "code": "TD", "dial": "+235"},
    {"name": "Comoros", "code": "KM", "dial": "+269"},
    {"name": "Congo", "code": "CG", "dial": "+242"},
    {"name": "Costa Rica", "code": "CR", "dial": "+506"},
    {"name": "Croatia", "code": "HR", "dial": "+385"},
    {"name": "Cuba", "code": "CU", "dial": "+53"},
    {"name": "Cyprus", "code": "CY", "dial": "+357"},
    {"name": "Democratic Republic of the Congo", "code": "CD", "dial": "+243"},
    {"name": "Djibouti", "code": "DJ", "dial": "+253"},
    {"name": "Dominica", "code": "DM", "dial": "+1"},
    {"name": "Dominican Republic", "code": "DO", "dial": "+1"},
    {"name": "Ecuador", "code": "EC", "dial": "+593"},
    {"name": "El Salvador", "code": "SV", "dial": "+503"},
    {"name": "Equatorial Guinea", "code": "GQ", "dial": "+240"},
    {"name": "Eritrea", "code": "ER", "dial": "+291"},
    {"name": "Estonia", "code": "EE", "dial": "+372"},
    {"name": "Eswatini", "code": "SZ", "dial": "+268"},
    {"name": "Ethiopia", "code": "ET", "dial": "+251"},
    {"name": "Fiji", "code": "FJ", "dial": "+679"},
    {"name": "Gabon", "code": "GA", "dial": "+241"},
    {"name": "Georgia", "code": "GE", "dial": "+995"},
    {"name": "Ghana", "code": "GH", "dial": "+233"},
    {"name": "Grenada", "code": "GD", "dial": "+1"},
    {"name": "Guatemala", "code": "GT", "dial": "+502"},
    {"name": "Guinea", "code": "GN", "dial": "+224"},
    {"name": "Guinea-Bissau", "code": "GW", "dial": "+245"},
    {"name": "Guyana", "code": "GY", "dial": "+592"},
    {"name": "Haiti", "code": "HT", "dial": "+509"},
    {"name": "Honduras", "code": "HN", "dial": "+504"},
    {"name": "Iceland", "code": "IS", "dial": "+354"},
    {"name": "Iran", "code": "IR", "dial": "+98"},
    {"name": "Iraq", "code": "IQ", "dial": "+964"},
    {"name": "Jamaica", "code": "JM", "dial": "+1"},
    {"name": "Jordan", "code": "JO", "dial": "+962"},
    {"name": "Kazakhstan", "code": "KZ", "dial": "+7"},
    {"name": "Kenya", "code": "KE", "dial": "+254"},
    {"name": "Kiribati", "code": "KI", "dial": "+686"},
    {"name": "Kuwait", "code": "KW", "dial": "+965"},
    {"name": "Kyrgyzstan", "code": "KG", "dial": "+996"},
    {"name": "Laos", "code": "LA", "dial": "+856"},
    {"name": "Latvia", "code": "LV", "dial": "+371"},
    {"name": "Lebanon", "code": "LB", "dial": "+961"},
    {"name": "Lesotho", "code": "LS", "dial": "+266"},
    {"name": "Liberia", "code": "LR", "dial": "+231"},
    {"name": "Libya", "code": "LY", "dial": "+218"},
    {"name": "Liechtenstein", "code": "LI", "dial": "+423"},
    {"name": "Lithuania", "code": "LT", "dial": "+370"},
    {"name": "Luxembourg", "code": "LU", "dial": "+352"},
    {"name": "Madagascar", "code": "MG", "dial": "+261"},
    {"name": "Malawi", "code": "MW", "dial": "+265"},
    {"name": "Maldives", "code": "MV", "dial": "+960"},
    {"name": "Mali", "code": "ML", "dial": "+223"},
    {"name": "Malta", "code": "MT", "dial": "+356"},
    {"name": "Marshall Islands", "code": "MH", "dial": "+692"},
    {"name": "Mauritania", "code": "MR", "dial": "+222"},
    {"name": "Mauritius", "code": "MU", "dial": "+230"},
    {"name": "Micronesia", "code": "FM", "dial": "+691"},
    {"name": "Moldova", "code": "MD", "dial": "+373"},
    {"name": "Monaco", "code": "MC", "dial": "+377"},
    {"name": "Mongolia", "code": "MN", "dial": "+976"},
    {"name": "Montenegro", "code": "ME", "dial": "+382"},
    {"name": "Mozambique", "code": "MZ", "dial": "+258"},
    {"name": "Myanmar", "code": "MM", "dial": "+95"},
    {"name": "Namibia", "code": "NA", "dial": "+264"},
    {"name": "Nauru", "code": "NR", "dial": "+674"},
    {"name": "Nepal", "code": "NP", "dial": "+977"},
    {"name": "Nicaragua", "code": "NI", "dial": "+505"},
    {"name": "Niger", "code": "NE", "dial": "+227"},
    {"name": "Nigeria", "code": "NG", "dial": "+234"},
    {"name": "North Macedonia", "code": "MK", "dial": "+389"},
    {"name": "Oman", "code": "OM", "dial": "+968"},
    {"name": "Palau", "code": "PW", "dial": "+680"},
    {"name": "Palestine", "code": "PS", "dial": "+970"},
    {"name": "Panama", "code": "PA", "dial": "+507"},
    {"name": "Papua New Guinea", "code": "PG", "dial": "+675"},
    {"name": "Paraguay", "code": "PY", "dial": "+595"},
    {"name": "Peru", "code": "PE", "dial": "+51"},
    {"name": "Qatar", "code": "QA", "dial": "+974"},
    {"name": "Republic of the Congo", "code": "CG", "dial": "+242"},
    {"name": "Rwanda", "code": "RW", "dial": "+250"},
    {"name": "Saint Kitts and Nevis", "code": "KN", "dial": "+1"},
    {"name": "Saint Lucia", "code": "LC", "dial": "+1"},
    {"name": "Saint Vincent and the Grenadines", "code": "VC", "dial": "+1"},
    {"name": "Samoa", "code": "WS", "dial": "+685"},
    {"name": "San Marino", "code": "SM", "dial": "+378"},
    {"name": "Sao Tome and Principe", "code": "ST", "dial": "+239"},
    {"name": "Senegal", "code": "SN", "dial": "+221"},
    {"name": "Serbia", "code": "RS", "dial": "+381"},
    {"name": "Seychelles", "code": "SC", "dial": "+248"},
    {"name": "Sierra Leone", "code": "SL", "dial": "+232"},
    {"name": "Slovakia", "code": "SK", "dial": "+421"},
    {"name": "Slovenia", "code": "SI", "dial": "+386"},
    {"name": "Solomon Islands", "code": "SB", "dial": "+677"},
    {"name": "Somalia", "code": "SO", "dial": "+252"},
    {"name": "South Sudan", "code": "SS", "dial": "+211"},
    {"name": "Sri Lanka", "code": "LK", "dial": "+94"},
    {"name": "Sudan", "code": "SD", "dial": "+249"},
    {"name": "Suriname", "code": "SR", "dial": "+597"},
    {"name": "Syria", "code": "SY", "dial": "+963"},
    {"name": "Tajikistan", "code": "TJ", "dial": "+992"},
    {"name": "Tanzania", "code": "TZ", "dial": "+255"},
    {"name": "Timor-Leste", "code": "TL", "dial": "+670"},
    {"name": "Togo", "code": "TG", "dial": "+228"},
    {"name": "Tonga", "code": "TO", "dial": "+676"},
    {"name": "Trinidad and Tobago", "code": "TT", "dial": "+1"},
    {"name": "Tunisia", "code": "TN", "dial": "+216"},
    {"name": "Tuvalu", "code": "TV", "dial": "+688"},
    {"name": "Uganda", "code": "UG", "dial": "+256"},
    {"name": "Uzbekistan", "code": "UZ", "dial": "+998"},
    {"name": "Vanuatu", "code": "VU", "dial": "+678"},
    {"name": "Vatican City", "code": "VA", "dial": "+379"},
    {"name": "Venezuela", "code": "VE", "dial": "+58"},
    {"name": "Yemen", "code": "YE", "dial": "+967"},
    {"name": "Zambia", "code": "ZM", "dial": "+260"},
    {"name": "Zimbabwe", "code": "ZW", "dial": "+263"}
]

CITIES = {
    "US": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin"],
    "GB": ["London", "Birmingham", "Manchester", "Leeds", "Glasgow", "Liverpool", "Newcastle", "Bristol", "Cardiff", "Edinburgh"],
    "IN": ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur"],
    "BR": ["Sao Paulo", "Rio de Janeiro", "Brasilia", "Salvador", "Fortaleza", "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre"],
    "CN": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Tianjin", "Wuhan", "Hangzhou", "Nanjing", "Chongqing"],
    "DE": ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Dusseldorf", "Leipzig", "Dortmund", "Essen"],
    "default": ["Jakarta", "London", "Paris", "Tokyo", "Sydney", "New York", "Berlin", "Moscow", "Delhi", "Bangkok", "Lagos", "Cairo", "Sao Paulo", "Lima", "Bogota", "Mexico City", "Istanbul", "Kolkata", "Singapore", "Dubai", "Seoul", "Tehran", "Riyadh", "Lahore", "Karachi", "Johannesburg", "Nairobi", "Addis Ababa", "Casablanca", "Alger"]
}

ISPS = ["Google Fiber", "Verizon Fios", "Comcast Xfinity", "AT&T Fiber", "Sprint", "T-Mobile", "O2", "Orange", "Vodafone", "Telefonica", "BT Group", "Deutsche Telekom", "NTT", "KDDI", "SoftBank", "Orange Business", "Liberty Global", "Altice", "Virgin Media", "Starlink", "Telstra", "Optus", "TPG", "Vodafone", "Telco Global", "HyperFiber", "FiberX", "NetBox", "DataStream", "CloudNet", "SecureLink", "NetGuard", "CyberFiber", "GlobalStream", "MetaNet", "IronFiber", "BlueWave", "RedCloud", "GreenNet", "YellowWire", "PurpleData", "CyanLink", "MagentaStream", "AzureNet", "EmeraldFiber", "SapphireLink", "AmethystWire", "OnyxData", "JadeNet", "CoralStream", "CopperWire", "SilverNet", "GoldFiber", "PlatinumLink", "DiamondWire", "CrystalNet", "RubyStream", "PearlWire", "OpalNet", "TopazStream", "QuartzWire", "FlintNet", "BerylStream", "JasperWire", "MalachiteNet", "TurquoiseStream", "LapisWire", "SodaliteNet", "AmberStream", "BronzeWire", "CopperNet", "IronStream", "SteelWire", "TitaniumNet", "ZincStream", "NickelWire", "CobaltNet", "RutileStream", "TantalumWire", "TungstenNet", "UraniumStream", "NeptuniumWire", "PlutoniumNet", "AmericiumStream", "CuriumWire", "BerkeliumNet", "CaliforniumStream", "EinsteiniumWire", "FermiumNet", "MendeleviumStream", "NobeliumWire", "LawrenciumNet", "RutherfordiumStream", "DarmstadtiumWire", "RoentgeniumNet", "CoperniciumStream", "NihoniumWire", "FleroviumNet", "MoscoviumStream", "LivermoriumWire", "TennessineNet", "OganessonStream"]

BROWSERS = [
    {"name": "Chrome", "versions": ["114.0", "115.0", "116.0", "117.0"]},
    {"name": "Firefox", "versions": ["114.0", "115.0", "116.0"]},
    {"name": "Safari", "versions": ["15.1", "16.0", "16.1"]},
    {"name": "Edge", "versions": ["114.0", "115.0", "116.0"]},
    {"name": "Opera", "versions": ["88.0", "89.0", "90.0"]}
]

OS_VERSIONS = {
    "windows": ["10.0", "11.0", "8.1"],
    "mac": ["10_15_7", "11_6", "12_3", "13_0"],
    "linux": ["x86_64", "arm64"],
    "android": ["10", "11", "12", "13"],
    "ios": ["14_4", "15_0", "15_1", "16_0"]
}

DEVICES = [
    "Pixel 5", "Pixel 6", "Pixel 7", "Samsung Galaxy S21", "Samsung Galaxy S22", "OnePlus 9",
    "iPhone 11", "iPhone 12", "iPhone 13", "iPhone 14", "iPad Pro"
]

# --- 2. Core Functions ---

def randInt(min, max):
    return random.randint(min, max)

def randomIP():
    return f"{randInt(1, 255)}.{randInt(0, 255)}.{randInt(0, 255)}.{randInt(1, 254)}"

def randomDate():
    year = 2022 + randInt(0, 3)
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
    else:
        return f"Mozilla/5.0 ({os_str})"

def generateRealWhatsAppNumber(countryObj):
    dial = countryObj["dial"]
    digits = ""
    while len(digits) < 9:
        digits += str(randInt(0, 9))
    digits = digits.lstrip('0')
    formatted = f"{dial} {digits}"
    if len(digits) > 4:
        formatted = f"{dial} {digits[:4]} {digits[4:]}"
    return formatted

def generateCity(countryObj):
    city_list = CITIES.get(countryObj["code"], ["Default City"])
    city = random.choice(city_list)
    if random.random() > 0.5:
        city = random.choice(CITIES["default"])
    return city

def generateISP():
    return random.choice(ISPS)

# --- 3. State Management & Rendering ---

class WhatsAppLogState:
    def __init__(self):
        self.total_logs_generated = 0
        self.all_entries = []
        self.current_country = None
        self.batch_size = 50
        self.max_logs = 10000000
        
    def create_row(self, entry):
        return entry

    def generate_log_entry_for_country(self, country_name, country_obj):
        return {
            "ip": randomIP(),
            "country": country_name,
            "city": generateCity(country_obj),
            "isp": generateISP(),
            "date": randomDate(),
            "time": randomTime(),
            "userAgent": generateUserAgent(),
            "phone": generateRealWhatsAppNumber(country_obj)
        }

    def load_more_logs(self):
        if self.total_logs_generated >= self.max_logs:
            print(f"[INFO] End of logs reached.")
            return

        print(f"[LOG] Generating batch... (Batch Size: {self.batch_size})")
        fragment = []
        for _ in range(self.batch_size):
            if self.total_logs_generated >= self.max_logs:
                break
            country_obj = next(c for c in COUNTRY_DATA if c["name"] == self.current_country)
            entry = self.generate_log_entry_for_country(self.current_country, country_obj)
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
        return [e for e in self.all_entries if filter_term.lower() in e["ip"].lower() or filter_term.lower() in e["country"].lower() or filter_term.lower() in e["phone"].lower() or filter_term.lower() in e["city"].lower() or filter_term.lower() in e["isp"].lower() or filter_term.lower() in e["userAgent"].lower()]

    def export_report(self):
        if not self.current_country or not self.all_entries:
            print("[INFO] No logs to export.")
            return
        
        filename = f"whatsapp_logs_{self.current_country.replace(' ', '_')}_{int(time.time())}.csv"
        header = ["IP Address", "Country", "City", "ISP", "Time", "Date", "WhatsApp Number"]
        
        # Limit to 100k for performance if needed, or use all
        limit = 100000
        data = self.all_entries[:limit]
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for e in data:
                writer.writerow([
                    e["ip"], 
                    f'"{e["country"]}"', 
                    f'"{e["city"]}"', 
                    f'"{e["isp"]}"', 
                    f'"{e["time"]}"', 
                    f'"{e["date"]}"', 
                    f'"{e["phone"]}"'
                ])
        print(f"[EXPORT] Report saved to: {filename}")

    def set_country(self, country):
        country_obj = next((c for c in COUNTRY_DATA if c["name"] == country), None)
        if country_obj:
            self.current_country = country
            print(f"[CONFIG] Target Country: {country}")
        else:
            print(f"[CONFIG] Warning: Country '{country}' not found. Using first available.")
            self.current_country = COUNTRY_DATA[0]["name"]

# --- 4. Event Listeners & Main Loop ---

def main():
    state = WhatsAppLogState()
    initial_country = random.choice(COUNTRY_DATA)
    state.current_country = initial_country
    
    print("=" * 60)
    print("INFINITE WHATSAPP LOG GENERATOR (Real Numbers) (Python Port)")
    print("=" * 60)
    print(f"[INIT] Starting...")
    print(f"[CONFIG] Default Country: {initial_country['name']}")
    print("-" * 60)
    
    # Initial Load
    print(f"[LOG] Loading initial batch...")
    initial_batch = state.load_more_logs()
    print(f"[LOG] Loaded {len(initial_batch)} entries.")
    print("-" * 60)
    
    while True:
        action = input("Command [next/generate/filter/export/reset/config/country]: ").strip().lower()
        
        if action == "next":
            state.load_more_logs()
            print(f"[LOG] Generated more entries. Total: {state.total_logs_generated}")
        elif action == "generate":
            batch = state.load_more_logs()
            print(f"[LOG] Generated {len(batch)} entries.")
        elif action == "filter":
            term = input("Filter term (IP, Country, City, Phone, ISP, User-Agent...): ").strip()
            if term:
                filtered = state.filter_logs(term)
                print(f"[RESULT] Found {len(filtered)} matching entries:")
                for i, e in enumerate(filtered[:5]):
                    print(f"  {i+1}. {e['ip']} - {e['country']} - {e['phone']}")
                if len(filtered) > 5:
                    print(f"  ... and {len(filtered) - 5} more.")
        elif action == "export":
            state.export_report()
        elif action == "reset":
            state.reset_logs()
        elif action == "config":
            cnt = input("Set Country (type 'random' for random): ").strip().lower()
            if cnt == "random":
                state.current_country = random.choice(COUNTRY_DATA)["name"]
                print(f"[CONFIG] New Random Country: {state.current_country}")
            else:
                state.set_country(cnt.title())
        elif action == "help":
            print("""
Available Commands:
  next      - Load next batch of 50 logs
  generate  - Force generate next batch
  filter    - Filter logs by IP, Country, City, Phone, ISP, User-Agent
  export    - Export current logs to CSV (limit 100k)
  reset     - Reset all logs
  config    - Change target country
  help      - Show this menu
            """)
        elif action == "country":
            cnt = input("Enter Country Name: ").strip().title()
            state.set_country(cnt)
        elif not action:
            pass
        else:
            print(f"[INFO] Unknown command: {action}")
            
        print("-" * 60)

if __name__ == "__main__":
    main()
