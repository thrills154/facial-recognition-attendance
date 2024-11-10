import firebase_admin
from firebase_admin import credentials, db

class Report:
    def __init__(self, database):
        """
        Initialize the Report class with a database reference.
        :param database: The database reference for Firebase.
        """
        self.db = database

    def fetch_all_records(self):
        """
        Fetches all attendance records from the Firebase database.
        """
        try:
            students_data = self.db.reference('Students').get()
            if students_data:
                print("Attendance Records:")
                for student_id, data in students_data.items():
                    print(f"ID: {student_id}, Name: {data['name']}, "
                          f"Total Attendance: {data['total_attendance']}, "
                          f"Last Attendance Time: {data['last_attendance_time']}")
            else:
                print("No records found.")
        except Exception as e:
            print(f"Error fetching attendance records: {e}")

    def generate_report(self, filename="Attendance_Report.txt"):
        """
        Generates a report and saves it to a text file.
        :param filename: Name of the file to save the report.
        """
        try:
            students_data = self.db.reference('Students').get()
            with open(filename, 'w') as file:
                file.write("Attendance Report\n")
                file.write("=" * 30 + "\n")
                if students_data:
                    for student_id, data in students_data.items():
                        file.write(f"ID: {student_id}\n")
                        file.write(f"Name: {data['name']}\n")
                        file.write(f"Total Attendance: {data['total_attendance']}\n")
                        file.write(f"Last Attendance Time: {data['last_attendance_time']}\n")
                        file.write("-" * 30 + "\n")
                    print(f"Report generated successfully and saved as {filename}")
                else:
                    file.write("No records found.\n")
                    print("No records found. Report generated with no data.")
        except Exception as e:
            print(f"Error generating report: {e}")

# Firebase initialization
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-19a92-default-rtdb.firebaseio.com/"
})

# Usage
report = Report(db)
report.fetch_all_records()
report.generate_report()
