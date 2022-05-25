from sqlalchemy import Table, Column
from config.db import meta
users = Table('users', meta, Column('id',Integer, primary_key=True),
              Column('name',String(50)), Column('email',String(200)),
              Column('password',String(200)), Column('role',String(50)))