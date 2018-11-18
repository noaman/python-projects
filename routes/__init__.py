from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .yt_downloader import *
from .tw_analyzer import *






if __name__ == '__main__':                
    app.run(debug=True)



#AWS code deploy access
#access key :AKIAITDOVL4MLVPWNHWA
#Secret key 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