import json

answers = []
user = {}

survey = [
    "What is your name?",
    "How old are you?",
    "What is your favorite color?"
]

key = ["name", "age", "color"]

done = "NO"
while done == "NO":
    for x in range(len(survey)):
        response = input(survey[x] + ": ")
        user[key[x]] = response
    answers.append(user)
    done = input("Are you done collecting data?: ").upper()
    # if done == "NO":
    #     edit = input("Would you like to edit your responses?: ")
    #     if edit == "yes":
    #         print(user)
    #         choice = int(input("Choose index number of response to change: "))
    #         new_answer = input("Enter new answer: ")
    #         user[key[choice]] = new_answer
    #         print(user)
    #         done = "NO"
    user = {}

file = open("user-responses.json", "r")
olddata = json.load(file)

answers.extend(olddata)
print(answers)
file.close()

file = open("user-responses.json", "w")
file.write("[\n")

counter = 0
for obj in answers:
    if counter < (len(answers)-1):
        json.dump(obj, file)
        file.write(",\n")
    else:
        json.dump(obj, file)
        file.write("\n")
    counter += 1

file.write("]")
file.close()
