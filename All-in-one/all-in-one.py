def calculator():
    while True:

        x = int(input(" enter a number: "))
        y = int(input(" enter another number: "))
        print(" what do you want to do? ")
        print(" 1. Add ")
        print(" 2. Subtract ")
        print(" 3. Multiply ")
        print(" 4. Divide ")
        print(" 5. Exit")
        choice = int(input(" enter your choice: "))

        if choice == 1:

            print(" the sum is: ", x + y)

        elif choice == 2:
        

            print(" the difference is: ", x - y)

        elif choice == 3:

            print(" the product is: ", x * y)

        elif choice == 4:

            print(" the quotient is: ", x / y)

        elif choice == 5:

            print(" exiting...\n")
            return choices()

        else:
            print(" invalid choice ")
            

def to_do_random():

    import random
    tasks = [" do laundry ", " clean the house ", " go shopping ", " cook food ", " play games "]
    print("you should " + random.choice(tasks) + "!")
    return choices()

def financial_tips():

    import random
    
    salary =[]

    food =[]

    bealty_products =[]

    other_things =[]

    salary.append(int(input("what is your salary? ")))
    food.append(int(input("how much do you spend on food? ")))
    bealty_products.append(int(input("how much do you spend on bealty products? ")))
    other_things.append(int(input("how much do you spend on other things? ")))

    debt = food[0] + bealty_products[0] + other_things[0]

    

    

    if debt>salary[0]:

        if bealty_products>food:
            
            print("your debts are very high, maybe you shold reconsider what you spend on bealty products! ")
            return choices()

        elif other_things>food:

             print("your debts are very high, maybe you shold stop buying unecessary things!")
             return choices()

        elif food<bealty_products and other_things:

            print("you shold really stop buying unessary things! your salary can't pay all your debts! ")
            return choices()
        else:
            print("your debts are higher than your salary! maybe you shoud cut your general spences?")
            return choices()

    elif salary[0]>1.5* debt:
        print("great work! your finacial situation is quite stable, with this income you can spend more on " + random.choice(["general things","bealty products","something you want"]) )
        return choices()
    else:

        print("you're doing fine! keep up the good work !")
        return choices()

def play():
        
        import random

        print(f"you're bored right {name}? then let's play rock, paper, scisors!\n ")


        print("1. rock")
        print("2. paper")
        print("3. scisors\n")
            
        pl= int(input("What do you choose? "))

        op= random.randint(1,3)

        if pl == 1 and op == 3 or pl == 2 and op ==1 or pl == 2 and op == 2 :

            print(f"you win {name}!\n ")

            cmd = str(input("try again? y/n : "))

            if cmd == "y":

                return play()
            elif cmd == "n":

             return choices()    
        
        else:

            print(f"you lose {name}!")

            cmd = str(input("try again? y/n? : "))

            if cmd == "y":

                return play()
            
            elif  cmd == "n":

                return choices()
            
            else  :

                ValueError
                return choices()
                
                
                
               


def choices ():  

 print(f"what do you want to do {name}?\n")

 print("1. calculator")
 print("2. financial advisor")
 print("3. to-do-list")
 print("4. play a game\n")

 alt= int(input())



 if alt == 1:

     return calculator()

 elif alt == 2:
    
     return financial_tips()

 elif alt == 3:

    return to_do_random()
    

 elif alt == 4:

    return play()

 else:

    print("please, choose a number among the options\n")
    return choices()

#the code starts here

name=str(input("what is your name? "))

choices()


    








