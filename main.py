import expenses
def main():
    while True:
        print("=" * 30)
        print(" Expenses Tracker ")
        print("=" * 30)
        print("[1] add expenses")
        print("[2] view expenses")
        print("[3] total expenses")
        print("[4] delete expense")
        print("[5] exit")

        choice = int(input("Enter your activities here: "))

        if choice == 1:
            expenses.add_expenses()
        elif choice == 2:
            expenses.view_expenses()
        elif choice == 3:
            expenses.calculate_total()
        elif choice == 4:
            expenses.delete_expenses()
        elif choice == 5:
            break
        else:
            print("invalid choice selected!")


        
main()