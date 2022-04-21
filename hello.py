from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return '<p> Hello World </p>'


@app.route('/products')
def products():
    response = jsonify([
        {
            'title': 'Caneca Personalizada de Porcelana',
            'amount': 123.45,
            'installments': {'number': 3, 'total': 41.15, 'hasFee': True}
        },
        {
            'title': 'Caneca de Tulipa',
            'amount': 123.45,
            'installments': {'number': 3, 'total': 41.15}
        }
    ])

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
