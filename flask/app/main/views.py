from . import main
 
# from flask import render_template,redirect,url_for
 
@main.route("/")
def index():
	return "<h3>这是前台页面</h3>"