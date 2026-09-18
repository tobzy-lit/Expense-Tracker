
def main():
    print("=== Expenses Tracker ===")
    print("[1] Add")
    print("[2] View")
    print("[3] Total")
    print("[4] Delete")
    print("[5] Exist")

    choose = input("Enter your choose here: ")

    if choose == [1]:
        add_expenses()