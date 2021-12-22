"""
CRUD Operations
- We will show our CRUD operations being performed manually in a .py script.
- Keep in mind, this is just to understand the syntax, typically a lot of this will be automated with Flask.
"""

from flask_and_database import db, Person

####################
# Create Operation #
####################

# gender field info is not passed deliberately in order to learn about flask migrate
person4 = Person("Jack", 35)
person5 = Person("Jill", 32)
db.session.add_all([person4, person5])
db.session.commit()

##################
# Read Operation #
##################

# Read all
all_person = Person.query.all()
print(all_person)

# Read one - By ID
person1 = Person.query.get(1)
print(person1, person1.name, person1.age)

# Filter -> You can also get filter query written by this method
person_name = Person.query.filter_by(name='Susan')
print(person_name.all()) # This will return a list of all the objects that match the filter

####################
# Update Operation #
####################

person3 = Person.query.get(3)
person3.name = "Shubham"
db.session.add(person3)
db.session.commit()


####################
# Delete Operation #
####################

person2 = Person.query.get(2)
db.session.delete(person2)
db.session.commit()


# Let's now see our database
print("Last - ", Person.query.all())
