from flask import Blueprint, request, jsonify
from ..utils import analyze_from_web, analyze_doc
import os

sentiment_routes = Blueprint('sentiment_routes', __name__)


upload_folder = 'app/tmp'  # Temporary upload folder for files
allowed_extensions = {'txt', 'text', 'csv'}


def allowed_file(filename):
    """

    :param filename:
    :return:
    """
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions:
        return True
    else:
        return False


@sentiment_routes.route('/', methods=['GET'])
def hello():
    return 'Welcome! Let\'s get analyzing'


@sentiment_routes.route('/web', methods=['GET'])
def sentiment_from_web():
    """

    :return:
    """
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


@sentiment_routes.route('/doc', methods=['POST'])
def sentiment_from_doc():
    """

    :return:
    """
    if 'file' not in request.files:
        return jsonify({
            "status": "fail",
            "message": "No file path found in this request"
        }), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({
            "status": "fail",
            "message": "No file was selected. Please select a file!"
        }), 400

    if file and allowed_file(file.filename):
        file_name = file.filename
        file_path = os.path.join(upload_folder, file_name)
        file.save(file_path)

        try:
            sentiment_category = analyze_doc(file_path)
            os.remove(file_path)  # Remove file after processing to free up space
            return jsonify({
                "status": "success",
                "sentiment": sentiment_category
            }), 200
        except Exception as e:
            os.remove(file_path)  # Does same as above even if an error occurs
            return jsonify({
                "status": "fail",
                "message": str(e)
            }), 500
    else:
        return jsonify({
            "status": "fail",
            "message": f"Invalid file type. Only the following files are allowed:"
                       f"{allowed_extensions}"
        }), 400
