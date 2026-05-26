import random

food=[]

beauty=[]

cleaning=[]

other_things =[]

salary=[int(input("What is your salary? "))]

food.append(int(input("How much did you spend on food? ")))

beauty.append(int(input("How much did you spend on beauty products? ")))

cleaning.append(int(input("How much did you spend on cleaning supplies? ")))

other_things.append(int(input("How much did you spend on other things? ")))

total_expenses = food[0] + beauty[0] + cleaning[0] + other_things[0]

def reduce_expenses(category, amount):
            print(f"You spent $ {amount} on {category}, which is a large expense compared to essentials. You should consider reducing your expenses in this category.")


if total_expenses > salary[0]:

    if beauty[0] > food[0] or cleaning[0]:

        reduce_expenses("beauty products", beauty[0])

    elif other_things[0] > food[0] or cleaning[0]:

        reduce_expenses("other things", other_things[0])

    else:
          print("Your expenses are mostly on essentials, which is good. However, you should still try to reduce your overall expenses to avoid financial stress.")

elif salary[0] > 1.8 * total_expenses:
      
      print("your expenses are well within your salary, which is great! which means you can spend more on " + random.choice(["beauty products", "other things"]) + " if you want to, but make sure to save some money for emergencies and future goals.")
    
else:
      print("your expenses are within your salary, which is good. However, you should still try to reduce your overall expenses to save more money for emergencies and future goals.")
