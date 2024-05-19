import httpx
from aioetherscan import Client
from aiohttp_retry import ExponentialRetry
from asyncio_throttle import Throttler
from fastapi import status
from fastapi.exceptions import HTTPException

from api.config import settings


async def get_currency_exchange(from_currency: str = 'USD', to_currency: str = 'USD', amount: float = 1.0) -> float:
    """
    Asynchronously retrieves the exchange rate for a given currency pair and amount.

    Args:
        from_currency (str, optional): The currency to exchange from. Default is 'USD'.
        to_currency (str, optional): The currency to exchange to. Default is 'USD'.
        amount (float, optional): The amount to exchange. Default is 1.0.
    Returns:
        float: The result of the exchange as a string.
    Raises:
        HTTPException: If the request times out or if the API response is unsuccessful.
    Notes:
        - This function makes an HTTP GET request to the API at https://api.apilayer.com/exchangerates_data/latest.
        - The API key is retrieved from the `settings.security.API_KEY` variable.
        - The exchange rate is calculated by multiplying the rate for the `to_currency` with the `amount`.
        - The result is rounded to 2 decimal places and returned as a string.
    """
    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    url = f"{base_url}?symbols={to_currency}&base={from_currency}"
    headers = {"apikey": settings.security.APILAYER_API_KEY}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=headers, timeout=15)
        except httpx.TimeoutException:
            raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Request timed out")
    response = resp.json()
    if not response["success"]:
        raise HTTPException(status_code=resp.status_code, detail=response["error"]["info"])
    rate = response["rates"][to_currency]
    response = round(rate * amount, 5)
    return response


async def get_exchange_eth() -> float:
    """
    Asynchronously retrieves the current exchange rate of Ethereum (ETH) to USD (USD) from the CoinGecko API.
    Returns:
        float: The current exchange rate of Ethereum (ETH) to USD (USD).
    Raises:
        None
    Notes:
        - The function creates a CoinGecko client with the ETH API key from the settings.
        - It uses an exponential retry strategy with two attempts to handle any potential API errors.
        - The function makes an asynchronous request to the CoinGecko API to retrieve the current ETH price in USD.
        - The function then extracts the 'ethusd' value from the response and converts it to a float.
        - Finally, the function closes the CoinGecko client and returns the exchange rate.
    """
    throttler = Throttler(rate_limit=1, period=6.0)
    retry_options = ExponentialRetry(attempts=2)
    client = Client(settings.security.ETH_API_KEY, throttler=throttler, retry_options=retry_options)
    try:
        eth_price = await client.stats.eth_price()
        eth_usd_price = eth_price['ethusd']
    finally:
        await client.close()
    return float(eth_usd_price)


async def exchange(from_currency: str = 'USD', to_currency: str = 'USD', amount: float = 1.0) -> float:
    """
    Perform currency exchange based on the given parameters.
    Args:
        from_currency (str): The currency to exchange from. Default is 'USD'.
        to_currency (str): The currency to exchange to. Default is 'USD'.
        amount (float): The amount to exchange. Default is 1.0.
    Returns:
        float: The result of the exchange as a string.
    """
    # Exchange ETH to USD
    if from_currency == 'ETH' and to_currency == 'USD':
        eth_usd_price = await get_exchange_eth()
        response = round(amount * eth_usd_price, 5)
    # Exchange USD to ETH
    elif from_currency == 'USD' and to_currency == 'ETH':
        eth_usd_price = await get_exchange_eth()
        response = round(amount / eth_usd_price, 5)
    # Exchange ETH to a different currency
    elif from_currency == 'ETH' and to_currency != 'USD':
        eth_usd_price = await get_exchange_eth()
        amount *= eth_usd_price
        response = await get_currency_exchange(from_currency='USD', to_currency=to_currency, amount=amount)
    # Exchange a different currency to ETH
    elif from_currency != 'USD' and to_currency == 'ETH':
        eth_usd_price = await get_exchange_eth()
        amount /= eth_usd_price
        response = await get_currency_exchange(from_currency=from_currency, to_currency='USD', amount=amount)
    # Exchange between different currencies
    else:
        response = await get_currency_exchange(from_currency, to_currency, amount)
    return response
