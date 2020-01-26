#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:

def main():
    f = open("dictionary.txt","r")

    print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password: ")

    for word in f:
        # if test_password.strip() == word.strip():
        #     print("Found")
        # if test_password.strip() == word.strip() + "2018":
        #     print("Found")
        if word.strip() in test_password.strip():
            print("Found")
            print(word.strip())
            break


#Write logic to see if the password is in the dictionary file below here:

if __name__ == "__main__":
    main()
