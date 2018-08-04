import logging
import datetime

from app_in_error import app


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename='app{}.log'.format(datetime.datetime.now()),
                        level=0)

    logging.info(': App started')
    app.config["DEBUG"] = False
    app.run()
