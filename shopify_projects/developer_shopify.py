import mysql.connector

def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insert_blob(emp_id, name, biodata_file):