from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# MySQL Database connection settings
db_host = "database.clq4kqsc0hun.us-east-1.rds.amazonaws.com"  
db_user = "admin1"  # Your MySQL username
db_password = "Tarunrathod"  # Your MySQL password
db_name = "db"  # Your database name

# Function to connect to the RDS MySQL database
def connect_to_db():
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return connection

# Route for landing page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle form submission from contact page
@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Connect to MySQL and insert the contact form data into the table
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        sql = "INSERT INTO contact_us (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, message))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

    # Redirect to thank you page
    return redirect(url_for('thank_you'))

# Route for thank you page
@app.route('/thank-you')
def thank_you():
    return "<h1>Thank you for contacting us!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
