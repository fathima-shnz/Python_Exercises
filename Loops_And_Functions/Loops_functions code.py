#number guessing game
import random
number = random.randint(1,10)

print("Guess a number between 1 and 10")
print("You have 3 attempts")
attempt = 0

while attempt < 3:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You have won.")
        break
    elif guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10")
        continue
    attempt += 1
    if guess > number:
        print("Try a lower number")
    else:
        print("Try a higher number")
    if attempt == 3:

        print(f"You've lost the game. The number was {number}")


#multiplication table generator
num = int(input("Enter number for multiplication table: "))
for i in range(1,11):
    product = num * i
    print (f"{num} x {i} = {product}")
    
           

#function
def calculate_bmi():
    weight = float(input("Enter weight in kg "))
    height = float(input("Enter height in m "))
    return weight / (height * height)

bmi = calculate_bmi()
print(f"Your bmi is {bmi:.2f}")







