import os
import whisper
import warnings
import openai
from datetime import datetime
import logging
from pathlib import Path
import subprocess

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

warnings.filterwarnings("ignore", category=FutureWarning,
                        message="You are using `torch.load` with `weights_only=False`")

class FileWriter:
    def __init__(self, directory: str):
        self.directory = directory
        self.ensure_directory_exists()

    def ensure_directory_exists(self):
        os.makedirs(self.directory, exist_ok=True)

    def write_to_file(self, filename: str, content: str):
        file_path = os.path.join(self.directory, filename)
        with open(file_path, "w") as f:
            f.write(content)
        logging.info(f"Content saved to {file_path}")

class AudioProcessor:
    def __init__(self):
        logging.info("Loading Whisper model...")
        self.model = whisper.load_model("base")
        logging.info("Whisper model loaded.")

    def transcribe_audio(self, file_path: str) -> str:
        try:
            logging.info(f"Attempting to transcribe file: {file_path}")
            result = self.model.transcribe(file_path)
            logging.info(f"Transcription result: {result['text']}")
            return result['text']
        except Exception as e:
            logging.error(f"Error transcribing audio: {e}")
            return ""

    def summarize_text(self, text: str, api_key: str) -> str:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                {"role": "system",
                    "content": "You are an assistant that summarizes audio texts in French."},
                {"role": "user", "content": f"Résume moi ce texte qui vient d'un audio en Français : {text}"}
                ],
                max_tokens=800
            )
            summary = response['choices'][0]['message']['content'].strip()
            return summary
        except Exception as e:
            logging.error(f"Error summarizing text: {e}")
            return ""

def generate_output_filename(base_name: str, suffix: str, extension: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{suffix}_{timestamp}.{extension}"

def is_supported_format(file_path: str) -> bool:
    supported_formats = ('.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm')
    return file_path.lower().endswith(supported_formats)

def convert_webm_to_wav(input_file: str, output_file: str):
    try:
        subprocess.run(['ffmpeg', '-y', '-i', input_file, output_file], check=True)  # '-y' flag forces overwrite
        logging.info(f"Converted {input_file} to {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        logging.error(f"Error converting {input_file} to WAV: {e}")
        return None

def process_audio(file_path: str, api_key: str):
    if not os.path.exists(file_path):
        logging.error("The specified file does not exist.")
        return None, None

    if not is_supported_format(file_path):
        logging.error("Unsupported file format.")
        return None, None

    # Convert .webm to .wav if necessary
    if file_path.lower().endswith('.webm'):
        wav_file_path = file_path.replace('.webm', '.wav')
        file_path = convert_webm_to_wav(file_path, wav_file_path)
        if not file_path:
            return None, None

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    audio_processor = AudioProcessor()

    logging.info("Transcription in progress...")
    text = audio_processor.transcribe_audio(file_path)
    logging.info("Transcription complete.")

    transcription_writer = FileWriter("text_transcription")
    transcription_filename = generate_output_filename(base_name, "transcription", "txt")
    transcription_writer.write_to_file(transcription_filename, text)

    logging.info("Summarization in progress...")
    summary = audio_processor.summarize_text(text, api_key)
    logging.info("Summarization complete.")

    summary_writer = FileWriter("text_summarize")
    summary_filename = generate_output_filename(base_name, "summary", "txt")
    summary_writer.write_to_file(summary_filename, summary)

    return text, summary

if __name__ == "__main__":
    # Example usage:
    file_path = "path_to_your_audio_file.webm"
    api_key = "your_openai_api_key"
    transcribed_text, summarized_text = process_audio(file_path, api_key)
    
    if transcribed_text and summarized_text:
        print("Transcription and summarization completed successfully.")
    else:
        print("There was an error in processing the audio.")
