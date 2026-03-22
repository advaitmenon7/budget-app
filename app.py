from flask import *

app = Flask(__name__)
methods=['GET', 'POST']
#@app.route("/")
#def home():
#    return render_template("index.html")


@app.route('/show_budget', methods=['GET', 'POST']
)
def show_budget():
        return render_template('dashboard.html') # Redirects to the dashboard view

@app.route('/show_goals', methods=['GET', 'POST']
)
def show_goals():
        return render_template('goals.html') # Redirects to the dashboard view

@app.route('/show_mortgage', methods=['GET', 'POST']
)
def show_mortgage():
        return render_template('Mortgage.html') # Redirects to the dashboard view

@app.route('/show_simple', methods=['GET', 'POST']
)
def show_simple():
        return render_template('Simple.html') # Redirects to the dashboard view

@app.route('/handle_data', methods=['POST']
)
def handle_data():
    # Retrieve data using the 'name' attribute from HTML
    bills = int(request.form.get('bills', 0) or 0)
    food = int(request.form.get('food', 0) or 0)
    rent = int(request.form.get('rent', 0) or 0)
    transport = int(request.form.get('transport', 0) or 0)
    fun = int(request.form.get('fun', 0) or 0)
    taxes = int(request.form.get('taxes', 0) or 0)
    income = int(request.form.get('income', 0) or 0)

    expenses = int(bills)+int(food) + int(rent) + int(transport) + int(fun) + int(taxes) 
    savings = int(income)-int(expenses)
    return render_template('dashboard.html', income=income, expenses=expenses, savings=savings)

@app.route('/handle_gata', methods=['POST']
)
def handle_gata():

    time = request.form.get('time', 0) or 0
    drate = request.form.get('drate', 0) or 0
    interest = request.form.get('interest', 0) or 0
    initial = request.form.get('initial', 0) or 0
    time = int(time) if time is not None else 0
    interest = int(interest) if interest is not None else 0
    interest = int(interest)/100 
    initial = float(initial) if initial is not None else 0
    drate=float(drate) if drate is not None else 0
    payment = float(initial)*(1+float(interest)/float(drate))**(float(time)/12*float(drate))
    payment = (round(float(payment), 2))
    return render_template('goals.html', payment=payment,time = time)
    #payment = payment 
  
@app.route('/handle_mata', methods=['POST']
)
def handle_mata():

    hprice = request.form.get('hprice', 0) or 0
    dpayment = request.form.get('dpayment', 0) or 0
    irate = request.form.get('rate', 0) or 0
    years = request.form.get('years', 0) or 0   
    hprice = float(hprice) if hprice is not None else 0
    dpayment = float(dpayment) if dpayment is not None else 0
    irate = float(irate) if irate is not None else 0
    years = float(years) if years is not None else 0
    p = int(hprice)-int(dpayment)
    r = float(irate)/1200
    r = round(r, 4)
    n = float(years)*12
    a = (1+float(r))**float(n)
    pamount = float(p)*((float(r)*float(a))/(float(a)-0.99))
    pamount = round(float(pamount), 2)
    return render_template('Mortgage.html', pamount=pamount, years=years)

@app.route('/handle_sata', methods=['POST']
)
def handle_sata():

    ideposit = request.form.get('ideposit', 0) or 0
    sate = request.form.get('sate', 0) or 0
    sears = request.form.get('sears', 0) or 0
    sate = float(sate) if sate is not None else 1 
    sate = float(sate)/100
    sears = float(sears) if sears  is not None else 1
    ideposit = float(ideposit) if ideposit  is not None else 500
    sint = float(sears)*float(sate)*int(ideposit)
    samount = float(sint)+int(ideposit)
    samount = round(samount, 2)
    return render_template('Simple.html', samount=samount, sears=sears)


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
    den = int(interest)**int(time)*int(drate)
    payment = int(soal)
    # Pass the variable to the template using keyword arguments
    return render_template('index.html', income=income, expenses=expenses, savings=savings, payment=payment)

if __name__ == '__main__':
    app.run(debug=True)