import random

def main():
    randomlist1 = random.sample(range(10,30),5)
    randomlist2 = random.sample(range(10,30),8)
    new_list = set(randomlist1) & set(randomlist2)
    print(f"Randomlist1 = {randomlist1}")
    print(f"Randomlist2 = {randomlist2}")
    print(new_list)

if __name__ == "__main__":
    main()