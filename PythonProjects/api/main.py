from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Customers'

mysql = MySQL(app)





@app.route('/customer') # GET
def getCustomer():
    result = {'id': 12, 'firstname': 'Agustin', 'lastname':'Escofet', 'email':'dlkasdl@dot.com', 'phone':'121239094', 'address':'djafjasfd'}
    return jsonify(result)

@app.route('/customers') # GET
def getAllCustomer():
    return 'Devuelve listado de clientes'

@app.route('/customers', methods=['POST']) # POST
def saveCustomer():
    cur = mysql.connection.cursor()
    cur.excecute("INSERT INTO `academias` (`id`, `firstname`, `lastname`, `email`, `phone`, `address`) VALUES ('Agustin', 'Escofet', 'dlkasdl@dot.com', '121239094', 'djafjasfd');")
    mysql.connection.commit()
    mysql.connection.close()
    return 'Cliente Guardado'

@app.route('/customers/<int:id>', methods=['DELETE']) # DELETE
def removeCustomer(id):
    return 'Cliente Eliminado'


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(None, 3000, True)

