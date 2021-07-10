import random
def letters():
    letters = ["a", "e", "i", "o", "u",
               "ka", "ke", "ki", "ko", "ku"
              ]
    print(letters[random.randint(0, len(letters) - 1)])

def main():
    answer = ""
    print("-------------------------\nEnter 'q' to quit\n-------------------------\n")
    while answer != "q":
        letters()
        answer = input()

main()
