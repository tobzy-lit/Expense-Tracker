
expenses = []

def add_expenses():

    """
    This functon use to add every expense together. 
    Ask user for their amount, category and description they like to add into expenses tracker. 
    """
    while True:
        try:
            amount = float(input("Enter amount here : "))
        except:
            print("Your input must be amount")
            continue
        else:
            break
    

    category = input("Enter category here : ")
    description = input("Enter description here : ")

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
    loop through the expenses and get their value not index.
    """
    for exp in expenses:
       amount = exp["amount"]
       category = exp["category"]
       description = exp["description"]
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
    print(f" your total amount is #{total:.2f}")


def delete_expenses():
    """
    This function handle deleting of any expense form the expenses,
    that does not neccessary useful again or you feel like you don't need it anymore in your expenses tracker.
    """

    "check if expenses not exit in the tracker. if there's the program should return and print out the message. "
    if not expenses: 
        print("Expenses is not exit ")
        return 

    delete_expense = int(input("Select the number you want to delete?: "))

    "htis is to check validation "
    if delete_expense < 1 or delete_expense > len(expenses):
        print("invalid!")
        return
    
    "convert user number to python relating index number, then delete the expense and print 'deleted was successfully!'."
    delete_expense -= 1
    expenses.pop(delete_expense)
    print("delete was successful!")
