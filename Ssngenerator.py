import time
import random
import datetime
from faker import Faker

fake = Faker()

# ANSI color escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
END = "\033[0m"

def generate_ssn(name, gender, dob, state, race):
    # Generate random first three digits (Area Number)
    area_number = random.randint(1, 899)
    if area_number == 666:  # Avoid numbers reserved for special use
        area_number += 1

    # Generate random middle two digits (Group Number)
    group_number = random.randint(1, 99)

    # Generate random last four digits (Serial Number)
    serial_number = random.randint(1, 9999)

    # Format SSN as XXX-XX-XXXX
    ssn = "{:03d}-{:02d}-{:04d}".format(area_number, group_number, serial_number)

    # Format DOB as MM/DD/YYYY
    dob_formatted = dob.strftime("%m/%d/%Y")

    return {
        "Name": name,
        "Gender": gender,
        "DOB": dob_formatted,
        "State": state,
        "Race": race,
        "SSN": ssn
    }

def generate_random_person(gender, state, dob, race):
    # Generate random name
    name = fake.name()

    return generate_ssn(name, gender, dob, state, race)

def show_banner():
    print(RED + "=======================================")
    print("      Social Security Number (SSN)      ")
    print("             Generator Tool             ")
    print("               Made by                 ")
    print("             DroidDevHub               ")
    print("=======================================" + END)
    print()

def show_loading_screen():
    print(YELLOW + "Generating SSN...", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(END)

def show_ssn_screen(person_info):
    print("\n" + GREEN + "Random Person Information:")
    for key, value in person_info.items():
        print(f"{key}: {value}")
    print("\n" + YELLOW + "Thank you for using this tool!" + END)

def main():
    show_banner()
    show_loading_screen()

    # Define lists for gender, states, and races
    genders = [YELLOW + "Male", "Female" + END]
    states = [
        YELLOW + "AL - Alabama", "AK - Alaska", "AZ - Arizona", "AR - Arkansas", "CA - California",
        "CO - Colorado", "CT - Connecticut", "DE - Delaware", "FL - Florida", "GA - Georgia",
        "HI - Hawaii", "ID - Idaho", "IL - Illinois", "IN - Indiana", "IA - Iowa",
        "KS - Kansas", "KY - Kentucky", "LA - Louisiana", "ME - Maine", "MD - Maryland",
        "MA - Massachusetts", "MI - Michigan", "MN - Minnesota", "MS - Mississippi", "MO - Missouri",
        "MT - Montana", "NE - Nebraska", "NV - Nevada", "NH - New Hampshire", "NJ - New Jersey",
        "NM - New Mexico", "NY - New York", "NC - North Carolina", "ND - North Dakota", "OH - Ohio",
        "OK - Oklahoma", "OR - Oregon", "PA - Pennsylvania", "RI - Rhode Island", "SC - South Carolina",
        "SD - South Dakota", "TN - Tennessee", "TX - Texas", "UT - Utah", "VT - Vermont",
        "VA - Virginia", "WA - Washington", "WV - West Virginia", "WI - Wisconsin", "WY - Wyoming" + END
    ]
    races = [
        YELLOW + "White", "Black or African American", 
        "American Indian or Alaska Native", "Asian", 
        "Native Hawaiian or Other Pacific Islander" + END
    ]

    # Prompt user to choose gender, state, race, and DOB
    show_banner()
    print(CYAN + "Choose gender:")
    for i, gender in enumerate(genders, start=1):
        print(f"{i}: {gender}")
    gender_choice = int(input("Enter the number of your gender (1: Male, 2: Female): ")) - 1

    show_banner()
    print("\n" + CYAN + "Choose state:")
    for i, state in enumerate(states, start=1):
        print(f"{i}: {state}")
    state_choice = int(input("Enter the number of the state you were born in: ")) - 1

    show_banner()
    print("\n" + CYAN + "Choose race:")
    for i, race in enumerate(races, start=1):
        print(f"{i}: {race}")
    race_choice = int(input("Enter the number of your race: ")) - 1

    show_banner()
    dob_input = input("\nEnter date of birth (YYYY/MM/DD): ")
    dob = datetime.datetime.strptime(dob_input, "%Y/%m/%d")

    # Generate and print a random person's information
    person_info = generate_random_person(genders[gender_choice], states[state_choice], dob, races[race_choice])
    show_ssn_screen(person_info)

if __name__ == "__main__":
    main()
