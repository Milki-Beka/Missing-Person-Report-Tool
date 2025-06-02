import json
import os

DATA_FILE = "missing_person_reports.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def submit_report(reports):
    print("\n--- Submit a Missing Person Report ---")
    report = {
        "full_name": input("Full name of missing person: "),
        "age": input("Age when missed: "),
        "how_missed": input("How they were missed: "),
        "date_missed": input("Date or year they went missing: "),
        "reporter_name": input("Your name: "),
        "relationship": input("Relationship to the missing person: "),
        "phone": input("Your phone number: "),
        "address": input("Your address: "),
        "submission_date":input("enter reported date: ")
    }
    reports.append(report)
    print("Report submitted successfully.")
    print("🙏 Good luck in your search. Hopefully you find them safe and sound.\n")

def search_missing_person(reports):
    print("\n--- Search for a Missing Person ---")
    name = input("Enter full name of missing person: ").strip().lower()
    age = input("Enter age of missing person: ").strip()
    date = input("Enter the year or date they went missing: ").strip()
    found = False
    for report in reports:
        if report["full_name"].strip().lower() == name and report["age"].strip() == age and report["date_missed"].strip() == date:
            found = True
            print("\n--- ✅ Report found with this name and age. We hope you find them safe and sound. ---")
            for key, value in report.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
    if not found:
        print("\n❌ Sorry, no match found.")
        print("👉 You can make a new report using Option 2.\n")

def missing_person_search_self(reports):
    print("\n--- I'm the Missing Person ---")
    name = input("Enter your full name: ").strip().lower()
    age = input("Enter your age: ").strip()
    date = input("Enter the year or date you went missing: ").strip()
    found = False
    for report in reports:
        if report["full_name"].strip().lower() == name and report["date_missed"].strip() == date and report["age"].strip() == age:
            found = True
            print("\n 🎉 Congratulations! Someone is looking for you with a similar name, age and date.")
            print(f"Reported by: {report['reporter_name']}")
            print(f"Relationship: {report['relationship']}")
            print(f"Phone: {report['phone']}")
            print(f"Address: {report['address']}")
    if not found:
        print("😔 Sorry, no match found. You can report yourself using Option 2 or view all reports with Option 4.")

def view_all_reports(reports):
    print("\n--- All Missing Person Reports ---")
    if not reports:
        print("No reports available.")
        return
    for i, report in enumerate(reports, 1):
        print(f"\nReport #{i}")
        for key, value in report.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
def main():
    reports = load_data()
    while True:
        print("\n--- Missing Person Report System ---")
        print("1. Search for a missing person")
        print("2. Submit a new report")
        print("3. I'm the missing person - check if someone reported me")
        print("4. View all reports")
        print("5. Exit ")
        choice = input("Choose an option: ")

        if choice == "1":
            search_missing_person(reports)
        elif choice == "2":
            submit_report(reports)
            save_data(reports)
        elif choice == "3":
            missing_person_search_self(reports)
        elif choice == "4":
            view_all_reports(reports)
        elif choice == "5":
            save_data(reports)
            print("\n🙏 Thank you for using the Missing Person Report System.")
            print("👋 Goodbye, and good luck in your search.\n")
            break
        else:
            print("Invalid option. Please try again.")

main()  
def delete_report(reports):
    print("\n--- Delete a Report ---")
    name = input("Enter missing person's name: ").lower()
    phone = input("Enter your phone number (to verify): ").strip()
    
    for report in reports[:]:
        if (report["full_name"].lower() == name and 
            report["phone"].strip() == phone):
            reports.remove(report)
            print("✅ Report deleted.")
            return
    
    print("❌ No matching report found or verification failed.")
and add on functon def an other option like given below
# Add to main menu:
# print("5. Delete a report")
# elif choice == "5": 
delete_report(reports) 
save_data(reports)