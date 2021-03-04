from flask import Flask, json, request, jsonify
from GUI_MySQL_class import MySQL
from waitress import serve

mysql = MySQL()

app = Flask(__name__)


@app.route("/")
def server_info():
    
    rvs = mysql.ConsultData()
    employee = [{'id':rv[0], 'alarma': rv[1]}]
    get_thing = {"get_alarma":employee}
    
    
    
    #content = {}
    #for rv in rvs:
    #    content = {'id':rv[0], 'alarma': rv[1]}
    #    employee.append(content)
    #    content = {}
    
    

    
    return jsonify(get_thing)


@app.route('/apagar/<string:id_user>', methods=["GET","POST"])
def add_adress(id_user):
    #address3 = request.form.get("hola")
    mysql.addAddress(id_user)     
    return id_user

if __name__ == "__main__":
    #app.run(debug=True)
    #serve(app, host='0.0.0.0', port=5555, threads=1)
    app.run(host="0.0.0.0", port="8080", debug=True,
            threaded=True, use_reloader=False)

