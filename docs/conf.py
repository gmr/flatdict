import datetime
import importlib.metadata

master_doc = 'index'
project = 'flatdict'
release = version = importlib.metadata.version('flatdict')
year = datetime.datetime.now(tz=datetime.UTC).year
copyright = f'{year}, Gavin M. Roy'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
