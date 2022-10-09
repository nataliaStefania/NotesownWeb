from flask import Flask

from config import config

#Routes
from routes import routsUsuarios
from routes import routsCarpetas
from routes import routsNotas

app=Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>",404

if __name__ =='__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(routsUsuarios.main, url_prefix='/api/users')
    app.register_blueprint(routsCarpetas.main, url_prefix='/api/folders')
    app.register_blueprint(routsNotas.main, url_prefix='/api/notes')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()

# main = Blueprint('carpeta_blueprint',  __name__)