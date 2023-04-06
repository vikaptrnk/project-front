from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        day = request.form['day']
        month = request.form['month']
        gender = request.form['gender']
        
        partner_day = request.form['partner_day']
        partner_month = request.form['partner_month']
        partner_gender = request.form['partner_gender']

        # result = process_data(day, month, gender, partner_day, partner_month, partner_gender)
        return render_template('index.html', info=True, day=day, month=month, gender=gender, partner_day=partner_day, partner_month=partner_month, partner_gender=partner_gender)

    return render_template('index.html')

if name == '__main__':
    app.run(debug=True)