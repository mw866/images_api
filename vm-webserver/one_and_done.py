from flask import Flask, request, abort,  make_response, redirect
import os
import requests
from StringIO import StringIO
from wand.image import Image
from wand.exceptions import MissingDelegateError
from urlparse import urlparse 
from tempfile import NamedTemporaryFile
import commands

app = Flask(__name__)

@app.route("/")
def home():
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
			command = "/usr/bin/identify -format %k "+temp_file.name
			color_count = commands.getoutput(command)
			temp_file.close()
			return color_count
	except MissingDelegateError:
		abort(400, 'Image is unusable')


if __name__ == "__main__":
	app.run() #if run locally ane exposed to public network
