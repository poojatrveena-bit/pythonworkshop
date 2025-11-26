import random
import time

class AadhaarCard:
    def __init__(self, name, age, dob, phone):
        self.name = name
        self.age = age
        self.dob = dob
        self.phone = phone
        self.aadhaar_number = self.generate_aadhaar_number()
        self.fingerprint_status = "Not Scanned"
        self.eye_scan_status = "Not Scanned"

    def generate_aadhaar_number(self):
        return str(random.randint(10**11, (10**12)-1))

    def scan_fingerprint(self):
        print("\nScanning Fingerprint...")
        time.sleep(2)
        self.fingerprint_status = "Fingerprint Scan Successful"
        print("✔ Fingerprint captured successfully!")

    def scan_eye(self):
        print("\nPerforming Eye (Iris) Scan...")
        time.sleep(2)
        self.eye_scan_status = "Eye Scan Successful"
        print("✔ Iris scan completed successfully!")

    def display_card(self):
        print("\n-----------------------------------")
        print("           AADHAAR CARD            ")
        print("-----------------------------------")
        print(f"Aadhaar Number : {self.aadhaar_number}")
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Date of Birth  : {self.dob}")
        print(f"Phone Number   : {self.phone}")
        print(f"Fingerprint    : {self.fingerprint_status}")
        print(f"Eye Scan       : {self.eye_scan_status}")
        print("-----------------------------------")


# ------------ MAIN PROGRAM --------------

name = input("Enter Name: ")
age = input("Enter Age: ")
dob = input("Enter Date of Birth (DD/MM/YYYY): ")
phone = input("Enter Phone Number: ")

# Create Aadhaar Object
card = AadhaarCard(name, age, dob, phone)

# Biometric Scanning
card.scan_fingerprint()
card.scan_eye()

# Display Aadhaar Card
card.display_card()
