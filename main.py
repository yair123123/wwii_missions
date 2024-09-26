from flask import Flask
from controllers.missions_controller import missions_blueprint
from repository.database import create_tables, drop_table
from model import *
from repository.target_un_normal import get_targets
from service.target_un_normal import load_targets


app = Flask(__name__)
app.register_blueprint(missions_blueprint, url_prefix='/api/mission')

# if __name__ == '__main__':
#     drop_table()
#     create_tables()
#     load_targets(get_targets())

if __name__ == '__main__':
    # create_tables()
    app.run()