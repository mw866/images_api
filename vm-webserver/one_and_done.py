from flask import Flask, request, abort
import os
import requests
from StringIO import StringIO
from wand.image import Image
from urlparse import urlparse 
from tempfile import NamedTemporaryFile
import commands
# import datetime
import logging


url_tmpfile_dict = {}
app = Flask(__name__)	
# handler = logging.FileHandler('flask.log')
# handler.setLevel(logging.INFO)
# app.logger.addHandler(handler)

@app.route("/")
def home():
	return "<a href='http://images.chriswang.tech/api/num_colors?src=https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png'>Click here to try this API example.</a>"

@app.route("/api/num_colors")
def num_colors():
	global url_count_dict 
	tmpfilepath = ""
	url = request.args.get('src')
	# if not cached
	if url not in url_tmpfile_dict:
		app.logger.info("cache: miss")
		r = requests.get(url, timeout=5)
		f, file_ext = os.path.splitext(os.path.basename(urlparse(url).path))
		if 'image' not in r.headers['content-type']:
			app.logger.error(url + " is not an image.")
			abort(400, url + " is not an image.")
		with Image(file=StringIO(r.content)) as img:
			with  NamedTemporaryFile(mode='w+b',suffix=img.format, delete=False) as temp_file:
				img.save(file=temp_file)
				temp_file.seek(0,0)
				url_tmpfile_dict[url] = temp_file.name
				tmpfilepath = temp_file.name
	else: 	# if cached
		app.logger.info("cache: hit at")
		tmpfilepath = url_tmpfile_dict[url]
	app.logger.info(tmpfilepath)
	command = "/usr/bin/identify -format %k " + tmpfilepath
	color_count = commands.getoutput(command)
	return color_count

if __name__ == "__main__":
	app.run() #if run locally ane exposed to public network
