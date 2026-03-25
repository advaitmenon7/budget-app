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
    bills = float(request.form.get('bills', 0) or 0)
    food = float(request.form.get('food', 0) or 0)
    rent = float(request.form.get('rent', 0) or 0)
    transport = float(request.form.get('transport', 0) or 0)
    fun = float(request.form.get('fun', 0) or 0)
    taxes = float(request.form.get('taxes', 0) or 0)
    income = float(request.form.get('income', 0) or 0)
    savings = float(request.form.get('savings', 0) or 0)
    expenses = float(bills)+float(food) + float(rent) + float(transport) + float(fun) + float(taxes) + float(savings)
    expenses = round(expenses, 2)
    tsavings = float(income)-float(expenses)
    return render_template('dashboard.html', income=income, expenses=expenses, tsavings=tsavings,
        bills = bills, food = food, rent = rent, transport = transport, fun = fun, taxes = taxes, savings = savings)

@app.route('/handle_gata', methods=['POST'])
def handle_gata():
    try:
        time = float(request.form.get('time', 0)) * 12
        drate = float(request.form.get('drate', 12))  # 12 or 4
        interest = float(request.form.get('interest', 0)) / 100
        initial = float(request.form.get('initial', 0))

        payment = initial * (1 + interest / drate) ** (time / 12 * drate)
        payment = round(payment, 2)

        return render_template(
    'goals.html',
    payment=payment,
    time=time/12,
    initial=initial,
    interest=interest * 100,
    drate=drate
)

    except:
        return "Invalid input"  


@app.route('/handle_mata', methods=['POST'])
def handle_mata():
    try:
        hprice = float(request.form.get('hprice', 0))
        dpayment = float(request.form.get('dpayment', 0))
        irate = float(request.form.get('rate', 0))
        years = float(request.form.get('years', 0))

        p = hprice - dpayment
        r = irate / 100 / 12   # monthly interest rate
        n = years * 12         # total payments

        if r == 0:
            pamount = p / n
        else:
            pamount = p * (r * (1 + r)**n) / ((1 + r)**n - 1)

        pamount = round(pamount, 2)

        return render_template('Mortgage.html', pamount=pamount, years=years, hprice = hprice,
            dpayment = dpayment, rate=irate)

    except:
        return "Invalid input"
    
@app.route('/handle_sata', methods=['POST']
)
def handle_sata():

    ideposit = request.form.get('ideposit', 0) or 0
    sate = request.form.get('sate', 0) or 0
    sears = request.form.get('sears', 0) or 0
    sate = float(sate) if sate is not None else 1 
    sears = float(sears) if sears  is not None else 1
    ideposit = float(ideposit) if ideposit  is not None else 500
    sint = float(sears)*float(sate)*float(ideposit)/100
    samount = float(sint)+float(ideposit)
    samount = round(samount, 2)
    return render_template('Simple.html', samount=samount, sears=sears,
        sate = sate, ideposit = ideposit)


@app.route('/')
def index():
    # Define your Python variable
    income = 0
    bills = 0
    food = 0
    rent = 0 
    initial = 0
    soal = 0
    time = 0
    drate = 0
    interest = 0
    expenses = 0
    savings = 0
    payment = float(soal)
    # Pass the variable to the template using keyword arguments
    return render_template('index.html', income=income, expenses=expenses, savings=savings, payment=payment)

if __name__ == '__main__':
    app.run(debug=True)