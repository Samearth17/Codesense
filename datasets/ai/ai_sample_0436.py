import stripe

stripe.api_key = 'sk_test_YOUR_KEY'

def process_payment(card_info):
    # validate the credit card information
    if not stripe.Token.create(
        card={
            'number': card_info['number'],
            'exp_month': card_info['exp_month'],
            'exp_year': card_info['exp_year'],
            'cvc': card_info['cvc'],
        },
    ):
        return False

    # create and process the charge:
    stripe.Charge.create(
        amount=card_info['amount'],
        currency='usd',
        source=card_info['token'],
        description='Example charge',
    )

    return True