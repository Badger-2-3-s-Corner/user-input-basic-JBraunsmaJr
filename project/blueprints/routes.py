from . import my_app

@my_app.route('/')
def hello_world():
    return "Hello World!"