from flask import render_template,request,redirect,url_for
import config
from models import Client,Delivery, client_schema, clients_schema, deliveries_schema, delivery_schema
import crud


app = config.connex_app
app.add_api(config.basedir/'swagger.yml')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clients', methods=['GET'])
def clients():
    clients_data = crud.read_all_clients()  
    return render_template('show_clients.html', clients=clients_data)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)