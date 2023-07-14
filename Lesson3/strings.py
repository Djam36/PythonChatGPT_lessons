print("Конкотеннация строк:")
str1 = "Hi "
result = str1 * 3
print(result + "\n")  # Output: Hi Hi Hi

print("Пример умножения строк:")
str1 = "Hello"
print(str1[0])  # Output: H
print(str1[1] + "\n")  # Output: e


print("Методы строк")
str1 = "hello world"
print(str1.upper())  # Output: HELLO WORLD
print(str1.lower())  # Output: hello world
print(str1.capitalize() + "\n")  # Output: Hello world

print("Методы для поиска подстроки (find, index, count)")
str1 = "Hello world"
print(str1.find("world"))  # Output: 6
print(str1.index("world"))  # Output: 6
print(str1.count("o" + "\n"))  # Output: 2


print("\n"+"Методы для замены подстроки (replace)")
str1 = "Hello world"
new_str = str1.replace("world", "python")
print(new_str + "\n")  # Output: Hello python

print("Методы для разделения строки (split)")
str1 = "Hello. my name is Edya"
result = str1.split(", ")
print(result)  # Output: ['Hello', 'my name is Edya']