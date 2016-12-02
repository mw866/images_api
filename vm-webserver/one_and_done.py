from flask import Flask, request, abort
import os
import requests
from urlparse import urlparse 
from tempfile import NamedTemporaryFile
import commands
import logging



url_colorcount_dict = {}
app = Flask(__name__)	
# handler = logging.FileHandler('/var/log/flask/error.log')
# handler.setLevel(logging.ERROR)
# app.logger.addHandler(handler)

@app.route("/")
def home():
	return "<a href='http://images.chriswang.tech/api/num_colors?src=https://s3.amazonaws.com/startup-systems-final-images/6461517483.jpg'>Click here to try this API example.</a>"

@app.route("/api/num_colors")
def num_colors():
	global url_colorcount_dict 
	tmpfilepath = ""
	url = request.args.get('src')
	# if not cached
	if url not in url_colorcount_dict:
		app.logger.info("cache: miss")
		r = requests.get(url, timeout=5)
		f, file_ext = os.path.splitext(os.path.basename(urlparse(url).path))
		if 'image' not in r.headers['content-type']:
			app.logger.error(url + " is not an image.")
			abort(400, url + " is not an image.")
		with  NamedTemporaryFile(mode='w+b',suffix=file_ext, delete=False) as temp_file:
			temp_file.write(r.content)
			temp_file.seek(0,0)
			command = "/usr/bin/identify -format %k " + temp_file.name
			app.logger.debug(command)
			colorcount = commands.getoutput(command)
			url_colorcount_dict[url] = colorcount

	else: 	# if cached
		app.logger.debug("cache: hit")
		colorcount = url_colorcount_dict[url]
	app.logger.debug(colorcount)
	return colorcount

if __name__ == "__main__":
	app.run() #if run locally ane exposed to public network
