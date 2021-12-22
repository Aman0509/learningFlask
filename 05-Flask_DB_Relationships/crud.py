from models import Citizen, Vehicle, DriversLicense, db


# Create some citizens
c1 = Citizen('John')
c2 = Citizen('Jane')
c3 = Citizen('Jack')

# Adding to the database
db.session.add_all([c1, c2, c3])
db.session.commit()

# Query the citizens
print(Citizen.query.all())
print("*"*50)

# Let's create drivers license and vehicle owned by Jane
jane_details = Citizen.query.filter_by(name='Jane').first()
dl1 = DriversLicense('12345', jane_details.id)
v1 = Vehicle('car', 'Toyota', jane_details.id)
v2 = Vehicle('bike', 'Honda', jane_details.id)

db.session.add_all([dl1, v1, v2])
db.session.commit()

# Let's see the details of Jane
jane_details = Citizen.query.filter_by(name='Jane').first()
print(jane_details)
jane_details.get_vehicles()