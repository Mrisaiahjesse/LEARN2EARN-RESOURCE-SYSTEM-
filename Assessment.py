resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
loans = []


def find_resource(rid):
    for r in resources:
        if r["id"].upper() == rid.upper():
            return r


def quantity():
    while True:
        try:
            q = int(input("Quantity: "))
            if q > 0:
                return q
            print("Enter a positive number.")
        except ValueError:
            print("Enter a valid integer.")


def add_resource():
    rid = input("Resource ID: ").upper()
    if find_resource(rid):
        print("Error: ID already exists.")
        return

    name = input("Name: ")
    category = input("Category: ")
    total = quantity()

    resources.append({
        "id": rid, "name": name, "category": category,
        "total": total, "available": total
    })
    print("Resource added.")


def list_resources():
    for r in resources:
        print(r)


def borrow():
    fid = input("Fellow ID: ").upper()
    if fid not in fellows:
        print("Error: Fellow not found.")
        return

    rid = input("Resource ID: ").upper()
    r = find_resource(rid)

    if not r:
        print("Error: Resource not found.")
        return

    q = quantity()

    if q > r["available"]:
        print(f"Error: Only {r['available']} available.")
        return

    r["available"] -= q

    for loan in loans:
        if loan["fellow"] == fid and loan["resource"] == rid:
            loan["quantity"] += q
            break
    else:
        loans.append({"fellow": fid, "resource": rid, "quantity": q})

    print(f"{fellows[fid]} borrowed {q} {r['name']}(s).")
    print(f"Available: {r['available']}")


def return_item():
    fid = input("Fellow ID: ").upper()
    if fid not in fellows:
        print("Error: Fellow not found.")
        return

    rid = input("Resource ID: ").upper()
    r = find_resource(rid)

    if not r:
        print("Error: Resource not found.")
        return

    q = quantity()

    for loan in loans:
        if loan["fellow"] == fid and loan["resource"] == rid:

            if q > loan["quantity"]:
                print(f"Error: They only have {loan['quantity']} on loan.")
                return

            loan["quantity"] -= q
            r["available"] += q

            if loan["quantity"] == 0:
                loans.remove(loan)

            print(f"{q} {r['name']}(s) returned.")
            print(f"Available: {r['available']}")
            return

    print("Error: No loan found.")


def search():
    name = input("Search name: ").lower()

    found = [r for r in resources if name in r["name"].lower()]

    if found:
        for r in found:
            print(r)
    else:
        print("No resource found.")


def category():
    cat = input("Category: ").lower()

    found = [r for r in resources if r["category"].lower() == cat]

    if found:
        for r in found:
            print(r)
    else:
        print("No resources found.")


def report():
    total = sum(r["total"] for r in resources)
    available = sum(r["available"] for r in resources)
    borrowed = total - available

    low = [r for r in resources if r["available"] < 3]

    amounts = {r["id"]: r["total"] - r["available"] for r in resources}
    highest = max(amounts.values())

    leaders = [
        r["name"] for r in resources
        if amounts[r["id"]] == highest
    ]

    print("\n--- REPORT ---")
    print("Total units:", total)
    print("Available units:", available)
    print("Borrowed units:", borrowed)

    print("Low stock:")
    for r in low:
        print(f"{r['name']} ({r['available']})")

    print("Most borrowed:", ", ".join(leaders), f"({highest})")


while True:
    print("""
===== LEARN2EARN RESOURCE SYSTEM =====
1. Add resource
2. List resources
3. Borrow
4. Return
5. Search
6. Filter category
7. Report
8. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_resource()
    elif choice == "2":
        list_resources()
    elif choice == "3":
        borrow()
    elif choice == "4":
        return_item()
    elif choice == "5":
        search()
    elif choice == "6":
        category()
    elif choice == "7":
        report()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")