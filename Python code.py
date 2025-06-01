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
    found = False
    for report in reports:
        if report["full_name"].strip().lower() == name and report["age"].strip() == age:
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
def update_report(reports):
    print("\n--- Update a Missing Person Report ---")
    reporter_name = input("Enter your name (as the reporter): ").strip().lower()
    missing_name = input("Enter the full name of the missing person: ").strip().lower()
    
    matching_reports = [
        report for report in reports 
        if report["reporter_name"].strip().lower() == reporter_name 
        and report["full_name"].strip().lower() == missing_name
    ]
    
    if not matching_reports:
        print("❌ No matching reports found. Verify your name and the missing person's name.")
        print("Make sure you entered your Full name")
        return
    
    print(f"\nFound {len(matching_reports)} report(s):")
    for i, report in enumerate(matching_reports, 1):
        print(f"\nReport #{i}")
        for key, value in report.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    report_idx = int(input("\nEnter the report number to update: ")) - 1
    if report_idx < 0 or report_idx >= len(matching_reports):
        print("❌ Invalid selection.")
        return
    
    report_to_update = matching_reports[report_idx]
    
    print("\n--- Update Fields (press Enter to keep current value) ---")
    for key in report_to_update:
        if key == "submission_date":
            continue
        current_value = report_to_update[key]
        new_value = input(f"{key.replace('_', ' ').title()} (current: {current_value}): ").strip()
        if new_value:
            report_to_update[key] = new_value
    
    print("✅ Report updated successfully.")
def main():
    reports = load_data()
    while True:
        print("\n--- Missing Person Report System ---")
        print("1. Search for a missing person")
        print("2. Submit a new report")
        print("3. I'm the missing person - check if someone reported me")
        print("4. View all reports")
        print("5. Update a report")
        print("6. Exit")
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
            update_report(reports)
            save_data(reports)
        elif choice == "6":
            save_data(reports)
            print("\n🙏 Thank you for using the Missing Person Report System.")
            print("👋 Goodbye, and good luck in your search.\n")
            break
        else:
            print("Invalid option. Please try again.")

main()
