Disclaimer 😏🔥
This tool is intended for ethical hacking and security research purposes only. Use it only on websites you have explicit permission to test. Misuse of this tool may be illegal in some jurisdictions. Always have written consent before performing any penetration testing.

# WP Brute Force Attack user Scanner

A simple and efficient WordPress live brute-force login attacks. The tool reads a list of WordPress sites, enumerates live usernames, and performs brute-force login attempts with common passwords.

## Features

- Enumerates usernames from WordPress sites.
- Performs brute-force login attacks with common passwords.
- Supports verbose output for detailed debugging.
- Saves scan results in a **JSON** format.
- Scans multiple sites listed in a `site_list.txt` file.

## Requirements

- Python 3.x
- Required Python libraries:


## Installation

```bash
pip install -r requirements.txt
### Clone the repository:

```bash
git clone https://github.com/your-username/wp-bruteforce-scanner.git
cd wp-bruteforce-scanner

## Usage
To run the scanner on all sites listed in the site_list.txt file, use the following command:

```bash
python brute_force_all.py

## Options:
--verbose : Enable verbose output for detailed attack logs.

--threads <number> : Set the number of threads for faster scanning (default is 5).

--save-json : Save the results in a brute_force_report.json file.

## Example:

```bash
python brute_force_all.py --verbose --threads 10 --save-json

⭐️ Good luck!
