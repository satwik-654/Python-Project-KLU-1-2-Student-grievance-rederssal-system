# Student Grievance Redressal System (Console Based)

complaints = []


def submit_complaint():
    name = input("Enter your name: ")
    issue = input("Enter your complaint: ")

    complaint = {
        "id": len(complaints) + 1,
        "name": name,
        "issue": issue,
        "status": "Pending"
    }

    complaints.append(complaint)
    print("✅ Complaint submitted successfully!\n")


def view_complaints():
    if not complaints:
        print("No complaints found.\n")
        return

    print("\n--- All Complaints ---")
    for c in complaints:
        print(f"ID: {c['id']}, Name: {c['name']}, Issue: {c['issue']}, Status: {c['status']}")
    print()


def resolve_complaint():
    view_complaints()
    cid = int(input("Enter Complaint ID to resolve: "))

    for c in complaints:
        if c["id"] == cid:
            c["status"] = "Resolved"
            print("✅ Complaint resolved!\n")
            return

    print("❌ Complaint not found!\n")


def menu():
    while True:
        print("===== Student Grievance System =====")
        print("1. Submit Complaint")
        print("2. View Complaints")
        print("3. Resolve Complaint")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            submit_complaint()
        elif choice == '2':
            view_complaints()
        elif choice == '3':
            resolve_complaint()
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid choice!\n")


# Run program
menu()