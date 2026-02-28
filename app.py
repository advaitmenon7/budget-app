from flask import *

app = Flask(__name__)

#@app.route("/")
#def home():
#    return render_template("index.html")


@app.route('/show_budget', methods=['POST'])
def show_budget():
        return render_template('dashboard.html') # Redirects to the dashboard view

@app.route('/submit', methods=['POST'])
def handle_data():
    # Retrieve data using the 'name' attribute from HTML
    bills = request.form.get('bills')
    food = request.form.get('food')
    rent = request.form.get('rent')
    income = request.form.get('income')
    transport = request.form.get('transport')
    fun = request.form.get('fun')
    charity = request.form.get('charity')

    # Define your Python variable
    income = income
    bills = bills
    food = food
    rent = rent 
    transport = transport
    fun = fun
    charity = charity 
    expenses = (int(bills) + int(food) + int(rent)+int(transport) + int(fun) + int(charity))
    savings = (int(income)-int(expenses))
    return render_template('index.html', income=income, expenses=expenses, savings=savings)
  

@app.route('/')
def index():
    # Define your Python variable
    income = 2000
    bills = 123
    food = 234
    rent = 1000 
    expenses = (int(bills) + int(food) + int(rent))
    savings = (int(income)-int(expenses))

    # Pass the variable to the template using keyword arguments
    return render_template('index.html', income=income, expenses=expenses, savings=savings)

if __name__ == '__main__':
    app.run(debug=True)

#<div class="container">
             #<div class="redtangle">
              #   <p style="color:rgb(255, 255, 255); font-size: 19px;">
               #     <form action="{{ url_for('show_budget') }}" method="POST">
                #        <button type="submit">Budget</button>
                 #    </form>
                 #</p>

    #    <div class="container">
     #       <div class="container">
      #      <div class="redtangle"> Goals </div>
#
 #           <div class="redtangle"> Insights</div>
#
 #       
  #          <div class="redtangle">Income ({{ income }})</div>
#
 #           <div class="redtangle">Expenses ({{ expenses }})</div>
#
 #           <div class="redtangle">Savings ({{ savings }})</div>
