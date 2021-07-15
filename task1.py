'''
Given the Department and Company tables. Write a python code to query the sum of the Employees of all
Department where the Country is 'India’.

Suppose you have a database “Company_details”. Assume hostname = “hostname”, username = “abed”,
and password = “password”.
Note: Department.Company_code and Company.Code are matching key columns.
'''


import psycopg2

def create_tables():
    try:
        # Create tables in the PostgreSQL database
        cur.execute('''CREATE TABLE Department
            (ID           INT    NOT NULL,
            NAME            VARCHAR(50),
            COMPANY_CODE        VARCHAR(50),
            TOTAL_EMPLOYEES         INT);''')

        cur.execute('''CREATE TABLE Company
            (CODE           VARCHAR(50)    NOT NULL,
            NAME            VARCHAR(50),
            COUNTRY        VARCHAR(50),
            TOTAL_EMPLOYEES         INT);''')

        # Insert rows into the table
        L1=[("1","EnT","A101","100"),("2","SSS","B102","110"),("3","MnC","C103","120"),("4","BS","D104","130"),("5","MnC","E105","140")]
        L2=[("A101","GOOGLE","India","500"),("B102","MICROSOFT","Australia","1000"),("C103","GOOGLE","India","250"),("D104","MICROSOFT","Australia","500"),("101","KPMG","Netherlands","100")]

        cur.executemany("INSERT INTO Department (ID,NAME,COMPANY_CODE,TOTAL_EMPLOYEES) VALUES (%s,%s,%s,%s)", L1)
        
        cur.executemany("INSERT INTO Company (CODE,NAME,COUNTRY,TOTAL_EMPLOYEES) VALUES (%s,%s,%s,%s)", L2)

    # Printing any error if occured
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# Connect to the PostgreSQL server
conn = psycopg2.connect(database = "Company_details", user = "abed", password = "password", host = "hostname", port = "5432")

# Create a cursor
cur = conn.cursor()

# Excecuting the query to get the desired output
cur.execute("SELECT SUM(Department.TOTAL_EMPLOYEES) FROM Department INNER JOIN Company ON Department.COMPANY_CODE=Company.CODE WHERE Company.COUNTRY = 'India'")
# Fetching the result
rows = cur.fetchall()
print(rows[0][0])

# Close communication with the PostgreSQL database server
cur.close()
# Commit the changes
conn.commit()
# Close the connection
conn.close()