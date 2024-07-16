from datetime import datetime
# from employeeLogin import access
# from employeeLogin import CreateAccount
# from employeeLogin import NewAccount
# from employeeLogin import Login
# from employeeLogin import Logout
# from create import new_task
# from create import home
# from lists import list_of_tasks
# from lists import open_tasks
# from lists import completed_tasks
# from delete import deleteTask
# from update import updateTask
# from fetchalltasks import fetchAllTasks
# from fetchopentasks import fetchListOfOpenTasks
# from fetchCompleted import fetchCompletedTasks
# from fetchaccs import fetchAccs
# from completedtask import completed_task
# from errorhandler import page_not_found
import re
from flask import render_template
from flask import Flask
# from app import app
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_db = mysql.connector.connect(
    host="host.docker.internal",
    port="3306",
    user="root",
    password="root123",
    database="dbjoins2"
)





def fetchCustomer():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close() 


def fetchProduct():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close() 


def fetchShipper():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM shipper")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchOrders():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchOrderItems():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM order_items")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchShipping():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM shipping")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchInnerJoins():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select item_id, oi.item_name, o.order_id, order_status From order_items oi Join orders o On oi.order_id = o.order_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()

  
def fetchInnerJoinsMultiple():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select o.order_id, item_id, oi.item_name, oi.item_quantity, o.order_status, s.shipper_id, s.shipping_details From order_items oi Join orders o On oi.order_id = o.order_id Join shipping s On s.shipper_id = o.shipper_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchUsingClause():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select item_id, oi.item_name, o.order_id, order_status From order_items oi Join orders o Using(order_id)")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchImplicitJoins():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select item_id, oi.item_name, o.order_id, order_status From order_items oi, orders o Where oi.order_id = o.order_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchJoinsAcrossDbs():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select o.order_id, c.customer_id, c.name, o.order_status From orders o Join dbjoins.customer c On o.customer_id = c.customer_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchSelfJoins():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select c.customer_id, c.name, a.name as agent From customer c Join customer a On a.customer_id = c.agent_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchCompoundJoins():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select o.order_id, o.customer_id, o.order_status, s.shipper_id, s.shipping_details From orders o Join shipping s On o.order_id = s.order_id and o.customer_id = s.customer_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchLeftJoin():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select c.customer_id, c.name, o.order_id, o.order_status From customer c Left Join orders o On c.customer_id = o.customer_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchLeftJoinMultiple():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select c.customer_id, c.name, o.order_id, o.order_status, s.shipper_id From customer c Left Join orders o On c.customer_id = o.customer_id Left Join shipping s On s.shipper_id = o.shipper_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchSelfOuterJoins():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select c.customer_id, c.name, a.name as agent From customer c Left Join customer a On a.customer_id = c.agent_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchCrossJoin():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select o.order_id, oi.item_name, oi.item_id, o.order_status From orders o Cross Join order_items oi Order by order_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()


def fetchUnion():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("Select c.customer_id, c.name, c.age, 'Male' As gender From customer c Where gender = 'M' Union  Select c.customer_id, c.name, c.age, 'Female' As gender From customer c Where gender = 'F' Order By customer_id")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close()






@app.route('/', methods=['GET'])
def DB():
  
      return render_template('DB.html',dataC=fetchCustomer(), dataP=fetchProduct(), dataS=fetchShipper(), dataO=fetchOrders(), dataOI=fetchOrderItems(), dataSH=fetchShipping())


@app.route('/innerjoins', methods=['GET'])
def innerJoins():

      return render_template('IJ.html',dataIJ=fetchInnerJoins(), dataOI=fetchOrderItems(), dataO=fetchOrders() )


@app.route('/innerjoinsmultiple', methods=['GET'])
def innerJoinsMultiple():

      return render_template('IJM.html',dataIJM=fetchInnerJoinsMultiple(), dataOI=fetchOrderItems(), dataO=fetchOrders(), dataSH=fetchShipping() )


@app.route('/usingclause', methods=['GET'])
def usingClause():

      return render_template('UC.html',dataUC=fetchUsingClause(), dataOI=fetchOrderItems(), dataO=fetchOrders() )


@app.route('/joinsacrossdbs', methods=['GET'])
def joinsAcrossDbs():

      return render_template('AD.html',dataAD=fetchJoinsAcrossDbs(), dataC=fetchCustomer(), dataO=fetchOrders() )


@app.route('/selfjoins', methods=['GET'])
def selfJoins():

      return render_template('SJ.html',dataSJ=fetchSelfJoins(), dataC=fetchCustomer() )


@app.route('/compoundjoins', methods=['GET'])
def compoundJoins():

      return render_template('CJ.html',dataCJ=fetchCompoundJoins(), dataSH=fetchShipping(), dataO=fetchOrders() )


@app.route('/implicitjoins', methods=['GET'])
def implicitJoins():

      return render_template('ImpJ.html',dataImpJ=fetchImplicitJoins(), dataOI=fetchOrderItems(), dataO=fetchOrders() )


@app.route('/leftjoin', methods=['GET'])
def leftJoin():

      return render_template('LJ.html',dataLJ=fetchLeftJoin(), dataC=fetchCustomer(), dataO=fetchOrders() )


@app.route('/leftjoinmult', methods=['GET'])
def leftJoinMultiple():

      return render_template('LJM.html',dataLJM=fetchLeftJoinMultiple(), dataC=fetchCustomer(), dataO=fetchOrders(), dataSH=fetchShipping() )


@app.route('/selfouterjoins', methods=['GET'])
def selfOuterJoins():

      return render_template('SOJ.html',dataSOJ=fetchSelfOuterJoins(), dataC=fetchCustomer() )


@app.route('/crossjoins', methods=['GET'])
def crossJoins():

      return render_template('XJ.html',dataXJ=fetchCrossJoin(), dataOI=fetchOrderItems(), dataO=fetchOrders() )


@app.route('/unions', methods=['GET'])
def unions():

      return render_template('U.html',dataU=fetchUnion(), dataC=fetchCustomer() )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")


    


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
