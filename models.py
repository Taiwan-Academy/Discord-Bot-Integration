from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date
from sqlalchemy import create_engine

Base = declarative_base()
class University(Base):
    __tablename__ = 'university'
    univ_id = Column(Integer, primary_key=True)
    univ_abbrev = Column(String, unique= True,nullable=False)
    univ_name = Column(String)
    region = Column(String)

    # NOTE Relationship should be referencing the class, not my actual table name:
    univ_alums = relationship("User", backref='university')

    def __init__(self, univ):
        super().__init__()
        self.univ_abbrev = univ['univ_abbrev'] if 'univ_abbrev' in univ else ''
        self.univ_name = univ['univ_name'] if 'univ_name' in univ else ''
        self.region = univ['region'] if 'region' in univ else ''


    def get_alums(self):
        alums = []
        for alumni in self.univ_alums:
            alums.append(alumni)
        return alums

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key= True)
    user_name =Column(String)
    univ_abbrev =Column(String, ForeignKey(University.univ_abbrev))
    prog_deg =Column(String)
    prog_name =Column(String)
    prog_start_yr = Column(Date)
    prog_end_yr = Column(Date)
    linkedin_url = Column(String)
    created_dt = Column(DateTime,default=datetime.now(), nullable=False)
    last_updated_dt= Column(DateTime)
    last_updated_user =Column(String)
    leave_server_dt= Column(DateTime)
    user_status = Column(String, default="Non-verified")

    def __init__(self, user):
        super().__init__()
        # If detected None, will use default value
        self.user_id = user['user_id'] if 'user_id' in user else None
        self.user_name = user['user_name'] if 'user_name' in user else None
        self.univ_abbrev = user['univ_abbrev'] if 'univ_abbrev' in user else None
        self.prog_deg = user['prog_deg'] if 'prog_deg' in user else None
        self.prog_name = user['prog_name'] if 'prog_name' in user else None
        self.prog_start_yr = datetime.strptime(user['prog_start_yr'], '%Y-%m-%d') if 'prog_start_yr' in user else None
        self.prog_end_yr = datetime.strptime(user['prog_end_yr'], '%Y-%m-%d') if 'prog_end_yr' in user else None
        self.linkedin_url = user['linkedin_url'] if 'linkedin_url' in user else None
        self.created_dt = datetime.strptime(user['created_dt'], '%Y-%m-%d') if 'created_dt' in user else None
        self.last_updated_dt = datetime.strptime(user['last_updated_dt'], '%Y-%m-%d') if 'last_updated_dt' in user else None
        self.last_updated_user = user['last_updated_user'] if 'last_updated_user' in user else None
        self.leave_server_dt = datetime.strptime(user['leave_server_dt'], '%Y-%m-%d') if 'leave_server_dt' in user else None
        self.user_status = user['user_status'] if 'user_status' in user else None


engine = create_engine('sqlite:///data.sqlite')
Base.metadata.create_all(engine, checkfirst=True)
