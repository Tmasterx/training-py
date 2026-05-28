import random

 
   

name = str(input("What is your name?\n"))
    
print(f"Hello, {name}! you look like you could do something.")

print(f" are you free, {name}? like, for at least a day?\n")


number = int(input("pick a number between 1 and 10: "))
 
if number < 1 or number > 10:
        print("Invalid input. Please pick a number between 1 and 10.")
        
elif number >= 1 and number <= 3:
        option_a = random.choice(["run for ","spar for ","play games for "])
        option_b = random.randint(1, 24)
        option_c = random.choice(["minutes", "hours", "seconds"])

        print(f"You should {option_a} {option_b} {option_c} {name}!")

elif number >= 4 and number <= 7:
        option_a = random.choice(["study for ","exercise for ", "sleep for "])
        option_b = random.randint(1, 24)
        option_c = random.choice(["minutes", "hours", "seconds"])

        print(f"You should {option_a} {option_b} {option_c} {name}!")

else:
        option_a = random.choice(["read for ", "write for ", "think for "])
        option_b = random.randint(1, 24)
        option_c = random.choice(["minutes", "hours", "seconds"])

        print(f"You should {option_a} {option_b} {option_c} {name}!")





