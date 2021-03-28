from flask import Blueprint, render_template, request
from datetime import datetime

home = Blueprint('home', __name__, template_folder="templates", static_folder='../static')

def get_time():
    '''Returns the current time as a YYYY/MM/DD HH/MM/SS string object
    Parameters
    ------
    None
    
    Returns
    ------
    time_string: `string`
    '''
    time = datetime.now()
    time_string = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_string


@home.route("/", methods=['GET', 'POST'])
def index():
    time_string = get_time()
    return render_template('index.html', time=time_string)