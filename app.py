import os
import publ

config = {
    'database_config': {
        'provider': 'sqlite',
        'filename': 'index.db'
    },
}
app = publ.publ(__name__, config)

@app.route('/favicon.ico')
def favicon():
    """ Send the favicon.ico file directly from this directory """
    return flask.redirect(flask.url_for('static', filename='favicon.ico'))
