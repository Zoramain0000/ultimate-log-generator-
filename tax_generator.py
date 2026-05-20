#!/usr/bin/env python3
"""
Transaction ID Generator with Platform Filter (Python Port)
Compatible with Windows, Mac, Linux, Termux.
Features: Generate Logs, Filter, Export CSV, Platform Selection.
"""

import random
import csv
import time
from datetime import datetime, timedelta

# --- 1. Configuration & Databases ---

PLATFORMS = [
    "Facebook", "Instagram", "Twitter", "LinkedIn", "Snapchat", "TikTok", "WhatsApp",
    "Telegram", "Signal", "Discord", "Reddit", "Pinterest", "YouTube", "Twitch",
    "Spotify", "Netflix", "Amazon", "Apple Pay", "Google Pay", "PayPal", "Venmo",
    "Cash App", "Stripe", "Shopify", "Etsy", "Uber", "Lyft", "Airbnb", "DoorDash",
    "Grubhub", "Uber Eats", "Zomato", "Swiggy", "Razorpay", "PhonePe", "Google Ads",
    "Facebook Ads", "Instagram Ads", "TikTok Ads", "LinkedIn Ads", "Snapchat Ads",
    "Twitter Ads", "Pinterest Ads", "Microsoft Ads", "Amazon Ads", "Shopify Payments",
    "Square", "Coinbase", "Binance", "Kraken", "Robinhood", "eToro", "Webull",
    "Alibaba", "Wish", "Walmart", "Target", "Best Buy", "eBay", "AliExpress",
    "Flipkart", "Mercado Libre", "Rakuten", "GoFundMe", "Kickstarter", "Patreon",
    "Buy Me a Coffee", "OnlyFans", "Fiverr", "Upwork", "Freelancer", "Toptal",
    "Adobe", "Microsoft 365", "Google Workspace", "Dropbox", "Zoom", "Slack",
    "AWS", "DigitalOcean", "Vercel", "Netlify", "Heroku", "Cloudflare",
    "Namecheap", "GoDaddy", "Bluehost", "Hostinger", "SiteGround", "WP Engine",
    "Grammarly", "Canva", "Figma", "Notion", "Trello", "Asana", "Monday.com",
    "HubSpot", "Salesforce", "Mailchimp", "SendGrid", "Constant Contact",
    "Steam", "Epic Games", "Xbox", "PlayStation", "Nintendo", "Roblox", "Minecraft",
    "Play Store", "App Store", "Samsung Pay", "Alipay", "WeChat Pay", "Paytm",
    "Google One", "iCloud", "GitHub", "GitLab", "Bitbucket", "Digital River",
    "Paddle", "Gumroad", "Sellfy", "Teachable", "Udemy", "Coursera", "Skillshare"
]

STATUSES = ["Completed", "Pending", "Processing", "Failed", "Refunded", "Chargeback", "Cancelled", "On Hold"]

# --- 2. Core Functions ---

def randInt(min, max):
    return random.randint(min, max)

def randomTransactionID():
    prefix = "TXN"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = prefix
    for _ in range(16):
        result += chars[random.randint(0, len(chars) - 1)]
    return result

def randomAmount():
    dollars = randInt(1, 9999)
    cents = randInt(0, 99)
    return f"{dollars}.{str(cents).zfill(2)}"

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

# --- 3. State Management & Rendering ---

