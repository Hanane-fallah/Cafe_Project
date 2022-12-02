from flask import Flask, render_template, url_for, request, redirect
from models.user import User


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    User.add(4, first_name, last_name, phone, email, password)
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            if User.check_login(request.form['username'], request.form['password']):
                return redirect(url_for('home'))
            else:
                error = "<h1> invalid user pass </h1>"
                return render_template('login.html', error=error)
                # todo: error

        else:
            # todo: cashier panel
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)

@app.route('/table_cashier', methods=['POST' ,'GET'])
def get_status_table():
    table_list = session.query(Table).all()
    table_recipt=session.query(Receipt).all()
    if request.method == 'POST':
        table_id = request.form["table_id"]
        table_id = int(table_id)
        tables = session.query(Table).filter(Table.id == table_id)
        status = request.form["status_table"]
        for j in tables:
            j.status = status
        session.commit()
        table_list = session.query(Table).all()
        return render_template('table.html', table_list=table_list)

    else:
        table_list = session.query(Table).all()
        return render_template('table.html', table_list=table_list ,table_recipt=table_recipt)


if __name__ == '__main__':
    app.run(debug=True)


