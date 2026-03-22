from flask import *

app = Flask(__name__)

#@app.route("/")
#def home():
#    return render_template("index.html")


@app.route('/show_budget', methods=['POST'])
def show_budget():
        return render_template('dashboard.html') # Redirects to the dashboard view

@app.route('/show_goals', methods=['POST'])
def show_goals():
        return render_template('goals.html') # Redirects to the dashboard view

@app.route('/show_mortage', methods=['POST'])
def show_mortage():
        return render_template('Mortgage.html') # Redirects to the dashboard view

@app.route('/show_simple', methods=['POST'])
def show_simple():
        return render_template('Simple.html') # Redirects to the dashboard view

@app.route('/handle_data', methods=['POST'])
def handle_data():
    # Retrieve data using the 'name' attribute from HTML
    bills = request.form.get('bills')
    food = request.form.get('food')
    rent = request.form.get('rent')
    income = request.form.get('income')
    transport = request.form.get('transport')
    fun = request.form.get('fun')
    charity = request.form.get('charity')
    income = income
    bills = bills
    food = food
    rent = rent 
    transport = transport
    fun = fun
    charity = charity 
    expenses = int(bills)+int(food) + int(rent) + int(transport) + int(fun) + int(charity)
    savings = int(income)-int(expenses)
    return render_template('index.html', income=income, expenses=expenses, savings=savings)

@app.route('/handle_gata', methods=['POST'])
def handle_gata():

    time = request.form.get('time')
    drate = request.form.get('drate')
    interest = request.form.get('interest')   
    initial = request.form.get('initial')  
    drate = int(drate)
    time = int(time)
    interest = int(interest) 
    initial = float(initial)
    payment = int(initial)*(1+int(interest)/int(drate))**(int(time)/12*int(drate))
    payment = (round(int(payment), 2))
    return render_template('goals.html', payment=payment,time = time)
    #payment = payment 
  
@app.route('/handle_mata', methods=['POST'])
def handle_mata():

    hprice = request.form.get('hprice')
    dpayment = request.form.get('dpayment')
    irate = request.form.get('rate')
    years = request.form.get('years')   
    p = int(hprice)-int(dpayment)
    r = float(irate)/1200
    r = round(r, 4)
    n = float(years)*12
    a = (1+int(r))**int(n)
    pamount = float(p)*((float(r)*float(a))/(float(a)-0.99))
    pamount = round(pamount, 2)
    return render_template('index.html', pamount=pamount, years=years)

@app.route('/handle_sata', methods=['POST'])
def handle_sata():

    ideposit = request.form.get('ideposit')
    sate = request.form.get('sate')
    sears = request.form.get('sears')   
    sate = int(sate)/100
    sint = float(sears)*float(sate)*int(ideposit)
    samount = float(sint)+int(ideposit)
    samount = round(samount, 2)
    return render_template('index.html', samount=samount, sears=sears)


@app.route('/')
def index():
    # Define your Python variable
    income = 2000
    bills = 123
    food = 234
    rent = 1000 
    initial = 500
    soal = 12
    time = 1
    drate = 1
    interest = 1 
    expenses = 2
    savings = (int(income)-int(expenses))
    den = int(interest)^int(time)*int(drate)
    payment = int(soal)
    # Pass the variable to the template using keyword arguments
    return render_template('index.html', income=income, expenses=expenses, savings=savings, payment=payment)

if __name__ == '__main__':
    app.run(debug=True)