from flask import Blueprint, request, jsonify
from ..utils import analyze_from_web, analyze_doc, analyze_sentence
import os

sentiment_routes = Blueprint('sentiment_routes', __name__)


upload_folder = '/app/tmp'  # Temporary upload folder for files
allowed_extensions = {'txt', 'csv'}


def allowed_file(filename):
    """
    Checks if the uploaded file has an allowed extension.

    This function checks if the provided filename has a valid extension that is included
    in the list of predefined allowed extensions. The check is case-insensitive and the
    function expects the filename to include an extension separated by a dot (.)

    :param filename: str
        The file name to check
    :return: boolean
        True if condition passes
        False if condition fails
    """

    if '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions:
        return True
    else:
        return False


@sentiment_routes.route('/', methods=['GET'])
def hello():
    """
    Hello function for greeting the user!

    :return: str
        Greet/Welcome message
    """
    return 'Welcome! Let\'s get analyzing'


@sentiment_routes.route('/web', methods=['GET'])
def sentiment_from_web():
    """
    Gets sentiment from text gotten from the web.

    This function gets the URL of a website as a query parameter and downloads
    the text from that website by calling the analyze_from_web() function.

    :return: str
        Sentiment/Polarity of the analyzed text
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
    Gets sentiment from text read from an uploaded document.

    This function receives a document of a specified file type and reads the
    text found in the file by calling the analyze_doc() function to get the
    sentiment of the text.

    :return: str
        Sentiment/Polarity of the analyzed text
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


@sentiment_routes.route('/sentence', methods=['GET'])
def sentiment_from_sentence():
    """
    Gets sentiment from a given sentence.

    This function receives a sentence as a query parameter and gets the
    sentiment of it by calling the analyze_sentence() function.

    :return: str
        Sentiment/Polarity of the analyzed text
    """

    sentence = request.args.get('sentence')
    try:
        if not sentence:
            return jsonify({
                "status": "fail",
                "message": "No sentence found! Please insert sentence."
            }), 400
        else:
            sentiment_category = analyze_sentence(sentence)
            return jsonify({
                "Status": "success",
                "sentiment": sentiment_category
            }), 200
    except Exception as e:
        return jsonify({
            "status": "fail",
            "message": str(e)
        }), 500
