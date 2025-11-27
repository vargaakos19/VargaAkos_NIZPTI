from datetime import datetime

class Costs:
    def __init__(self, category, amount, comment=""):
        self.category = category
        self.amount = float(amount)
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.date}] {self.category}: {int(self.amount)} Ft {self.comment}"