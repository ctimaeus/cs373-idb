# flask imports
from flask import request, \
                  session, \
                  g, \
                  redirect, \
                  url_for, \
                  abort, \
                  render_template, \
                  flash, \
                  jsonify

# app configuration imports
from config import app, \
                   manager

# unit test imports
from io import StringIO
from models import Cocktail
from tests import TestIdb
from unittest import TextTestRunner, \
                     makeSuite
import json



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cocktails/<int:id_>')
def cocktails(id_):
    return render_template('index.html', cocktail_id=id_)


@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@app.route('/api/cocktail', methods=['GET'])
def api_cocktail_list():
    results = []
    for c in Cocktail.query.all():
        results.append({'name': c.name, 'id': c.id_})

    return json.dumps(results)
    

@app.route('/api/cocktail/<int:id_>', methods=['GET'])
def api_cocktail(id_):
    return ('', 501)


@app.route('/api/cocktail/<int:id_>/name', methods=['GET'])
def api_cocktail_name(id_):
    return ('', 501)


@app.route('/api/cocktail/<int:id_>/ingredients', methods=['GET'])
def api_cocktail_ingredients(id_):
    return ('', 501)


@app.route('/api/cocktail/<int:id_>/glass', methods=['GET'])
def api_cocktail_glass(id_):
    return ('', 501)


@app.route('/api/cocktail/<int:id_>/recipe', methods=['GET'])
def api_cocktail_recipe(id_):
    return ('', 501)


@app.route('/api/cocktail/<int:id_>/image', methods=['GET'])
def api_cocktail_image(id_):
    return ('', 501)


@app.route('/api/ingredient', methods=['GET'])
def api_ingredient_list():
    return ('', 501)


@app.route('/api/ingredient/<int:id_>', methods=['GET'])
def api_ingredient(id_):
    return ('', 501)


@app.route('/api/ingredient/<int:id_>/name', methods=['GET'])
def api_ingredient_name(id_):
    return ('', 501)


@app.route('/api/ingredient/<int:id_>/cocktails', methods=['GET'])
def api_ingredient_cocktails(id_):
    return ('', 501)


@app.route('/api/ingredient/<int:id_>/image', methods=['GET'])
def api_ingredient_image(id_):
    return ('', 501)


@app.route('/api/ingredient/<int:id_>/numcocktails', methods=['GET'])
def api_ingredient_numcocktails(id_):
    return ('', 501)


@app.route('/tests', methods=['GET'])
def run_unittests():
    """
    Runs unit tests and returns the result.
    """
    io = StringIO()
    TextTestRunner(stream=io, verbosity=2).run(makeSuite(TestIdb))
    results = io.getvalue().split('\n')
    # return results
    return render_template("tests.html", text=results)

if __name__ == '__main__':
    manager.run()
