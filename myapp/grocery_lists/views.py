from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Grocery
from myapp.grocery_lists.forms import GroceryForm

grocery_lists = Blueprint('grocery_lists', __name__)

@grocery_lists.route('/create', methods=['GET', 'POST'])
@login_required
def create_list():
  form = GroceryForm()
  if form.validate_on_submit():
    grocery = Grocery(name=form.name.data, quantity=form.quantity.data, unit=form.unit.data, user_id=current_user.id)
    db.session.add(grocery)
    db.session.commit()
    flash('Grocery Created')
    print('Grocery was created')
    return redirect(url_for('core.index'))
  return render_template('create_list.html', form=form)

@grocery_lists.route('/<int:grocery_id>')
def grocery(grocery_id):
    grocery = Grocery.query.get_or_404(grocery_id) 
    return render_template('grocery.html', name=grocery.name, quantity=grocery.quantity, unit=grocery.unit, grocery=grocery)

@grocery_lists.route('/<int:grocery_id>/update', methods=['GET', 'POST'])
@login_required
def update(grocery_id):
  grocery = Grocery.query.get_or_404(grocery_id)

  if grocery.author != current_user:
    abort(403)

  form = GroceryForm()

  if form.validate_on_submit():
      grocery.name = form.name.data
      grocery.quantity = form.quantity.data
      grocery.unit = form.unit.data
      db.session.commit()
      flash('Grocery Updated')
      return redirect(url_for('grocery_lists.grocery',grocery_id=grocery.id))

  elif request.method == 'GET':
    form.name.data = grocery.name
    form.quantity.data = grocery.quantity
    form.unit.data = grocery.unit

  return render_template('create_list.html',title='Updating',form=form)

@grocery_lists.route('/<int:grocery_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_list(grocery_id):

  grocery = Grocery.query.get_or_404(grocery_id)
  if grocery.author != current_user:
    abort(403)

  db.session.delete(grocery)
  db.session.commit()
  flash('Grocery Deleted')
  return redirect(url_for('core.index'))

