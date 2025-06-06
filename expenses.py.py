import json 
import os

DATA_FILE="expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return[]
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(espenses):
    with open(DATA_FILE, "W") as file:
        json.dump(expenses, file, indent=4)

def add_expense(category, amount):
    expenses=load_expenses ()
    expenses.append(( "category": category, "amount":amount))
    save_expenses(expenses)

def get_total_expense():
    expenses=load_expenses()
    return sum(item["amount"]for item in expenses)

def get_expense_by_ctegory(category):
    expenses=load_expenses()
    return sum(item[" amount"]for item in expenses if item ["category"]==category)
