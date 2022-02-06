from uncodejupyterplugin.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'uncodejupyterplugin',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "uncodejupyterplugin",
        "src": "static",
        "require": "uncodejupyterplugin/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp)
    