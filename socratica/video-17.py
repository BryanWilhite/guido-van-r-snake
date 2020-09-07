import logging

LOG_FORMAT = '%(levelname)s: %(asctime)s - %(message)s'

logging.basicConfig(
    filename='./video-17.log',
    filemode='a',   # open for writing, appending to the end of the file if it exists
                    # [ 📖 https://docs.python.org/3/library/functions.html#filemodes ]
    level=logging.DEBUG,
    format=LOG_FORMAT)

logger = logging.getLogger()

logger.info('Our first message.')
