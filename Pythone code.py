import json
import os
class MissingPersonReport:
    def init(self, filename='missing_persons.json'):
        self.filename = filename
        self.reports = self.load_reports()
    def load_reports(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    def add_report(self, name, age, last_seen, description):
        report = {
            'name': name,
            'age': age,
            'last_seen': last_seen,
            'description': description
        }
        self.reports.append(report)
        self.save_reports()
    def save_reports(self):
        with open(self.filename, 'w') as file:
            json.dump(self.reports, file, indent=4)
    def display_reports(self):
        if not self.reports:
            print("No reports found.")
            return
        for index, report in enumerate(self.reports, start=1):
            print(f"Report {index}:")
            print(f"  Name: {report['name']}")
            print(f"  Age: {report['age']}")
            print(f"  Last Seen: {report['last_seen']}")
            print(f"  Description: {report['description']}\n")
def main():
    tool = MissingPersonReport()
    while True:
        print("Missing Person Report Tool")
        print("1. Add Report")
        print("2. Display Reports")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter the name of the missing person: ")
            age = input("Enter the age of the missing person: ")
            last_seen = input("Enter the last seen location: ")
            description = input("Enter a description: ")
            tool.add_report(name, age, last_seen, description)
            print("Report added successfully.\n")
        elif choice == '2':
            tool.display_reports()
        elif choice == '3':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please try again.\n")
if name == "main":
    main()