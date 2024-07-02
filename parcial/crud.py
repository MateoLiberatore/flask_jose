from models import Client, Delivery, client_schema, clients_schema, deliveries_schema,delivery_schema
from config import db, app
from flask import abort, jsonify

def read_all_clients():
    clients = Client.query.all()
    return print(clients_schema.dump(clients))

def read_single_client(id):
    client = Client.query.filter(Client.id == id).one_or_none()

    if client is not None:
        return print(client_schema.dump(client))
    else:
        return print(404,"Client not found")
    
def create_client(client):

    phone = client.get('phone')
    existing_phone = Client.query.filter(Client.phone == phone).one_or_none()

    if existing_phone is None:

        new_client = Client(
            name=client.get('name'),
            address=client.get('address'),
            phone=client.get('phone')
        )

        db.session.add(new_client)
        db.session.commit()

        return client_schema.dump(new_client)

    else:
        abort(406, message=f"Client with phone number: {phone}, already exists")

    
def update_client(id, client):

    existing_client = Client.query.filter(Client.id == id).one_or_none()

    if existing_client:
        existing_client.name = client.get('name')
        existing_client.address = client.get('address')
        existing_client.phone = client.get('phone')

        db.session.merge(existing_client)
        db.session.commit()

        return client_schema.dump(existing_client)
    else:
        abort(404, message=f"Client with id: {id}, not found")


def delete_client(id):

    existing_client = Client.query.filter(Client.id == id).one_or_none()

    if existing_client:
        db.session.delete(existing_client)
        db.session.commit()

        return print(client_schema.dump(existing_client))
    else:
        abort(404, message=f"Client with id: {id}, not found")

def add_delivery(client_id, delivery):
    client = Client.query.filter(Client.id == client_id).one_or_none()

    if client is not None:
        new_delivery = Delivery(
            Client_id=client_id,
            description=delivery.get('description')
        )

        db.session.add(new_delivery)
        db.session.commit()

        return client_schema.dump(new_delivery)
    else:
        abort(404, message=f"Client with id: {client_id}, not found")

def read_all_deliveries():
    deliveries = Delivery.query.all()
    return print(deliveries_schema.dump(deliveries))

def read_single_delivery(id):
    delivery = Delivery.query.filter(Delivery.id == id).one_or_none()

    if delivery is not None:
        return print(delivery_schema.dump(delivery))
    else:
        return print(404,"Delivery not found")
    
def update_delivery(id, delivery):

    existing_delivery = Delivery.query.filter(Delivery.id == id).one_or_none()

    if existing_delivery:
        existing_delivery.description = delivery.get('description')

        db.session.merge(existing_delivery)
        db.session.commit()

        return print(delivery_schema.dump(existing_delivery))
    else:
        abort(404, message=f"Delivery with id: {id}, not found")

def delete_delivery(id):

    existing_delivery = Delivery.query.filter(Delivery.id == id).one_or_none()

    if existing_delivery:
        db.session.delete(existing_delivery)
        db.session.commit()

        return print(delivery_schema.dump(existing_delivery))
    else:
        abort(404, message=f"Delivery with id: {id}, not found")

with app.app_context():
    read_all_clients()