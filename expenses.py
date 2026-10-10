import json


expenses = []

def add_expenses():

    """
    This functon use to add every expense together.
    Ask user for their amount, category and description they like to add into expenses tracker.
    """
    while True:
        try:
            amount = float(input("Enter amount here : "))
            if 0 >= amount:
                print("Invalid process!. amount must be above (0)")
                continue

        except ValueError:
            print("Your input must be amount")
        else:
            break


    while True:
        try:
            category = input("Enter category here : ").strip()
            if category == "":
                continue
        except ValueError:
            print("your category must be in words!")
            continue
        else:
            break


    while True:
        try:
            description = input("Enter description here : ").strip()
            if description == "":
                continue
        except ValueError:
            print("your description must be in words!")
            continue
        else:
            break

    "Dictionary to handle the data structure and add expense into expenses tracker."
    expense = {
        "amount": amount,
        "category" : category,
        "description" : description
    }
    expenses.append(expense)

def view_expenses():
    """
    This function show the user what they have in there expenses tracker.
    loop through the expenses and import json
# import os get their value not index.
    """
    if not expenses:
        print("expenses is not exist yet!")
        return
    for index, exp in enumerate(expenses, start=1):
        # print("----- Your Expenses category are: -----")

        amount = exp["amount"]
        category = exp["category"]
        description = exp["description"]

        print("-" * 30)
        print(f"Expense: #{(index)}")
        print("amount:", amount)
        print("category:", category)
        print("description:", description)


def calculate_total():
    """
    This function handle total expenses. programmically go through every expense in an expenses tracker
    and look for amount, add all the amount together and let the user know their total amount.
    """
    total = 0

    for expense in expenses:
        amount = expense["amount"]
        total += amount
    return total

def find_the_expenses_by_category(category):
    match_expenses = []
    total = 0
    found_match = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            match_expenses.append(expense)
            total += expense["amount"]
            found_match = True

    if found_match == True:
        print(f"All matching expenses : {match_expenses}")
        print(f"Total: #{total}")

    else:
        print("Category was not found!")




def delete_expenses():
    """
    This function handle deleting of any expense form the expenses,
    that does not neccessary useful again or you feel like you don't need it anymore in your expenses tracker.
    """

    "check if expenses not exit in the tracker. if there's the program should return and print out the message. "
    if not expenses:
        print("Expenses not found! ")
        return

    view_expenses()
    while True:
        try:
            delete_expense = int(input("Select the number you want to delete?: "))
            if delete_expense < 1 or delete_expense > len(expenses):
                print(f"You selection must be bewteen 1 - {len(expenses)}")
                continue
        except ValueError:
            print("invalid! input. the delete must be number. ")
        else:
            break




    "htis is to check validation "
    if delete_expense < 1 or delete_expense > len(expenses):
        print(f"invalid seletion!, you currently have {len(expenses)} expenses.")
        return

    "convert user number to python relating index number, then delete the expense and print 'deleted was successfully!'."
    delete_expense -= 1
    while True:
        delete_request = input("Are you sure you want to delete this? YES/NO ").upper()

        if delete_request == "YES":
            break
        elif delete_request == "NO":
            print("Deletion cancelled. Your expense was not removed.")
            return
        else:
            print("Your seletion must be Yes/No")


    expenses.pop(delete_expense )
    print(f"Expense {[delete_expense + 1] } delete was successful!")

def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try :
        with open("expenses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []