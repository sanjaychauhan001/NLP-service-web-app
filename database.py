import mysql.connector
import os
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
class DB:
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user=user,
                password=password,
                database='users',
                auth_plugin='mysql_native_password'
            )
            self.mycursor = self.conn.cursor()
            print("Connection established")
        except:
            print("Connection error")

    def insert_user_data(self, name, email, password):
        name = str(name)
        email = str(email)
        query = """
                SELECT email FROM users.user_information
                WHERE email = %s
                """
        self.mycursor.execute(query, (email,))
        data = self.mycursor.fetchall()
        
        if len(data) == 1:
            return 0
            
        else:
            # Using parameterized query to avoid SQL injection
            query = "INSERT INTO users.user_information (name, email, password) VALUES (%s, %s, %s)"
            values = (name, email, password)
            self.mycursor.execute(query, values)
            self.conn.commit() # Don't forget to commit the transaction after executing the query
            return 1
        
    def search_user_data(self,email,password):
            
            email = str(email)
            query = """
                SELECT * FROM users.user_information
                WHERE email = %s
                """
            self.mycursor.execute(query, (email,))
            data = self.mycursor.fetchall()
            if len(data) == 1:
                if data[0][2] == password:
                    return 1
                else:
                    return 0
            else:
                return 0     
        

                