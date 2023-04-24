from yoomoney import Authorize
from config import CLIENT_ID, REDIRECT_URL

# https://yoomoney.ru/myservices/new

Authorize(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URL,
    scope=["account-info",
           "operation-history",
           "operation-details",
           "incoming-transfers",
           "payment-p2p",
           "payment-shop",
           ]
)
