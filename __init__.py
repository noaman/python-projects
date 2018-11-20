#from flask import Flask

#from flask import Blueprint, render_template, abort



#app = Flask(__name__)
#@app.route("/")
#def index():
#	return render_template("index.html")


#@app.route("/yt")
#def yt_downloader():
#	return render_template("yt_downloader.html")


#if __name__ == "__main__":
#   app.run(debug= True)

#When installing on EC2 aws for pip3 install use the below command
#sudo -H pip3 install <name of library>


from flask import (Flask)




#this is for localhost
from .routes import *

#this is for server on ec2
#from routes import *

app = Flask(__name__)
app.secret_key = 'jhshs%545343543HHH**£223££##€€'
app.register_blueprint(routes)

if __name__ == "__main__":
   app.run(debug= True)

