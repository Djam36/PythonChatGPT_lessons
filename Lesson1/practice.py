def input_user_name():
    print("Введи свое имя пожалуйста...")
    user_name = input("Ваше имя... ")
    return user_name


user_name = input_user_name()
print("Вас зовут: " + user_name)