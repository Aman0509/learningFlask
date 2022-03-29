# RESTAPI in Flask

## Understanding REST

- So far we've only visited our sites manually.
- This means needing to serve information visually through templates and views.
- But what if we just wanted direct information access?
- What if we wanted a server to directly access our database.

<br/>

*REST stands for **Representational State Transfer**. It allows us to provide interactions and operations between computer systems online.\
REST is a standardized way for communication between computer systems on the web. Systems that support and are compliant with REST are often known as RESTful.*


## Understand REST use cases

- When to use REST and implement it in your own project will depend heavily on your final goal.
- If you have no intention of automated systems communicating with your website, then you probably don't need to implement REST.

Example:
1. Web Site for an Art Gallery
   - You may only intend people to visit the site to see the pictures. REST probably not necessary, but always depends on the situation.

2. Web Site for Online Store
   - You may only intend people to manually shop online, in which case you don't implement REST.
   - But maybe the site grows in popularity, and users want to create scripts to directly access items for sale programmatically.
   - Either they can scrape the site Or you can provide a *REST API (Application Programming Interface)* for them to interact with.

## Be able to implement basic REST API with Flask Web Application

- There are many options available for implementing a REST API with Flask.
- One of the easiest to use and most popular is the Flask-Restful library.


### Study References
- [Flask Restful Docs](https://flask-restful.readthedocs.io/en/latest/)
- [Flask JWT](https://pythonhosted.org/Flask-JWT/)
