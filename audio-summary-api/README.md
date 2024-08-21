# Audio Processor with Transcription and Summarization

This project is a Python-based audio processing application that uses Whisper for transcription and OpenAI's GPT-4 for summarization. The application supports audio input, transcribes it to text, summarizes the transcribed text, and optionally converts the summary to speech.

## Features

- **Audio Transcription**: Converts audio files to text using OpenAI's Whisper model.
- **Text Summarization**: Summarizes the transcribed text using GPT-4.
- **Text-to-Speech**: Converts the summarized text into an MP3 file.
- **Supports Various Audio Formats**: Handles `.mp3`, `.mp4`, `.mpeg`, `.mpga`, `.m4a`, `.wav`, `.webm`, and more.

## Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download it from [here](https://www.docker.com/products/docker-desktop).

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Goutcho/React-Audio-Summarizer.git
cd React-Audio-Summarizer
cd audio-summary-api
```

### 2. Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t audio-processor .
```

### 3. Run the Docker Container

Run the Docker container, exposing it on port 8000:

```bash
docker run -d -p 8000:8000 audio-processor
```

### 4. Access the Application

The application will be running on `http://localhost:8000`. You can interact with the API or use the provided React frontend.

### 5. API Endpoints

- **POST `/process-audio`**: Upload an audio file for transcription and summarization.
  - **Parameters**:
    - `api_key`: Your OpenAI API key.
    - `audio`: The audio file to be processed.
  - **Response**:
    - `transcribed_text`: The transcribed text from the audio.
    - `summarized_text`: The summarized text.
    - `download_link`: Link to download the summarized text as an MP3 file.
    - `transcription_file`: Link to download the transcribed text as a `.txt` file.
    - `summary_file`: Link to download the summarized text as a `.txt` file.

### 6. Example Usage

You can test the application using a tool like `curl`:

```bash
curl -F "api_key=your_openai_api_key" -F "audio=@/path/to/your/audiofile.webm" http://localhost:8000/process-audio
```

### 7. Stop the Container

To stop the running Docker container:

```bash
docker ps  # Find the container ID
docker stop <container_id>
```

## Project Structure

- `flask_app.py`: Main Flask application file.
- `main.py`: Core logic for audio processing, transcription, and summarization.
- `requirements.txt`: Python dependencies for the project.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `README.md`: This readme file.

## Notes

- This application is configured for development use. For production, it is recommended to use a production-grade WSGI server like `gunicorn` and configure proper security measures.
- Ensure your OpenAI API key is secure and not exposed in public repositories.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper)
- [OpenAI GPT-4](https://openai.com/)
- [Flask](https://flask.palletsprojects.com/)
