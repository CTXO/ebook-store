class PaymentInfo:
    def __init__(self, user_id: int, payment_method: str, total_price_cents: int, ebook_ids: list[int]):
        self.user_id = user_id
        self.payment_method = payment_method
        self.total_price_cents = total_price_cents
        self.ebook_ids = ebook_ids
