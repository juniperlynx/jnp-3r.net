import os
import publ

config = {
    'database_config': {
        'provider': 'sqlite',
        'filename': 'index.db'
    },
}
app = publ.publ(__name__, config)
