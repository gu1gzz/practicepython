import random

def main():
    randomlist1 = set(random.sample(range(10,30),5))
    randomlist2 = set(random.sample(range(10,30),8))
    new_list = randomlist1 | randomlist2
    print(f"Randomlist1 = {randomlist1}")
    print(f"Randomlist2 = {randomlist2}")
    print(f"NewList = {new_list}")

if __name__ == "__main__":
    main()

    