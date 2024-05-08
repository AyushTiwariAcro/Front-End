from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_KEY = 'YOUR_RAPIDAPI_KEY'  # Replace with your RapidAPI key

@app.route('/translate', methods=['POST'])
def translate():
    try:
        text = request.form['text']
        source_lang = request.form['source']
        target_lang = request.form['target']

        response = requests.post(
            'https://google-translate1.p.rapidapi.com/language/translate/v2',
            headers={
                'content-type': 'application/json',
                'x-rapidapi-host': 'google-translate1.p.rapidapi.com',
                'x-rapidapi-key': RAPIDAPI_KEY
            },
            json={
                'q': text,
                'source': source_lang,
                'target': target_lang
            }
        )

        if response.status_code == 200:
            translated_text = response.json()['data']['translations'][0]['translatedText']
            return jsonify({'translatedText': translated_text})
        else:
            return jsonify({'error': 'Translation error'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)