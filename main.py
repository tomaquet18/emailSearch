import argparse
from google_scraper import extract_mails
import itertools
import sys

SEPARATORS = [".", "-", ""]
SPECIAL_CHARS = [".", "-", "!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~"]

def banner():
    print("___________                 .__ .__     _________                               .__     ")
    print("\_   _____/  _____  _____   |__||  |   /   _____/  ____  _____  _______   ____  |  |__  ")
    print(" |    __)_  /     \ \__  \  |  ||  |   \_____  \ _/ __ \ \__  \ \_  __ \_/ ___\ |  |  \ ")
    print(" |        \|  Y Y  \ / __ \_|  ||  |__ /        \\\  ___/  / __ \_|  | \/\  \___ |   Y  \\")
    print("/_______  /|__|_|  /(____  /|__||____//_______  / \___  >(____  /|__|    \___  >|___|  /")
    print("        \/       \/      \/                   \/      \/      \/             \/      \/ ")
    print("                                                                     by: tomaquet18")

def create_combinations(name, lastname, separators, domain):
    combinations = []

    for separator in separators:
        # ex. john.doe
        combinations.append(name + separator + lastname + "@" + domain)

        # ex. j.doe
        combinations.append(name[0] + separator + lastname + "@" + domain)

        # ex. doe.john
        combinations.append(lastname + separator + name + "@" + domain)
    

    return combinations

def get_parameters():
    parser = argparse.ArgumentParser(description='Mail permutation')
    parser.add_argument('-n', '--name', type=str, help='Name')
    parser.add_argument('-l', '--lastname', type=str, help='Lastname')
    parser.add_argument('-d', '--domain', type=str, help='Domain')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        exit(1)
    return (args.name.lower(), args.lastname.lower(), args.domain.lower())

def print_results(combinations):
    for combination in combinations:
        print(combination)

def extract_separators(emails):
    separators_list = []
    for email in emails:
        username = email.split("@")[0]
        for c in username:
            for special_char in SPECIAL_CHARS:
                if special_char == c:
                    separators_list.append(c)
    if len(separators_list) == 0:
        return SEPARATORS
    return separators_list

def main():
    # Get parameters
    name, lastname, domain = get_parameters()

    # Search emails from specified domain in Google
    found_emails = extract_mails(domain)
    if not len(found_emails) == 0:
        print(f"{len(found_emails)} emails found in Google:")
        print_results(found_emails)
    else:
        print("No emails found in Google :(")

    separators = extract_separators(found_emails)
    if not separators == SEPARATORS:
        print("\nDetected some separators in email:")
        print_results(separators)
    else:
        print("\nNo separators detected in email")

    combinations = create_combinations(name, lastname, separators, domain)
    if not separators == SEPARATORS:
        print("\nGenerated emails based on structure:")
    else:    
        print("\nGenerated emails using default list of separators:")
    print_results(combinations)


if __name__ == "__main__":
    banner()
    main()