from app.routes import create_app
import nltk

nltk.download('punkt', download_dir='/opt/render/nltk_data')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
