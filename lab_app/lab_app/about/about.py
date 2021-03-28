from flask import Blueprint, render_template
from datetime import datetime

about = Blueprint('about', __name__, template_folder="templates", static_folder='../static')

def get_time():
    time = datetime.now()
    time_string = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_string


@about.route('/about', methods=["GET"])
def index():
    time_string = get_time()
    return render_template('about.html', time=time_string)