# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Grocery

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    grocery_lists = Grocery.query.order_by(Grocery.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', grocery_lists=grocery_lists)

@core.route('/info')
def info():
    return render_template('info.html')