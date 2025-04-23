class ProccessPayment:
    def proccess_payment(self):
        pass

    def verify_payment(self):
        pass

class PayPalPayment:
    def send_payment(self, pp_request):
        print(f"PayPal payment of {pp_request['amount']} proccessed")
        return f"PP-{hash(str(pp_request))}"[:10]

    def check_payment_status(self, pp_id):
        print(f"PayPal payment verified {pp_id}")
        return {"status": "succeeded", "id": pp_id}

class PayPalAdapter(ProccessPayment):
    def __init__(self):
        self.paypal = PayPalPayment()

    def proccess_payment(self, amount, currency):
        return self.paypal.send_payment({"amount": amount, "currency": currency})

    def verify_payment(self, id):
        return self.paypal.check_payment_status(id)

class StripePayment:
    def create_charge(self, st_request):
        print(f"PayPal payment of {st_request['amount']} proccessed")
        return f"ST-{hash(str(st_request))}"[:10]

    def retrive_charge(self, st_id):
        print(f"PayPal payment verified {st_id}")
        return {"status": "succeeded", "id": st_id}

class StripeAdapter(ProccessPayment):
    def __init__(self):
        self.stripe = StripePayment()

    def proccess_payment(self, amount, currency):
        return self.stripe.create_charge({"amount": amount, "currency": currency})

    def verify_payment(self, id):
        return self.stripe.retrive_charge(id)

class CheckoutService:
    def __init__(self, payment_adapter):
        self.payment_adapter = payment_adapter

    def checkout(self, amount, currency):
        payment_id = self.payment_adapter.proccess_payment(amount, currency)
        verification = self.payment_adapter.verify_payment(payment_id)

        if verification["status"] == "succeeded":
            print(f"Order completed! Payment reference: {verification['id']}")
            return True
        else:
            print("Payment failed")
            return False

def main():
    paypal_adapter = PayPalAdapter()
    stripe_adapter = StripeAdapter()

    checkout_service = CheckoutService(paypal_adapter)
    checkout_service.checkout(100, "USD")

    checkout_service = CheckoutService(stripe_adapter)
    checkout_service.checkout(100, "USD")

if __name__ == "__main__":
    main()