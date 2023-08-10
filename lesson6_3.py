import random
min = 1
max = 100
num = 0
target = random.randint(min, max)

print("=========Guess Number Game==========")

while True:
    guess = int(input(f"Enter a guess number between {min}~{max}:"))
    num += 1
    if num < 10:
        if guess >= min and guess <= max:
            if guess == target:
                    print(f"Bingo!!!! The number is {target}")
                    print(f"You've guessed {num} times. Game Over.")
                    break
            elif guess > target:
                    print("Make it Smaller")
                    max = guess + 1
            else:
                    print("Make it Bigger")
                    min = guess - 1
                
        else:
                print("Entered value not in range")
    else:
          print("You've guess 5 times. Game Over")
          break