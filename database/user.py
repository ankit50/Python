import psycopg2
#Creating Connection To The Database
def connection():
		cursor = None
		conn = None
		try:
			conn = psycopg2.connect(dbname='Student', user="postgres", password="root")
			cursor = conn.cursor()
		except Exception :
			print("Couldn't Connect to database!!!")

		return cursor, conn

#Fetching Record From Database Using Id
def viewRecord():
	try:
		cursor, conn = connection()
		ID = int(input("Enter The Student ID:"))
		query = 'SELECT *FROM personal_records WHERE "ID" = %s'
		cursor.execute(query, (ID,))
		details = cursor.fetchall()
		for row in details:
			print("---------------------------------------")
			print("ID:{}".format(row[ 0 ]))
			print("Student Name:{} {}".format(row[ 1 ], row[ 2 ]))
			print("Phone:{}".format(row[ 3 ]))
			print("Gender:{}".format(row[ 4 ]))
			print("Address:{}".format(row[ 5 ]))
	except Exception:
		print("Id value not Found In Database.Please Enter A Valid Id Number.")
	finally:
		cursor.close()

#Inserting Record To the Database
def insertRecord():
	try:
		cursor, conn = connection()
		Id = int(input("Enter Id:"))
		fname = input("Enter First Name:")
		lname = input("Enter Last Name:")
		phone = int(input("Enter Phone Number:"))
		gen = input("Enter Gender:")
		add = input("Enter Address:")
		query1 = "INSERT INTO personal_records VALUES(%s, %s, %s, %s, %s, %s)"
		record_to_insert = (Id, fname, lname, phone, gen, add)
		cursor.execute(query1, record_to_insert)
		conn.commit()
		print("Record Inserted Successfully!!!")
	except Exception:
		print("Error!!!!")
	finally:
		cursor.close()

if __name__=="__main__":
	while True:
		print("---------------------------------------")
		print("1.View Record\n2.Add Record\n3.Exit")
		Choice = int(input("Enter Your Choice:"))
		if Choice == 1:
			#Fetching Row From Database Using ID
			viewRecord()

		elif Choice == 2:
			insertRecord()

		elif Choice == 3:
			cursor, conn = connection()
			cursor.close()
			conn.close()
			break