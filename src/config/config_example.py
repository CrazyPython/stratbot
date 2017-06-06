config = {

    # details required to login to twitch IRC server
    'server': 'irc.twitch.tv',
    'port': 6667,
    'username': 'twitch_username',
    'oauth_password': 'oauth:yxualcmmtixlodszt0n4te66f3yzzl',

    # channel to join
    'channels': ['#stockstream'],

    'cron': {
        '#stockstream': {
            'run_cron': True,
            'run_time': 300,  # time in seconds
            'cron_messages': [
                '!sell AMD'
            ]
        },
    },

    # if set to true will display any data received
    'debug': False,

    # if set to true will log all messages from all channels
    # todo
    'log_messages': True,

    # maximum amount of bytes to receive from socket - 1024-4096 recommended
    'socket_buffer_size': 2048
}
