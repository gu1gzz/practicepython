def main():

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    age_100_years_old = 2024 - age + 100
    message =(f"Hey {name},\nyou turn 100 years old in {age_100_years_old}\n")
    print(message)
    number_of_print = int(input("Please enter a number: "))
    for i in range (number_of_print):
        print(message)

main()