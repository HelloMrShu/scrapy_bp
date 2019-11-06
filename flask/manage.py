#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app
from flask_script import Manager

# from flask_migrate import MigrateCommand

# 从环境变量中获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)

# 调试模式，模板代码修改立即生效. 等价于 TEMPLATES_AUTO_RELOAD = True
app.config['DEBUG'] = True

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
