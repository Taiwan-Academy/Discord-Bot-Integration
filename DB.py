import sqlite3
from Singleton import Singleton


class DB(metaclass=Singleton):
    def __init__(self):
        # Since, by far we plan to have only one database
        # Not providing flexibility to access different db
        db_name = 'data.sqlite'
        try:
            self.db = sqlite3.connect(db_name)
            self.cur = self.db.cursor()
            print('Successfully connect to DB')
        except Exception as e:
            print("Fail connection to DB")
            raise e
    
    def create_university(self, univ_info: list):
        try:
            univ_info = [univ_info] if not isinstance(univ_info, list) else univ_info
            query = """INSERT INTO UNIVERSITY
                            (univ_abbrev, univ_name, region) 
                            VALUES (?, ?, ?);"""

            self.cur.executemany(query, univ_info)
            self.db.commit()
            print("Successfully create University")
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        

    def delete_university(self, univ_id):
        try:
            query = 'DELETE from UNIVERSITY WHERE univ_id = ?'; 
            self.cur.executemany(query, univ_id)
            self.db.commit()
            print("Successfully DELETE University")
                    
        except sqlite3.Error as error:
            print("Failed to DELETE Python variable from sqlite table", error)

    def delete_user(self, user_id):
        try:
            query = 'DELETE from USER WHERE user_id = ?'; 
            self.cur.executemany(query, user_id)
            self.db.commit()
            print("Successfully DELETE USER")
        except sqlite3.Error as error:
            print("Failed to DELETE Python variable from sqlite table", error)



    def create_user(self, user_id:str, user_name:str):
        try:
            query = """INSERT INTO USER
                            (user_id, user_name) 
                            VALUES (?, ?);"""

            data_tuple = (user_id, user_name)
            self.cur.execute(query, data_tuple)
            self.db.commit()
            print("Successfully create User")
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)

    def update_user_info(self, user_id:str, updated_info: dict): 
        # updated_info should be a dictionary contain the updated attribute and value
        # NOTE: the key should match the attributes name
        # {
        #     'prog_name' : "Computer Science",
        #     'prog_deg' : "Master",
        #     'univ_abbrev' : 'UCI'
        # }

        try:
            cols = ', '.join('{}=:{}'.format(col, col) for col in updated_info.keys())
            updated_info['user_id'] = user_id
            query = """UPDATE USER
                        SET {}
                        WHERE USER_ID=:user_id;""".format(cols)
            # print(query)
            self.cur.execute(query, updated_info)
            self.db.commit()
            print("Successfully Update User Info : {}".format(updated_info.keys()))

        except sqlite3.Error as error:
            print("Failed to update Python variable into sqlite table", error)

    def select_all(self,tablename):
        try:
            # NOTE: table names cannot be parametrized. May be Vulnerable to Injection?
            exec = "select * from {};".format(tablename)
            res = self.cur.execute(exec).fetchall()
            return res
            
        except sqlite3.Error as error:
            print("Failed to select from table", error)
        
    def select_where_eql(self, tablename, condition: dict):
        try:
            eql_condition = ' and '.join('{}=:{}'.format(col, col) for col in condition.keys())
            condition['tablename'] = tablename
            # NOTE: table names cannot be parametrized. May be Vulnerable to Injection?
            exec = "Select * from {} where {}".format(tablename,eql_condition)
            res = self.cur.execute(exec, condition).fetchall()
            return res
            
        except sqlite3.Error as error:
            print("Failed to select from table", error)

