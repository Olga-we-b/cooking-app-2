from logowanie import login
from classes import User, PremiumUser, Admin, SuperAdmin, Przepis

def check_login():
    email = 'olga@mail.com'
    password = '123'
    server = 'OLGA\\MSSQLSERVER01'
    database = 'yumm'
    user_info = login(email, password, server, database)

    if user_info:
        return user_info
    else:
        print("Logowanie nieudane")
        return None

user_login_info = check_login()
admin = user_login_info
if user_login_info:
    print("Utworzono instancję użytkownika:", user_login_info)


    if isinstance(user_login_info, Admin):
        my_server = 'OLGA\\MSSQLSERVER01'
        my_base = 'yumm'
        print("co chceszz zrobić? \n 1 - dodaj przepis \n 2 - usuń użytkownika \n 3 - dodaj użytkownika \n 4 - przeglądaj użytkowników")
        answer = int(input("Podaj liczbę: "))
        if answer == 1:

            title = input("Podaj tytuł przepisu: ")
            category = input("Podaj kategorię: ")
            author = input("Podaj autora przepisu: ")
            ingredients = input("Podaj składniki: ")
            instructions = input("Podaj instrukcje: ")

            new_recipe = Przepis(title, category, author, ingredients, instructions)
            user_login_info.dodaj_przepis(new_recipe, my_server, my_base)
        elif answer == 2:
            user_email = input("Podaj maila użytkownika, którego chcesz usunąć: ")
            user_login_info.usun_uzytkownika(user_email, my_server, my_base)

        elif answer == 3:
            user_email = input('Podaj maila użytkownika: ')
            password = '123'
            user_name = input('Podaj imię użytkownika: ')
            user_surname = input('Podaj nazwisko użytkownika ')
            premium = int(input('Czy jest to użytkownik premium? 0/1'))

            admin.dodaj_uzytkownika(my_server, my_base, user_email, password, user_name, user_surname, premium)
        elif answer == 4:
            admin.przegladaj_uzytkowników(my_server, my_base)
else:
    print("Nie utworzono instancji użytkownika - logowanie nieudane")
