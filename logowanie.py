import pyodbc
from classes import User, PremiumUser, Admin, SuperAdmin

def login(email, password, server, database):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute("SELECT email, name, surname, password, premium, favourites FROM Users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user:
        if user[3] == password:  # Sprawdzanie hasła na podstawie indeksu kolumny
            print('Logowanie poprawne')
            email, name, surname, _, premium, favourites = user
            if premium:
                return PremiumUser(email, name, surname, favourites)
            else:
                return User(email, name, surname)
        else:
            print("Logowanie nieudane")
            return None

    cursor.execute("SELECT email, name, surname, password, superAdmin FROM Admins WHERE email = ?", (email,))
    admin = cursor.fetchone()

    if admin:
        if admin[3] == password:
            email, name, surname, _, superAdmin = admin
            print("Logowanie poprawne")
            if superAdmin:
                return SuperAdmin(email, name, surname, superAdmin)
            else:
                return Admin(email, name, surname)

    print("Logowanie nieudane")
    return None

    cursor.close()
    conn.close()
