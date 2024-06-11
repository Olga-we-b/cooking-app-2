import pyodbc

server = 'OLGA\\MSSQLSERVER01'
database = 'yumm'
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;'
class User:

    def __init__(self, email, name, surname):
        self.id = email
        self.name = name
        self.surname = surname
        self.category = 'User'

    def __str__(self):
        return f"User(ID={self.id}, Name={self.name}, Surname={self.surname}, Category={self.category})"

    def wyszukaj_przepis(self, sever, database, title):
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            srch_qry = "SELECT * FROM Recipes WHERE TITLE LIKE ?"
            cursor.execute(srch_qry, '%' + title + '%')
            rows = cursor.fetchall()
            cursor.close()

            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Błąd wykonania zapytania: ", e)
        finally:
            conn.close()

    def wyszukaj_autora(self, sever, database, author):
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            srch_qry = "SELECT * FROM Recipes WHERE AUTHOR LIKE ?"
            cursor.execute(srch_qry, '%' + author + '%')
            rows = cursor.fetchall()
            cursor.close()

            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Błąd wykonania zapytania: ", e)
        finally:
            conn.close()

    def wyszukaj_kategorie(self, sever, database, category):
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            srch_qry = "SELECT * FROM Recipes WHERE CATEGORY LIKE ?"
            cursor.execute(srch_qry, '%' + category + '%')
            rows = cursor.fetchall()
            cursor.close()

            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Błąd wykonania zapytania: ", e)
        finally:
            conn.close()

class PremiumUser(User):
    def __init__(self, email, name, surname, favourites):
        super().__init__(email, name, surname)
        self.category = 'PremiumUser'
        self.favourites = favourites if favourites else []

    def add_favourite(self, recipe_id):
        pass
    def __str__(self):
        return f"PremiumUser(ID={self.id}, Name={self.name}, Surname={self.surname}, Category={self.category}, Favourites={self.favourites})"

class Admin(User):
    def __init__(self, email, name, surname):
        super().__init__(email, name, surname)
        self.category = 'Admin'

    def dodaj_przepis(self, recipe, server, database):
        conn = pyodbc.connect(
           f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Recipes (TITLE, CATEGORY, AUTHOR, INGREDIENTS, INSTRUCTIONS) VALUES (?, ?, ?, ?, ?)",
            (recipe.title, recipe.category, recipe.author, recipe.ingredients, recipe.instructions))
        conn.commit()
        cursor.close()
        conn.close()
        print("Przepis został dodany do tabeli")

    def usun_uzytkownika(self, user_email, server, database):
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Users WHERE email=?', user_email)
        conn.commit()
        conn.close()
        print(f"Użytkownik {user_email} został usunięty")


    def dodaj_uzytkownika(self, server, database, user_email, password, user_name, user_surname, premium):
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO Users (email, password, name, surname, premium) VALUES (?, ?, ?, ?, ?)',
                           user_email, password, user_name, user_surname, premium)
            conn.commit()
        except pyodbc.Error as e:
            print("Błąd wykonania zapytania: ", e)
        finally:
            conn.close()

        print(f'Użytkownik {user_name} {user_surname} został dodany do bazy')

    def przegladaj_uzytkowników(self, server, database):
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;')
        try:
            ser_qry = "SELECT * FROM Users"
            cursor = conn.cursor()
            cursor.execute(ser_qry)
            rows = cursor.fetchall()
            cursor.close()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Błąd wykonania zapytania: ", e)
        finally:
            conn.close()


    def __str__(self):
        return f"Admin(ID={self.id}, Name={self.name}, Surname={self.surname}, Category={self.category})"

class SuperAdmin(Admin):
    def __init__(self, email, name, surname, superAdmin):
        super().__init__(email, name, surname)
        self.category = 'SuperAdmin'
        self.superAdmin = superAdmin

    def nadac_uprawnienia_admina(self, user_email):
        # Implementacja nadawania uprawnień admina
        pass

    def nadac_uprawnienia_superadmina(self, admin_email):
        # Implementacja nadawania uprawnień superadmina
        pass

    def __str__(self):
        return f"SuperAdmin(ID={self.id}, Name={self.name}, Surname={self.surname}, Category={self.category}, SuperAdmin={self.superAdmin})"

class Przepis:
    def __init__(self, title, category, author, ingredients, instructions):
        self.title = title
        self.category = category
        self.author = author
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Przepis(Title={self.title}, Category={self.category}, Author={self.author}, Ingredients={self.ingredients}, Instructions={self.instructions})"

