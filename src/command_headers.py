from src.config import *

commands = {
}

for channel in config['channels']:
    for command in commands:
        commands[command][channel] = {}
        commands[command][channel]['last_used'] = 0
