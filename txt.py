# def txt():
#     while True:
#         try:
#             choice = float(input("Enter your amount here :"))
            
#         except:
#             print("Your input must be amount ")
#             continue
#         else:
#             print(f"your amount is #{choice:.2f}") 
#             break       
# txt()

def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file , indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []