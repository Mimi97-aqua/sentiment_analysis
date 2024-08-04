# Sentiment Analysis

## Overview

This API provided endpoints for sentiment analysis for the following sources:
- Web page URLs
- Uploaded documents of file types `.txt` and `.csv`
- Directly provided sentences

The different sentiment types are:

| Sentiment Type | Polarity Value (p) |
|----------------|--------------------|
| Postive        | p > 0              |
| Negative       | p < 0              |
| Neutral        | p = 0              |


It uses:
- **Flask**: for the web framework
- **TextBlob**: for sentiment analysis
- **NewsPaper**: for downloading articles from the web

````python
pip install nltk, flask, newspaper3k, textblob
````

**Note:** This API is hosted [here.](https://sentiment-analysis-8nic.onrender.com) You can use this link to test the endpoints as an alternative to local setup. 

## Installation
1. **Clone this repository**

```gitignore
git clone https://github.com/Mimi97-aqua/sentiment_analysis.git
cd <repo-dir>
```

2. **Create and activate virtual environment**

```python
python -m venv .venv
source .venv/Scripts/activate  # On Windows OS
```

3. **Install required packages**

`pip install -r requirements.txt`


## Configuration
1. **Setup the upload folder**

- The upload folder is used for temporarily storing uploaded documents. The files
in this folder are deleted after processing is over in order to free up space.

- Ensure the `app/tmp` directory exists or modify the `upload_folder` path in the code
to a directory of your choice.


## Usage
1. **Start the Flask application**

To achieve this, run `main.py`

2. **Endpoints**

**Base endpoint:** `/api`

- **GET `/`**
  - Returns a welcome message.
  

- **GET `/web`**
  - _Query paramter_: `url` (string)
  - _Description_: Analyzes the sentiment from the text of the provided webpage URL
  - _Response_:
  ```json
  {
    "status": "success",
    "sentiment": "positive" // or "negative" or "neutral"
  }
  ```
- **POST `/doc`**
  - _Form data_: `file` (file)
  - _Description_: Analyzes sentiment from the text of the uploaded document.
  - _Response_:
  ```json
   {
      "status": "success",
      "sentiment": "positive" // or "negative" or "neutral"
   }
    ```

- **GET `/sentence`**
  - _Query parameter_: `sentence` (string)
  - _Description_: Analyzes the sentiment from a provided sentence
  - _Response_:
    ```json
     {
        "status": "success",
        "sentiment": "positive" // or "negative" or "neutral"
     }
      ```

## Error Handling 

This API responds with appropriate error messages and status codes for issues such as missing parameters or invalid file types.

## Contributing

1. Fork this repository and clone your fork.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.
