
def calc_total():
    sum = 0
    num_list = []
    num = 0
    while num < 5:
        num_list.append(int(input("Enter a number: ")))
        num += 1
    for num in num_list:
        sum += num
    print(sum)

calc_total()
