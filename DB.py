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

    def create_table(self):
        # Template NEED FIX
        # SQL query for create table
        query = '''
            CREATE TABLE USERS(
                user_id varchar(255),
                user_name varchar(255),
                tokens int,
                primary key(user_id)
            )
        '''
        self.cur.execute(query)
        self.db.commit()


    def insert_data(self, tablename, **kwargs):
        key_args = ','.join(kwargs.keys())
        val_args = ",'".join(kwargs.values())
        # NEED FIX: if different datatype, value may need to ''
        exec = "INSERT INTO {}({}) values('{}'); ".format(tablename,key_args,val_args)
        # print(exec)
        self.cur.execute(exec)
        self.db.commit()

    def select_first(self,tablename):
        # NEED FIX:
        exec = "Select * from {} ".format(tablename)
        res = self.cur.execute(exec).fetchone()
        if res:
            res = res[0]
        return res


    # def add_token(db, cur,user_id, tokens):
    #     # select current left tokens
    #     exec = "Select tokens from users where user_id = '{}'".format(user_id)
    #     res = cur.execute(exec).fetchone()
    #     if res:
    #         res = res[0]
    #     update_exec = "Update users set tokens={} where user_id ='{}'".format(res+int(tokens), user_id)
        
    #     try:
    #         cur.execute(update_exec)
    #         db.commit()
    #         return "Successfully Update"
    #     except Exception as e: 
    #         return e

    #     # then add
