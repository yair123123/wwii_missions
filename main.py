from flask import Flask
from controllers.missions_controller import missions_blueprint
from model import *



app = Flask(__name__)
app.register_blueprint(missions_blueprint, url_prefix='/api/mission')


if __name__ == '__main__':
    # create_tables()
    app.run()