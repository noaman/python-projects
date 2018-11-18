from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .yt_downloader import *
from .tw_analyzer import *


if __name__ == '__main__':                
    app.run(debug=True)