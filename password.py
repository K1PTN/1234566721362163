a = input("Введите пароль")
b = input("Подтвердите пароль")
if a == b and len(a)>=5:
    print("Пароль совпадает")
elif a == b and len(a)<5:
    print("Пароль Короткий")
elif a != b:
    print("Пароль не совпадает")





