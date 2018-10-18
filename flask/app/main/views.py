from . import main
#from app.models import Image
 
# from flask import render_template,redirect,url_for
 
@main.route("/")
def index():
	#image_list = Image.query.all()
	#print(image_list)
	return "<h3>这是前台页面</h3>"