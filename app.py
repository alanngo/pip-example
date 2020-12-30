from flask import *
from flask_cors import *
from util.error_advice import advice

app = Flask(__name__)
app.register_blueprint(advice)


@app.route('/', methods=['GET'])
def index():
    return \
        {
            "name": "omruti",
            "fav_stuff": ["Harry Potter", "django", "SQL", "Linus", "Tom and Jerry", "TABS"],
            "has_real_computer": False
        }


if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()
