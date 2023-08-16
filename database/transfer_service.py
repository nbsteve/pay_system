from database.models import Transactions, Card
from database import get_db


# money transfer (balance check)
def money_transfer_db(card_from, card_to, amount, transaction_date):
    db = next(get_db)

    card_from_db = db.query(Card).filter_by(card_number=card_from).first()
    card_to_db = db.query(Card).filter_by(card_number=card_to).first()


    # checking cards for existence
    if card_from_db and card_to_db:
        # checking if balance if sufficient
        if card_from_db.card_balance >= amount:
            card_from_db.card_balance -= amount
            card_to_db.card_balance += amount

            new_transaction = Transactions(card_from=card_from,
                                          card_to=card_to,
                                          amount=amount,
                                          transfer_time=transaction_date)

            db.add(new_transaction)
            db.commit()
            return ' недостаточно средств'
        return 'неверные данные'
# monetoring card_id