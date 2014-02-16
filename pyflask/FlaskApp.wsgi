import sys,os

PROJECT_DIR = '/home/auron/Projects/FlaskApp/pyflask'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR + '/App')

from FlaskApp import app as application
