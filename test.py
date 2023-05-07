import time
import random
import logging
import sys

logging.basicConfig(filename=sys.argv[1],
                    format='%(name)s- %(levelname)s - %(asctime)s %(message)s',
                    filemode='a+')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.NOTSET)

i = 0
while True:
    error  = random.randint(0, 4)
    if error == 0:
        logger.debug(f"{i}|Harmless debug Message")
    elif error == 1:
        logger.info(f"{i}|Just an information")
    elif error == 2:
        logger.warning(f"{i}|Its a Warning")
    elif error == 3:
        logger.error(f"{i}|Did you try to divide by zero")
    else:
        logger.critical(f"{i}|Internet is down")

    wait  = random.uniform(0,2)
    time.sleep(wait)
    i += 1
