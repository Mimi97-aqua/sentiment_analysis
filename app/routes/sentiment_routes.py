from flask import Blueprint, request, jsonify
from ..utils import *

sentiment_routes = Blueprint('sentiment_routes', __name__)


@sentiment_routes.route('/', methods=['GET'])
def hello():
    return 'Welcome! Let\'s get analyzing'
