import mysql.connector

def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insert_blob(emp_id, name, biodata_file):
    print("Insert Blob into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost', database='python_db', user='pynative', password='pynative@#29')
        cursor = connection.cursor()
        sql_inter_blob_query = """INSERT INTO python_employee (id, name, photo, biodata) Values (%s,%s,%s,%s)"""
        emp_picture = convert_to_binary_data(photo)
        file = convert_to_binary_data(biodata_file)

        #making data into tuple format
        insert_blob_tuple = (emp_id, name, emp_picture, file)
        result = cursor.execute(sql_inter_blob_query, insert_blob_tuple)
        connection.commit()
        print("image and file inserted as a blob into the python_employee table", result)
        

