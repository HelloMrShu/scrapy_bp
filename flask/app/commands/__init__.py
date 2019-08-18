#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask_script import Manager, Command
from app.commands.poi2es import PoiElastic

TaskCommand = Manager()

TaskCommand.add_command('poi2es', Command(PoiElastic.create_index))

if __name__ == '__main__':
    TaskCommand.run()

