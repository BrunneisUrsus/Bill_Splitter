import random
lucky = False
lucky_one = None
friend_dict = {}
friend_list = []
i = 0
print("Enter the number of friends joining (including you):")
number_friend = int(input())
if number_friend <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    while i < number_friend:
        name = input()
        friend = {name: 0}
        friend_list.append(name)
        friend_dict.update(friend)
        i += 1
    print("Enter the total bill value:")
    bill = int(input())
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    answer = input()
    if answer == "Yes":
        lucky_one = random.choice(friend_list)
        print(f"{lucky_one} is the lucky one!")
        number_friend -= 1
        lucky = True
    elif answer == "No":
        print("No one is going to be lucky")
    payment = round(bill / number_friend, 2)
    friend_dict = {key: payment for key in friend_dict}
    if lucky:
        name = {lucky_one: 0}
        friend_dict.update(name)
    print(friend_dict)
