import pyodbc

server = 'OLGA\\MSSQLSERVER01'
database = 'yumm'

conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute("DELETE FROM Users WHERE email='kasia@mail.com'")
cursor.commit()
cursor.close()