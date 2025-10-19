import random
secret_number = random.randint(1,100) # System will random select a number in  between 1 to 100

guess = int(input("Guess a number :"))
guess_count = 0
while guess != secret_number:  # LOOP WILL FINFISHED WHEN GUESS NO IS SAME AS SECRET NNUMBER

    if guess < (secret_number-10):
# Give hint for users 
        print(f"Too low, Guess in range of ({secret_number-10,secret_number+10})")
    elif guess > (secret_number+10):
        print(f"Too High, Guess in range of ({secret_number-10,secret_number+10})")
    elif (secret_number-10) < guess < (secret_number+10):
        if guess > secret_number:
            print(f"Too Close, But try to guess less than {guess}") 
        elif guess < secret_number:
            print(f"Too Close, But try to guess greater number than {guess}")
    guess_count += 1
#update guess after each iteration to guess it correctly
    guess = int(input("Nope, Try to guess again follwed by hint"))
if guess == secret_number:
    guess_count += 1
print(f"You got it! The secret number was {secret_number} in {guess_count} times . 🎉")