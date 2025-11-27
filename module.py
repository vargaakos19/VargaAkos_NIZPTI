from cl import Costs
from datetime import datetime, date

costs = []

def new_cost(category, amount, comment=""):
    new = Costs(category, amount, comment)
    costs.append(new)
    return new

def get_list_strings():
    return [str(k) for k in costs]

def delete_index(index):
    if 0 <= index < len(costs):
        del costs[index]
        return True
    return False

def all_amount():
    return sum(k.amount for k in costs)

def save(filename="costs.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for k in costs:
            f.write(str(k) + "\n")
    return filename

def todays_date():
    return date.today()

def now_timestamp():
    return datetime.now()

def format_date(dt, fmt="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(fmt)