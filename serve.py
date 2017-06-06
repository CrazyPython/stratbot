#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config import config

bot = Roboraj(config).run()
