from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route("/")
def hello():
    # return "Hello goorm!"
    return render_template('index.html')


if __name__ == "__main__":
    # application.run(host='0.0.0.0', port=int(sys.argv[1]))
    application.run(host='0.0.0.0', port=8000, debug=True)
