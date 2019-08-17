from flask_script import Manager, Command

TaskCommand = Manager()

from .poi2es import *

TaskCommand.add_command('poi', Command(poi))
