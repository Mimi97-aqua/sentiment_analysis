from flask import Blueprint, request, jsonify
from ..utils import analyze_from_web

sentiment_routes = Blueprint('sentiment_routes', __name__)


@sentiment_routes.route('/', methods=['GET'])
def hello():
    return 'Welcome! Let\'s get analyzing'


@sentiment_routes.route('/web', methods=['GET'])
def sentiment_from_web():
    url = request.args.get('url')
    if not url:
        return jsonify({
            "status": "fail",
            "message": "URL parameter is missing. Insert it!"
        }), 400

    try:
        sentiment_category = analyze_from_web(url)
        return jsonify({
            "status": "success",
            "sentiment": sentiment_category
        }), 200
    except Exception as e:
        return jsonify({
            "status": "fail",
            "message": str(e)
        }), 500