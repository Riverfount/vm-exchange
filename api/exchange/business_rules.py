import httpx
from fastapi import status
from fastapi.exceptions import HTTPException

from api.config import settings


async def exchange(from_currency: str = 'USD', to_currency: str = 'USD', amount: float = 1.0) -> str:
    """
    Asynchronously exchanges a given amount of currency from one base currency to another.
    Args:
        from_currency (str, optional): The currency to exchange from. Default is 'USD'.
        to_currency (str, optional): The base currency to exchange to. Default is 'USD'.
        amount (float, optional): The amount of currency to exchange. Default is 1.0.
    Returns:
        str: The converted amount of currency.
    Raises:
        HTTPException: If the API request fails or the response is not successful.
    Notes:
        - The function makes an asynchronous HTTP GET request to the APILayer to retrieve the exchange rates.
        - The API key is obtained from the `settings.security.API_KEY` configuration variable.
        - The function raises an `HTTPException` if the API request fails or the response is not successful.
        - The function rounds the converted amount of currency to 2 decimal places.
    """
    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    url = f"{base_url}?symbols={to_currency}&base={from_currency}"
    headers = {"apikey": settings.security.API_KEY}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=headers, timeout=15)
        except httpx.TimeoutException:
            raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Request timed out")

    response = resp.json()

    if not response["success"]:
        raise HTTPException(status_code=resp.status_code, detail=response["error"]["info"])

    rate = response["rates"][to_currency]
    response = f'{round(rate * amount, 2):.2f}'
    return response
