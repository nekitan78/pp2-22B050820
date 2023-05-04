import psycopg2
import csv

hostname = 'localhost'
database = 'phonebook'
username = 'postgres'
pwd = '43435465niK&'
port_id = '5432'

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur = conn.cursor()

    #cur.execute("DROP TABLE contacts")

    #cur.execute("CREATE TABLE contacts (id SERIAL PRIMARY KEY, name TEXT NOT NULL, surname TEXT,  mobile TEXT)")
    #conn.commit()

except Exception as error:
    print(error)

def create(data):
    for contact in data["contacts"]:
        try:
            cur.execute("INSERT INTO contacts (name, surname, mobile) VALUES (%s,%s,%s)",(contact["name"], contact["surname"], contact["mobile"]))
        except psycopg2.OperationalError as err:
            print(err)
            return
    conn.commit()
    print("New Record added!")
    return




def read(namef):
    cur.execute(f"SELECT * FROM contacts WHERE name LIKE '{namef}%' ORDER BY name")
    res = cur.fetchall()
    if len(res) == 0:
        print("Data hasnt been found!")
        return
    for record in res:
        print(f' Name: {record[1]} \n Surname: {record[2]} \n Phone number: {record[3]} \n')
    return




def readall():
    cur.execute("SELECT * FROM contacts ORDER BY name")
    res = cur.fetchall()
    if len(res) == 0:
        print("Data hasnt been found!")
        return
    for record in res:
        print(f' Name: {record[1]} \n Surname: {record[2]} \n Phone number: {record[3]}\n')
    return




def update(namef):
    newsur = input("Enter a new surname")
    newmob = input("Enter a new mobile:")
    cur.execute("SELECT * FROM contacts WHERE name = %s",(namef,))
    res = cur.fetchall()
    for record in res:
        cur.execute("UPDATE contacts SET surname = %s WHERE surname = %s", (newsur, record[2]))
        cur.execute("UPDATE contacts SET mobile = %s WHERE mobile = %s", (newmob, record[3]))
    conn.commit()



def delete(namef):
    cur.execute("DELETE FROM contacts WHERE name = %s",(namef,))
    conn.commit()




while True:
        options = input("Select one of the options: \n Create (C) \n Read (R) \n Update (U) \n Delete (D) \n Quit (Q) \n")

        if options.lower() == "c":
            des = input("Do you want to read from file or enter by hand?(F or H)")
            if des.lower() == "h":
                new_record = {
                    "contacts": [
                        {
                            "name": input("Enter a name: "),
                            "surname": str(input("Enter your surname: ")),
                            "mobile": str(input("Enter a phone number: "))
                        }
                    ]
                }
                create(new_record)
            elif des.lower() == "f":
                data = input("Enter the  CSV file name!")
                with open(f'{data}'+'.CSV', 'r') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        cur.execute("INSERT INTO contacts (name, surname, mobile) VALUES (%s,%s,%s)",(row[0], row[1], row[2]))
                conn.commit()
                print("New Record added!")
        elif options.lower() == "r":
            des = input("do you want to read all or specific one?(Enter A or S)")
            if des.lower() == "a":
                readall()
            elif des.lower() == "s":
                name = input("Enter a name: ")
                read(name)
        elif options.lower() == "u":
            name = input("Enter a name: ")
            update(name)
        elif options.lower() == "d":
            name = input("Enter a name: ")
            delete(name)
            print("Data deleted")
        elif options.lower() == "q":
            print("Bye Bye")
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()
            quit()
        else:
            print(f"No option {options} available!")




