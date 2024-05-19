from pydantic import BaseModel


class ExchangeResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount_consulted: float
    amount_resulted: float

    class Config:
        schema_extra = {
            'example': {
                'from_currency': 'USD',
                'to_currency': 'BRL',
                'amount_consulted': 1.00,
                'amount_resulted': 5.11
            }
        }
