import random

n = random.randint(1, 100)
rounds = 0

def main():
  while True:
    s = input("The number is ")

    if int(s) == n:
      rounds += 1
      print(f"GG! You won in {rounds}!")
    elif int(s) < n:
      rounds += 1
      print("The number is greater.")
    elif int(s) > n:
      rounds += 1
      print("The number is lesser.")

if __name__ == "__main__":
  main()
