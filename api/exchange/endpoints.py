from fastapi import APIRouter

from api.exchange.business_rules import exchange
from api.exchange.schemas import ExchangeResponse

router = APIRouter()


@router.get("/exchange", response_model=ExchangeResponse)
async def get_exchange(from_currency: str, to_currency: str, amount: float) -> ExchangeResponse:
    response = {
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount_consulted': amount,
        'amount_resulted': await exchange(from_currency, to_currency, amount)
    }

    return ExchangeResponse(**response)
