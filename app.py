from flask import Flask, render_template, request
import requests
# from config import NEWS_API_KEY
from major_categories import FinancialCategory, FinancialSubmodule

app = Flask(__name__)

@app.route('/')
def index():
    categories = [
        FinancialCategory("Preparing For Your First Job", 
            [
                FinancialSubmodule("Career Planning", "insert info", "navigate"),
                FinancialSubmodule("Comparing Jobs", "info", "path"),
                FinancialSubmodule("Taxes", "info", "path")
            ]
        ),
        FinancialCategory("Saving and Investing", [
                FinancialSubmodule("Budgeting", "info", "path"),
                FinancialSubmodule("Banking", "info", "path"),
                FinancialSubmodule("Investing", "info", "path"),
                FinancialSubmodule("Retirement", "info", "path")
            ]),
        FinancialCategory("Debt", [
                FinancialSubmodule("Credit Cards", "info", "path"),
                FinancialSubmodule("Major Purchases", "info", "path"),
                FinancialSubmodule("Debt Management", "info", "path"),
                FinancialSubmodule("Student Loans", "info", "path"),
            ]),
    ]
    return render_template('index.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
