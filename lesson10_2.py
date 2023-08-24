import random

def allnames()->list:
    name_list2 = []
    with open("names.txt", encoding="utf-8") as file:
        for line in file:
            name_list2.append(line[:3])
    return name_list2
    
print("==========命名機器人==============")

while True:
    name_list2 = allnames() 
    lastname = input("輸入你的姓氏=?")
    count = int(input("你要幾筆=?"))
    random_names = random.choices(name_list2,k=count)

    for name in random_names:
        print(lastname + name[-2:])
    
    again = input("還要繼續嗎? y or n: ")
    if again.lower() =="n":
        break
print("系統結束")
