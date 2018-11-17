from . import main
from flask import render_template
from app.models import Image
from flask import request
  
@main.route('/')
def hello():
	return 'Hello Flask !';

@main.route('/list', methods=['GET'])
def index():
	page = int(request.args.get('page') or 1)
	perpage = int(request.args.get('perpage') or 15)

	paginate = Image.query.paginate(page, perpage, error_out=False)
	image_list = paginate.items
	return render_template('image.html', images=image_list, paginate=paginate)
