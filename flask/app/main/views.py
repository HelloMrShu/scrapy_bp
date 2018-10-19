from . import main
<<<<<<< Updated upstream
=======
from flask import render_template
from app.models import Image
>>>>>>> Stashed changes
 
# from flask import render_template,redirect,url_for
 
@main.route("/")
def index():
<<<<<<< Updated upstream
	return "<h3>这是前台页面</h3>"
=======
	image_list = Image.query.all()
	return render_template('image.html', images=image_list,msg='123')
>>>>>>> Stashed changes
