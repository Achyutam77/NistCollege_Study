import random
random_number = random.randint(0, 100)

while True: 
    user_number = int(input("Guess a number between 0 and 100: "))
    if user_number == random_number:
        print("Congratulations! You guessed the number correctly.")
    elif user_number < random_number:
        print("Your guess is low. Try again!")
    else:
        print("Your guess is high. Try again!")

    #print("The correct number is ", random_number)