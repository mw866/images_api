from flask import Flask
from flask import send_file, request, abort, jsonify, send_from_directory, make_response, redirect, current_app
import os
import requests
from StringIO import StringIO
from wand.image import Image, GRAVITY_TYPES
from wand.exceptions import MissingDelegateError
from urlparse import urlparse 
from tempfile import NamedTemporaryFile
import commands
# from shutil import copyfileobj
# from functools import wraps, update_wrapper
# from datetime import datetime
# import logging
# from gevent import monkey; monkey.patch_all()

app = Flask(__name__)

@app.route("/")
def hello():
	return "To use the API, the URL must be `images.chriswang.tech/api/num_colors?src=https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png`."

@app.route("/api/num_colors")
def num_colors():
	url = request.args.get('src')
	try:
		r = requests.get(url, timeout=1)
		filename, file_ext = os.path.splitext(os.path.basename(urlparse(url).path))
		if 'image' not in r.headers['content-type']:
			app.logger.error(url + " is not an image.")
			abort(400, url + " is not an image.")
	except:
		app.logger.exception("Error while getting url: " + url)
	try:
		with Image(file=StringIO(r.content)) as img:
			temp_file = NamedTemporaryFile(mode='w+b',suffix=img.format, delete=False)
			img.save(file=temp_file)
			temp_file.seek(0,0)
			command = "identify -format %k "+temp_file.name
			temp_file.close()
			print command
			color_count = commands.getoutput(command)
			print color_count			
			return color_count
	except MissingDelegateError:
		abort(400, 'Image is unusable')


if __name__ == "__main__":
	app.run() #if run locally ane exposed to public network
