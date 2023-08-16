from pydantic import BaseModel
from datetime import datetime

# Model transfer from card to card
class P2PDent(BaseModel):
    card_from: int
    amount: float
    card_to: int
    transfer_time: datetime



