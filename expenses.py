
expenses = []

def add_expenses():

    amount = float(input("Enter amount here : "))
    category = input("Enter category here : ")
    description = input("Enter description here : ")

    expense = {
        "amount": amount,
        "category" : category,
        "description" : description
    }
    expenses.append(expense)
add_expenses()

def view_expenses():
    for exp in expenses:
       amount = exp["amount"]
       category = exp["category"]
       description = exp["description"]
       print("amount:", amount)
       print("category:", category)
       print("description:", description)
view_expenses()

def calculate_total():
    total = 0

    for expense in expenses:
        amount = expense["amount"]
        total += amount
        print(total)
calculate_total()

def delete_expenses():
    """
    This function handle deleting of any expense form the expenses, that does not neccessary useful again in your expenses tracker.

    """
    if not expenses:
        print("Expenses is not exit ")
        return 
    delete_expense = int(input("Select the number you want to delete?: "))

    if delete_expense < 1 or delete_expense > len(expenses):
        print("invalid!")
        return
    
    delete_expense -= 1
    expenses.pop(delete_expense)
    print("deleted was successful!")

delete_expenses()


def exit_expenses():
    pass
