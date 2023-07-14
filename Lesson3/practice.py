print("""Задача 1 Практическое задание:
3.1. Создание списка из нескольких имен
3.2. Вывод каждого имени на отдельной строке """)

names = ["Evgeniy", "Alexandr", "Maks", "Pavel"]
for i in names:
    print(i)
print(names)

print("Реализовать функцию, которая принимает строковый аргумент и возвращает список всех слов в строке")
def split_string(str1):
    result = str1.split(" ")
    return result
print(split_string("Hello my followers on Twitch"))

print("Реализовать функцию, которая принимает список и возвращает новый список, содержащий только уникальные элементы исходного списка")
def uniq_index(str1):
    getlist = str1.split(" ")
    result = list(set(getlist))
    return result
print(uniq_index("Hello my followers on Twitch followers"))



print("Реализовать функцию, которая принимает список и выводит на экран количество повторяющихся элементов в списке")
my_list = [1, 2, 3, 2, 4, 5, 1, 5]
def repeat_index(mylist):
    count_dict = {}
    for item in my_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

print(repeat_index(my_list))