def txt():
    while True:
        try:
            choice = float(input("Enter your amount here :"))
            
        except:
            print("Your input must be amount ")
            continue
        else:
            print(f"your amount is #{choice:.2f}") 
            break       
txt()