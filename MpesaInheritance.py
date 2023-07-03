class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount
    def process_transaction(self):
            raise NotImplementedError("subclass to use this method")

class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit transaction with ID {self.transaction_id} processed. Amount{self.amount}")
class WithdrawalTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdrawal Transaction with ID {self.transaction_id} processed. Amount{self.amount}")

class PaymentTransaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recepient):
        super().__init__(transaction_id, amount)
        self.recipient = recepient
    def process_transaction(self):
        print(f"Payment transaction with ID {self.transaction_id} processed. Amount {self.amount} procesed. Recipient {self.recipient}")

deposit = DepositTransaction("DHTY", 2000)
deposit.process_transaction()
withdrawal = WithdrawalTransaction("PKGY", 500)
withdrawal.process_transaction()
payment = PaymentTransaction("DHTY", 1000, "Weston")
payment.process_transaction()