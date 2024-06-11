import pyodbc

'--------------------------DODANIE PRZEPISU -------------------------------------'
def AddRecipe(title, category, author, ingredients, instructions, server='OLGA\MSSQLSERVER01', database='yumm'):

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO Recipes (TITLE, CATEGORY, AUTHOR, INGREDIENTS, INSTRUCTIONS) VALUES (?, ?, ?, ?, ?)",
                   (title, category, author, ingredients, instructions))


    conn.commit()


    cursor.close()
    conn.close()

    print("Przepis został dodany do tabeli Recipes.")


# Dane przepisu
title = input('Podaj tytuł przepisu: ')
category = input('Podaj kategorię: ')
author = input('Podaj autora przepisu: ')
ingredients = input('Podaj składniki: ')
instructions = input('Podaj instrukcję: ')



