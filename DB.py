from sqlalchemy.sql.expression import update
from sqlalchemy.sql.functions import user
from Singleton import Singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models import University, User, Base

class DB(metaclass=Singleton):
    def __init__(self):
        self.engine = create_engine('sqlite:///data.sqlite')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_universities(self, university_list: list):
        ''' university_list : list, each element should contain
        {
            univ_abbrev : **Required**,
            univ_name : ,
            region : ,
        }

        '''

        if not isinstance(university_list, list): university_list = [university_list]

        for univ in university_list:
            try:
                new_univ = University(univ)
                self.session.add(new_univ)
                self.session.commit()
                print("Successfully Create University with {}".format(univ))

            except Exception as E:
                self.session.rollback()
                print(E)

    def add_users(self, user_list: list):
        ''' user_list should be list of user, each user should at least contain
        {
            user_id :  **Required**
            user_name :
            univ_abbrev
            prog_deg
            prog_name
            prog_start_yr
            prog_end_yr
            created_dt: **Default value: datetime.now*
            last_updated_dt
            last_updated_user
            leave_server_dt
            user_status: **Default value: Non-verified**
        }
        '''
        if not isinstance(user_list, list): user_list = [user_list]

        for user in user_list:
            try:
                new_user = User(user)
                self.session.add(new_user)
                self.session.commit()
                print("Successfully Create User with {}".format(user))
            except Exception as E:
                self.session.rollback()
                print(E)

    def get_user_by_ID(self, user_id) -> User:
        # Will return User object, can directly access its attributes ex: user.user_name
        user = self.session.query(User).filter(User.user_id == user_id).first()
        if not user:
            print("Cannot find this user")
            return None
        else:
            return user

    def get_univ_by_abbrev(self,univ_abbrev) -> University:
        univ = self.session.query(University).filter(University.univ_abbrev == univ_abbrev).first()
        if not univ:
            print("Cannot find this university")
            return None
        else:
            return univ

    def update_user_by_ID(self, user_id: int, user_info: dict):
        try:
            res = self.session.query(User)\
                        .filter(User.user_id == user_id)\
                        .update(user_info, synchronize_session=False)
            self.session.commit()
            # KEY, IF user_id wrong will not find the user, And res will be 0
            if res == 0:
                print("Warning: Such update wasn't executed, please check whether user_id is correct")
            return res
        except Exception as e:
            self.session.rollback()
            print("**Failed Update**")
            print(e)

    def update_univ_by_abbrev(self, univ_abbrev: str, univ_info:dict):
        try:
            res = self.session.query(University)\
                        .filter(University.univ_abbrev == univ_abbrev)\
                        .update(univ_info, synchronize_session=False)
            self.session.commit()
            # KEY, IF user_id wrong will not find the user, And res will be 0
            if res == 0:
                print("Warning: Such update wasn't executed, please check whether univ_abbrev is correct")
        except Exception as e:
            self.session.rollback()
            print("**Failed Update**")
            print(e)

    def get_university_alums(self, univ_abbrev: str):
        univ = self.session.query(University).filter(University.univ_abbrev == univ_abbrev).first()
        if not univ:
            print("Cannot Find this University, Please check abbreviation again, or whether this university already created")
            return None
        else:
            return univ.get_alums()


        

    




