from . import main
from flask import render_template
from app.models import Image
  
@main.route("/")
def index():
	image_list = Image.query.all()
	return render_template('image.html', images=image_list,msg='123')
