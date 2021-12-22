"""
Normally, we do not set up a database in a script like we are doing here.
It is being handled by CLI tools which we will see later.
"""

from flask_and_database import db, Person


# Create the tables based on the models defined in your flask app
db.create_all()

# Once you have created the tables, you can add some data to them - Create Operation
# gender field info is not passed deliberately in order to learn about flask migrate
person1 = Person("John", 36)
person2 = Person("Susan", 33)
person3 = Person("Bob", 28)

# Add above data to the database
db.session.add_all([person1, person2])

# You can also add data individually like this
db.session.add(person3)

# Commit the changes to the database
db.session.commit()

print(person1, person2, person3)

