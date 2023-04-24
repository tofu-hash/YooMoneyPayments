from yoomoney import Quickpay, Client
from config import TOKEN


def invoice(amount: int, card: str):
    quickpay = Quickpay(
        receiver=card,
        quickpay_form="shop",
        targets="Sponsor this project",
        paymentType="SB",
        sum=amount,
        label="a1b2c3d4e5"
    )
    print(quickpay.base_url)
    print(quickpay.redirected_url)


# Get transactions history

def check_payment():
    client = Client(TOKEN)
    history = client.operation_history(label="a1b2c3d4e5")
    print("List of operations:")
    print("Next page starts with: ", history.next_record)
    for operation in history.operations:
        print()
        print("Operation:", operation.operation_id)
        print("\tStatus     -->", operation.status)
        print("\tDatetime   -->", operation.datetime)
        print("\tTitle      -->", operation.title)
        print("\tPattern id -->", operation.pattern_id)
        print("\tDirection  -->", operation.direction)
        print("\tAmount     -->", operation.amount)
        print("\tLabel      -->", operation.label)
        print("\tType       -->", operation.type)