class TxGeneratorState:
    def __init__(self):
        self.total_logs_generated = 0
        self.all_entries = []
        self.current_platform = None
        self.batch_size = 50
        self.max_logs = 10000000
        
    def create_row(self, entry):
        return entry

    def generate_log_entry_for_platform(self, platform):
        return {
            "txnId": randomTransactionID(),
            "platform": platform,
            "amount": randomAmount(),
            "date": randomDate(),
            "time": randomTime(),
            "status": random.choice(STATUSES)
        }

    def load_more_logs(self):
        if self.total_logs_generated >= self.max_logs:
            print(f"[INFO] End of transaction logs reached.")
            return

        print(f"[LOG] Generating batch... (Batch Size: {self.batch_size})")
        fragment = []
        for _ in range(self.batch_size):
            if self.total_logs_generated >= self.max_logs:
                break
            entry = self.generate_log_entry_for_platform(self.current_platform)
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
        return [e for e in self.all_entries if filter_term.lower() in e["txnId"].lower() or filter_term.lower() in e["platform"].lower() or filter_term.lower() in e["status"].lower()]

    def export_report(self):
        if not self.current_platform or not self.all_entries:
            print("[INFO] No logs to export.")
            return
        
        filename = f"transactions_{self.current_platform}_{int(time.time())}.csv"
        header = ["Transaction ID", "Platform", "Amount ($)", "Date", "Time", "Status"]
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for e in self.all_entries:
                writer.writerow([
                    e["txnId"], 
                    f'"{e["platform"]}"', 
                    f'"{e["amount"]}"', 
                    f'"{e["date"]}"', 
                    f'"{e["time"]}"', 
                    f'"{e["status"]}"'
                ])
        print(f"[EXPORT] Report saved to: {filename}")

    def set_platform(self, platform):
        if platform in PLATFORMS:
            self.current_platform = platform
            print(f"[CONFIG] Target Platform: {platform}")
        else:
            print(f"[CONFIG] Warning: Platform '{platform}' not found in list. Using first available.")
            self.current_platform = PLATFORMS[0]

# --- 4. Event Listeners & Main Loop ---

def main():
    state = TxGeneratorState()
    # Initialize with a random platform
    initial_platform = random.choice(PLATFORMS)
    state.current_platform = initial_platform
    
    print("=" * 60)
    print("TRANSACTION ID GENERATOR WITH PLATFORM FILTER (Python Port)")
    print("=" * 60)
    print(f"[INIT] Starting...")
    print(f"[CONFIG] Default Platform: {initial_platform}")
    
    # Initial Load
    print(f"[LOG] Loading initial batch...")
    initial_batch = state.load_more_logs()
    print(f"[LOG] Loaded {len(initial_batch)} entries.")
    print("-" * 60)
    
    while True:
        # Check for scroll (simulated by checking batch count)
        # In a terminal, we just keep generating if requested or auto-loop
        
        action = input("Command [next/generate/filter/export/reset/config/platform]: ").strip().lower()
        
        if action == "next":
            state.load_more_logs()
            print(f"[LOG] Generated more entries. Total: {state.total_logs_generated}")
        elif action == "generate":
            batch = state.load_more_logs()
            print(f"[LOG] Generated {len(batch)} entries.")
        elif action == "filter":
            term = input("Filter term (TXN ID, Platform, Status...): ").strip()
            if term:
                filtered = state.filter_logs(term)
                print(f"[RESULT] Found {len(filtered)} matching entries:")
                for i, e in enumerate(filtered[:5]): # Show first 5
                    print(f"  {i+1}. {e['txnId']} - {e['platform']} - {e['status']}")
                if len(filtered) > 5:
                    print(f"  ... and {len(filtered) - 5} more.")
        elif action == "export":
            state.export_report()
        elif action == "reset":
            state.reset_logs()
        elif action == "config":
            plat = input("Set Platform (type 'random' for random): ").strip().lower()
            if plat == "random":
                state.current_platform = random.choice(PLATFORMS)
                print(f"[CONFIG] New Random Platform: {state.current_platform}")
            else:
                state.set_platform(plat.title())
        elif action == "help":
            print("""
Available Commands:
  next      - Load next batch of 50 logs
  generate  - Force generate next batch
  filter    - Filter logs by TXN ID, Platform, Status, etc.
  export    - Export current logs to CSV
  reset     - Reset all logs
  config    - Change target platform
  help      - Show this menu
            """)
        elif action == "platform":
            plat = input("Enter Platform Name: ").strip().title()
            state.set_platform(plat)
        elif not action:
            # Do nothing
            pass
        else:
            print(f"[INFO] Unknown command: {action}")
            
        print("-" * 60)

if __name__ == "__main__":
    main()
