import random
def main():
    running = True
    while running == True:
        random_number = random.randrange(1,9,1)
        user_input = None
        attemp = 0
        while random_number != user_input:
            user_input = int(input("Guess the number between 1 and 9: "))
            attemp = attemp +1
            if user_input == random_number:
                print(f"Congrats, the number was {random_number}")
            else:
                print(f"Failed")
        print(f"Number of attemps:{attemp}")
        print("Do you want replay Y/N")
        user_input = input()
        if user_input == 'N':
            running = False
if __name__ == "__main__":
    main()