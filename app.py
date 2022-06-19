from project import create_app

app, blueprint = create_app('flask.cfg')

app.run()