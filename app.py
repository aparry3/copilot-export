from config import app
from routes.programs import programs_api

app.register_blueprint(programs_api)

if __name__ == '__main__':
    app.run()
