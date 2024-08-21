import logging
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import main  # Import your main processing code

# Enable debugging and set up logging
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# Add debug logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/process-audio', methods=['POST'])
def process_audio():
    logging.debug("Received request at /process-audio")

    api_key = request.form.get('api_key')
    audio_file = request.files.get('audio')

    logging.debug(f"API Key: {api_key}")
    logging.debug(f"Audio File: {audio_file}")

    if not api_key or not audio_file:
        logging.error("API key or audio file missing")
        return jsonify({'error': 'API key and audio file are required'}), 400

    # Ensure the directory exists
    if not os.path.exists('uploaded_audio'):
        os.makedirs('uploaded_audio')

    file_path = os.path.join('uploaded_audio', audio_file.filename)
    audio_file.save(file_path)
    logging.debug(f"Saved file to {file_path}")

    try:
        text, summary = main.process_audio(file_path, api_key)

        # Delete the uploaded file after processing
        os.remove(file_path)

        # Get base filename without extension
        base_name = os.path.splitext(audio_file.filename)[0]

        # Create paths for transcription and summary
        transcription_filename = f"{base_name}_transcription.txt"
        summary_filename = f"{base_name}_summary.txt"

        transcription_path = os.path.join('text_transcription', transcription_filename)
        summary_path = os.path.join('text_summarize', summary_filename)

        logging.debug("Processing complete, sending response")
        return jsonify({
            'transcribed_text': text,
            'summarized_text': summary,
            'transcription_link': f'/text_transcription/{transcription_filename}',
            'summary_link': f'/text_summarize/{summary_filename}'
        }), 200
    except Exception as e:
        logging.error(f"Error processing audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/text_transcription/<filename>', methods=['GET'])
def download_transcription(filename):
    return send_from_directory('text_transcription', filename)

@app.route('/text_summarize/<filename>', methods=['GET'])
def download_summary(filename):
    return send_from_directory('text_summarize', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
