import expenses


def main():

    expenses.expenses = expenses.load_expenses()



    while True:
        print("=" * 30)
        print(" Expenses Tracker ")
        print("=" * 30)
        print("[1] add expenses")
        print("[2] view expenses")
        print("[3] total expenses")
        print("[4] delete expense")
        print("[5] search expenses by category")
        print("[6] exit")

        try :
            choice = int(input("Enter your activities here: "))
            if choice < 1 or choice > 6:
                print("invalid! ")
                continue
        except ValueError:
            print("Invalid choice! choice must be between (1-6)")
            continue



        if choice == 1:
            expenses.add_expenses()

            expenses.save_expenses(expenses.expenses)
        elif choice == 2:
            print("`" * 30)
            expenses.view_expenses()
        elif choice == 3:
            print("-" * 30)
            print(f"Total : #{expenses.calculate_total():.2f}")
        elif choice == 4:
            expenses.delete_expenses()
            expenses.save_expenses(expenses.expenses)
        elif choice == 5:
            category = input("enter category you want to search here: ").strip().lower()
            print("*" * 30)
            expenses.find_the_expenses_by_category(category)
        elif choice == 6:
            break
        else:
            print("invalid choice selected!")


main()
