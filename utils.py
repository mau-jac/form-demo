from typing import Optional

def add_user_db(db:list, name:str, email: str, password: str):
    db.append({
        "name": name,
        "email": email,
        "password": password
    })