import random

def get_score()->list:
    score = []
    for i in range(5):
        score.append(random.randint(50,100))
    return score


def get_names(student_nums):
    with open('names.txt', encoding='utf-8', newline='') as file:
        names_str = file.read()
        names_list = names_str.split(sep='\n')
        final_list = random.choices(names_list, k=student_nums)
        return final_list

nums_int = int(input("輸入學生人數："))
name_list = get_names(nums_int)
student = []
for i in range(nums_int):
    score = get_score()
    namescore_list = [name_list[i]] + score
    student.append(namescore_list)

print(student)
