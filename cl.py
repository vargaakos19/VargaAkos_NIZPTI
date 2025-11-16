from datetime import datetime

class Costs:
    def __init__(self, category, amount, comment=""):
        self.category = category
        self.amount = amount
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"[{self.date}] {self.category}: {self.amount} Ft ({self.comment})"