from flask import Flask, render_template, request
# from config import API_KEY
from major_categories import FinancialCategory, FinancialSubmodule

app = Flask(__name__)

categories = [
    FinancialCategory("Preparing For Your First Job", [
        FinancialSubmodule("Career Planning", "career_planning"),
        FinancialSubmodule("Comparing Jobs", "comparing_jobs"),
        FinancialSubmodule("Taxes 101", "taxes")   
    ]),
    FinancialCategory("Saving and Investing", [
        FinancialSubmodule("Budgeting / Emergency Fund", "budgeting"),
        FinancialSubmodule("Banking", "banking"),
        FinancialSubmodule("Investment Basics", "investment_basics") 
    ]),
    FinancialCategory("Debt", [
        FinancialSubmodule("Credit Cards", "credit_cards"),
        FinancialSubmodule("Major Purchases", "major_purchases"),
        FinancialSubmodule("Debt Management", "debt_management"),
        FinancialSubmodule("Student Loans", "student_loans") 
    ]),
]

valid_paths = {}
for category in categories: 
    for submodule in category.submodules:
        valid_paths[submodule.path] = True
valid_paths["career_planning_q"] = True
valid_paths["submit-answer"] = True
valid_paths["submit-answer-incorrect"] = True

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/<string:Name>')
def submodule(Name):
    path_name = "404"
    if Name in valid_paths: 
        path_name = Name
    return render_template(f"pages/{path_name}.html")

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    selected_answer = request.form.get('answer')
    correct_answer = request.form.get('cAns')

    if selected_answer == correct_answer:
        result_message = "Correct!"
        return render_template('pages/submit-answer.html', result_message=result_message)
    elif not selected_answer:
        result_message = "You didn't select an answer!"
    else:
        result_message = "Incorrect. Try again."
    return render_template('pages/submit-answer-incorrect.html', result_message=result_message)
    

if __name__ == '__main__':
    app.run(debug=True)
