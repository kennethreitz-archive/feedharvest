# -*- coding: utf-8 -*-

"""
feedharvest.core
~~~~~~~~~~~~~~~~

This module provides the FeedHarvest entrypoint.
"""

from flask import Flask, request

app = Flask(__name__)


if __name__ == '__main__':
    app.run()

