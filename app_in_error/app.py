import flask

import datetime
import logging

app = flask.Flask(__name__)


@app.errorhandler(500)
def handle_bad_request(e):
    return flask.render_template('error.html')


@app.errorhandler(404)
def handle_bad_request(e):
    logging.exception(': 404')
    return flask.render_template('404_page.html')


@app.route('/')
def index():
    return 'index page'


@app.route('/feature')
def feature():

    raise NotImplementedError

    return 'feature page'


@app.route('/user')
def user():
    number = 1 // 2

    return number


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename='app{}.log'.format(datetime.datetime.now()),
                        level=0)

    logging.info(': App started')
    app.config["DEBUG"] = False
    app.run()
