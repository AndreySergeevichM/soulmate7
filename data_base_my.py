import sqlite3
from config import db_file

connect = sqlite3.connect(db_file)


def create_table():
    connect.execute("create table users(profile_id)")
    connect.commit()

def add_user(profile_id):
    connect.execute(f"insert into users values({profile_id})")

def check_user(profile_id):
    userid = connect.execute(f"select profile_id from  users where profile_id = ({profile_id})").fetchone()
    return True if userid else False


if __name__ == '__main__':
    create_table()

