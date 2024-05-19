from fastapi import APIRouter

from api.resources.exchange.business_rules import exchange
from api.resources.exchange.schemas import ExchangeResponse

router = APIRouter()


@router.get("/exchange", response_model=ExchangeResponse)
async def get_exchange(from_currency: str, to_currency: str, amount: float) -> ExchangeResponse:
    """
    Get the exchange rate between two currencies.\n
    **Parameters**:\n
        - from_currency (str): The currency to exchange from.
        - to_currency (str): The currency to exchange to.
        - amount (float): The amount to exchange.
    **Returns**:\n
        - ExchangeResponse: The response object containing the exchange rate.
    **Notes**:\n
        - This function makes an asynchronous call to the `exchange` function to get the exchange rate.
        - The `ExchangeResponse` object is created with the provided parameters and the result of the exchange.
    """
    response = ExchangeResponse(
        from_currency=from_currency,
        to_currency=to_currency,
        amount_consulted=amount,
        amount_resulted=await exchange(from_currency, to_currency, amount))
    return response
