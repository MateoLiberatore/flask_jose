from config import db, ma
from sqlalchemy.orm import relationship

class Delivery(db.Model):

    __tablename__ = 'Delivery'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Client_id = db.Column(db.Integer, db.ForeignKey('Clients.id'))
    description = db.Column(db.String(50))

    clients = relationship("Client", back_populates="deliveries")


class Client(db.Model):

    __tablename__ = 'Clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))

    deliveries = relationship("Delivery", back_populates="clients")
    

class DeliverySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Delivery
        load_instance = True
        sqla_session = db.session


class ClientSchema(ma.SQLAlchemyAutoSchema):

    deliveries = ma.Nested(DeliverySchema, many=True)
    class Meta:
        model = Client
        load_instance = True
        sqla_session = db.session

    



delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)