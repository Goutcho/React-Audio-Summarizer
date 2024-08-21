# Audio Processor Application

This project is a full-stack application that processes audio files for transcription and summarization. The backend is a Python-based API using Docker, while the frontend is a React application that allows users to record audio, submit it to the API, and view or download the results.

## Features

- **Audio Transcription**: The backend converts audio files to text using OpenAI's Whisper model.
- **Text Summarization**: Summarizes the transcribed text using GPT-4.
- **Text-to-Speech**: Converts the summarized text into an MP3 file.
- **Supports Various Audio Formats**: Handles `.mp3`, `.mp4`, `.mpeg`, `.mpga`, `.m4a`, `.wav`, `.webm`, and more.
- **Frontend Interface**: The React frontend allows users to record audio, submit it for processing, and view the results.

## Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download it from [here](https://www.docker.com/products/docker-desktop).
- **Node.js and npm**: Ensure Node.js and npm are installed on your system. You can download them from [here](https://nodejs.org/).

## Project Structure

- **Backend (Python API)**
  - `flask_app.py`: Main Flask application file.
  - `main.py`: Core logic for audio processing, transcription, and summarization.
  - `requirements.txt`: Python dependencies for the project.
  - `Dockerfile`: Docker configuration file for containerizing the application.

- **Frontend (React Application)**
  - `src/axiosInstance.js`: Configures the Axios instance to communicate with the backend API.
  - `src/AudioProcessorForm.js`: Main component that handles audio recording, submission, and displaying results.
  - `src/index.js`: Entry point for the React application.
  - `src/index.css`: Basic styling for the application.

## How to Set Up and Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Goutcho/React-Audio-Summarizer.git
cd React-Audio-Summarizer
```

### 2. Set Up the Backend

Navigate to the backend directory and build the Docker image:

```bash
cd audio-summary-api
docker build -t audio-processor-backend .
```

Run the Docker container, exposing it on port 8000:

```bash
docker run -d -p 8000:8000 audio-processor-backend
```

### 3. Set Up the Frontend

Navigate to the frontend directory and install dependencies:

```bash
cd ../audio-summary-api
npm install --legacy-peer-deps
```

Start the React application:

```bash
npm start
```

The React application will run on `http://localhost:3000` and interact with the API running on `http://localhost:8000`.

## How to Use the Application

1. **API Key**: Enter your OpenAI API key in the input field on the React frontend.
2. **Record Audio**: Use the frontend interface to start and stop recording audio.
3. **Submit**: Click "Process Audio" to submit the recorded audio to the backend API.
4. **View Results**: The transcribed and summarized text will be displayed on the frontend, with an option to download the summarized text as an MP3 file.

## API Endpoints

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

## Stopping the Application

To stop the running Docker container:

```bash
docker ps  # Find the container ID
docker stop <container_id>
```

To stop the React application, simply close the terminal or stop the running process with `Ctrl+C`.

## Notes

- This application is configured for development use. For production, consider using a production-grade WSGI server like `gunicorn` for the backend and optimizing the frontend build.
- Ensure your OpenAI API key is secure and not exposed in public repositories.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper)
- [OpenAI GPT-4](https://openai.com/)
- [Flask](https://flask.palletsprojects.com/)
- [React](https://reactjs.org/)
- [React Mic](https://github.com/hackingbeauty/react-mic)
- [Axios](https://axios-http.com/)
