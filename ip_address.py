#!/usr/bin/env python3
"""
Log IP with Country Filter (Python Port)
Compatible with Windows, Mac, Linux, Termux.
Features: Generate Logs, Filter, Export CSV, Country Selection, Real User-Agent.
"""

import random
import csv
import time
from datetime import datetime, timedelta

# --- 1. Configuration & Databases ---

COUNTRIES = [
    "United States", "Canada", "United Kingdom", "Germany", "France", "Australia", "India",
    "Brazil", "Japan", "Russia", "China", "Mexico", "Italy", "South Korea", "Netherlands",
    "Spain", "Sweden", "Norway", "Poland", "Turkey", "South Africa", "Argentina", "Belgium",
    "Switzerland", "New Zealand", "Singapore", "Malaysia", "Thailand", "Indonesia", "Vietnam",
    "Ireland", "Czech Republic", "Portugal", "Greece", "Finland", "Denmark", "Colombia",
    "Chile", "Egypt", "United Arab Emirates", "Saudi Arabia", "Israel", "Philippines",
    "Hungary", "Romania", "Ukraine", "Pakistan", "Bangladesh", "Morocco", "Algeria", "Angola",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
    "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
    "Chad", "Chile", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba",
    "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti",
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
    "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
    "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan",
    "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan",
    "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    "Yemen", "Zambia", "Zimbabwe"
]

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
    year = 2022
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

# --- 3. State Management & Rendering ---

class IPLogState:
    def __init__(self):
        self.total_logs_generated = 0
        self.all_entries = []
        self.current_country = None
        self.batch_size = 50
        self.max_logs = 10000000
        
    def create_row(self, entry):
        return entry

    def generate_log_entry_for_country(self, country):
        return {
            "ip": randomIP(),
            "country": country,
            "date": randomDate(),
            "time": randomTime(),
            "userAgent": generateUserAgent()
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
            entry = self.generate_log_entry_for_country(self.current_country)
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
        return [e for e in self.all_entries if filter_term.lower() in e["ip"].lower() or filter_term.lower() in e["country"].lower() or filter_term.lower() in e["userAgent"].lower()]

    def export_report(self):
        if not self.current_country or not self.all_entries:
            print("[INFO] No logs to export.")
            return
        
        filename = f"logs_{self.current_country.replace(' ', '_')}_{int(time.time())}.csv"
        header = ["IP Address", "Country", "Date", "Time", "User-Agent"]
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for e in self.all_entries:
                writer.writerow([
                    e["ip"], 
                    f'"{e["country"]}"', 
                    f'"{e["date"]}"', 
                    f'"{e["time"]}"', 
                    f'"{e["userAgent"]}"'
                ])
        print(f"[EXPORT] Report saved to: {filename}")

    def set_country(self, country):
        if country in COUNTRIES:
            self.current_country = country
            print(f"[CONFIG] Target Country: {country}")
        else:
            print(f"[CONFIG] Warning: Country '{country}' not found in list. Using first available.")
            self.current_country = COUNTRIES[0]

# --- 4. Event Listeners & Main Loop ---

def main():
    state = IPLogState()
    # Initialize with a random country
    initial_country = random.choice(COUNTRIES)
    state.current_country = initial_country
    
    print("=" * 60)
    print("LOG IP WITH COUNTRY FILTER (Python Port)")
    print("=" * 60)
    print(f"[INIT] Starting...")
    print(f"[CONFIG] Default Country: {initial_country}")
    
    # Initial Load
    print(f"[LOG] Loading initial batch...")
    initial_batch = state.load_more_logs()
    print(f"[LOG] Loaded {len(initial_batch)} entries.")
    print("-" * 60)
    
    while True:
        # Check for scroll (simulated by checking batch count)
        # In a terminal, we just keep generating if requested or auto-loop
        
        action = input("Command [next/generate/filter/export/reset/config/country]: ").strip().lower()
        
        if action == "next":
            state.load_more_logs()
            print(f"[LOG] Generated more entries. Total: {state.total_logs_generated}")
        elif action == "generate":
            batch = state.load_more_logs()
            print(f"[LOG] Generated {len(batch)} entries.")
        elif action == "filter":
            term = input("Filter term (IP, Country, User-Agent...): ").strip()
            if term:
                filtered = state.filter_logs(term)
                print(f"[RESULT] Found {len(filtered)} matching entries:")
                for i, e in enumerate(filtered[:5]): # Show first 5
                    print(f"  {i+1}. {e['ip']} - {e['country']} - {e['userAgent'][:30]}...")
                if len(filtered) > 5:
                    print(f"  ... and {len(filtered) - 5} more.")
        elif action == "export":
            state.export_report()
        elif action == "reset":
            state.reset_logs()
        elif action == "config":
            cnt = input("Set Country (type 'random' for random): ").strip().lower()
            if cnt == "random":
                state.current_country = random.choice(COUNTRIES)
                print(f"[CONFIG] New Random Country: {state.current_country}")
            else:
                state.set_country(cnt.title())
        elif action == "help":
            print("""
Available Commands:
  next      - Load next batch of 50 logs
  generate  - Force generate next batch
  filter    - Filter logs by IP, Country, User-Agent, etc.
  export    - Export current logs to CSV
  reset     - Reset all logs
  config    - Change target country
  help      - Show this menu
            """)
        elif action == "country":
            cnt = input("Enter Country Name: ").strip().title()
            state.set_country(cnt)
        elif not action:
            # Do nothing
            pass
        else:
            print(f"[INFO] Unknown command: {action}")
            
        print("-" * 60)

if __name__ == "__main__":
    main()
