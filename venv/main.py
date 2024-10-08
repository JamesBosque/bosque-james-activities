from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    if request.form["username"] == "marvin" and request.form["password"] == "alingasa":
        return redirect('employee-list')
    else:
        return render_template('index.html')
    
@app.route('/employee-list')
def employee_list():
    return render_template('employee_list.html')

if __name__ == '__main__':
    app.run()