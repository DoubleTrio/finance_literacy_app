from flask import Flask, render_template, request, jsonify
import requests

class FinancialSubmodule:
  def __init__(self, module_name: str, path: str):
    self.module_name = module_name
    self.path = path
    self.completed = False
    
class FinancialCategory:
  def __init__(self, name: str, submodules: list[FinancialSubmodule]):
    self.name = name
    self.submodules = submodules

  def all_completed(self):
    completed = True
    for module in self.submodules:
      if not module.completed:
        completed = False
    return completed

class AllCategories:
  def __init__(self, categories: list[FinancialCategory]):
    self.categories = categories

  def mark_complete(self, name):
    for category in self.categories:
      for submodule in category.submodules:
        if submodule.path == name:
          submodule.completed = True

  def completed(self):
    completed = True
    for category in self.categories:
      if not category.all_completed():
        completed = False
    return completed
  
import json
app = Flask(__name__)

all_categories = AllCategories([
    FinancialCategory("Preparing For Your First Job", [
        FinancialSubmodule("Career Planning", "career_planning"),
        FinancialSubmodule("Comparing Jobs", "comparing_jobs"),
        FinancialSubmodule("Taxes 101", "taxes")
    ]),
    FinancialCategory("Saving and Investing", [
        FinancialSubmodule("Budgeting / Emergency Fund", "budgeting"),
        FinancialSubmodule("Banking", "banking"),
        FinancialSubmodule("Investment / Retirement Basics", "investment_basics") 
    ]),
    FinancialCategory("Debt", [
        FinancialSubmodule("Credit Cards", "credit_cards"),
        FinancialSubmodule("Major Purchases", "major_purchases"),
        FinancialSubmodule("Debt Management", "debt_management"),
        FinancialSubmodule("Student Loans", "student_loans") 
    ]),
])

valid_paths = {}
for category in all_categories.categories: 
    for submodule in category.submodules:
        valid_paths[submodule.path] = True


@app.route('/')
def index():
    return render_template('index.html', categories=all_categories.categories)

@app.route('/finished', methods=['POST'])
def finished_submodule():
    raw_data = request.data  # this gives you the raw byte data
    decoded_data = raw_data.decode('utf-8')
    data = json.loads(decoded_data)
    path = data.get('path')

    print(f"Received path: {path}")
    all_categories.mark_complete(path)
    return jsonify({"status": "success", "received_path": True})

@app.route('/submodules/<string:name>')
def submodule(name):
    return render_template(f"pages/{name}.html", path_name=name)

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    selected_answer = request.form.get('answer')
    correct_answer = request.form.get('think')

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
