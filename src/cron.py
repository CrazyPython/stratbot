from src.config import *
from src.functions_general import *

from src.functions_general import *


class cron:
    def __init__(self, irc, channel):
        self.messages = config['cron'][channel]['cron_messages']
        self.run_time = config['cron'][channel]['run_time']
        self.last_index = 0
        self.irc = irc
        self.channel = channel
        self.waiting = True

    @staticmethod
    def get_next_message():
        with open("schedule.txt", "r") as f:
            messages = f.readlines()
            writeback = '\n'.join(messages[1:])
        with open("schedule.txt", "w") as f:
            f.write(writeback)
        return messages[0]

    def callback(self):
        self.waiting = False

    def run(self):
        self.irc.pingback = lambda: self.callback()
        while self.waiting:
            time.sleep(1)
        while True:
            index = self.get_next_message()
            print(index)

            pbot('[CRON] %s' % index, self.channel)

            self.irc.send_message(self.channel, index)

            self.last_ran = time.time()

            time.sleep(self.run_time)
