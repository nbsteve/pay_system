from database.models import User, Card
from database import get_db

# Registration


# Func of checking numb and phone
def check_numb(phone_number, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number, password=password).first()
    return checker

# Func of adding user card
def add_user_card(user_id, card_number, exp_date, card_balance, card_name, reg_date):
    db = next(get_db())
    new_card = Card(user_id=user_id, card_number=card_number, exp_date=exp_date, card_balance=card_balance, card_name=card_name,reg_date=reg_date)
    db.add(new_card)
    db.commit()
    return new_card.id


# Func of getting user data by user_id
def get_user_data(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        return exact_user
    return False