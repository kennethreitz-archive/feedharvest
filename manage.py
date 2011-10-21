#!/usr/bin/env python
# -*- coding: utf-8 -*-

from feedharvest import app
from flaskext.script import Manager, Command


manager = Manager(app)


@manager.command
def hello():
    """Hello World!"""
    print r'\o/'


if __name__ == "__main__":
    manager.run()