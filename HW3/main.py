from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python
def index():
    return render_template('index.html')

# insert a new row (5, 'Cherry') into basket_a. On the browser, it should either show "Success!" 
# Or error message from PostgreSQL.
@app.route('/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    # Send request to insert value into table
    record = util.run_and_commit_sql(cursor,connection,"INSERT INTO basket_a VALUES (5, 'Cherry')")
    util.disconnect_from_db(connection,cursor)

    return render_template('success_fail.html', log_message = record)

# show unique fruits in basket_a and unique fruits in basket_b in an HTML table. 
# If there are any errors from PostgreSQL, show the error message on the browser.
@app.route('/unique')
def unique():
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    record = util.run_and_fetch_sql(cursor, """
                                    SELECT 
                                        a.fruit_a AS basket_a,
                                        b.fruit_b AS basket_b
                                    FROM 
                                        basket_a a
                                    FULL OUTER JOIN 
                                        basket_b b ON a.fruit_a = b.fruit_b
                                    WHERE 
                                        a.fruit_a IS NULL OR b.fruit_b IS NULL;
                                    """)


    if record == -1:
        print('Something is wrong. 404.')
        return render_template('404.html')
    else:
        col_names = [desc[0] for desc in cursor.description]

    util.disconnect_from_db(connection,cursor)

    return render_template('unique.html', table_title = col_names, sql_table = record)


    

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

