# React Frontend for Audio Processor API

This project is a React-based frontend application designed to interact with a Python-based audio processing API. The application allows users to record audio, submit it for transcription and summarization, and download the results.

## Features

- **Audio Recording**: Record audio directly from the browser using the React Mic component.
- **API Integration**: Submit recorded audio files to a backend API for transcription and summarization.
- **Result Display**: Display the transcribed and summarized text returned from the API.
- **Download Option**: Download the summarized text as an MP3 file.

## Prerequisites

- **Node.js and npm**: Ensure Node.js and npm are installed on your system. You can download them from [here](https://nodejs.org/).

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Goutcho/React-Audio-Summarizer.git
cd React-Audio-Summarizer
cd audio-summary-app
```

### 2. Install Dependencies

Install the necessary dependencies using npm:

```bash
npm install
```

### 3. Run the Application

Start the React application with the following command:

```bash
npm start
```

The application will be running on `http://localhost:3000`.

## Project Structure

- `src/axiosInstance.js`: Configures the Axios instance to communicate with the backend API.
- `src/AudioProcessorForm.js`: Main component that handles audio recording, submission, and displaying results.
- `src/index.js`: Entry point for the React application.
- `src/index.css`: Basic styling for the application.

## How to Use the Application

1. **API Key**: Enter your OpenAI API key in the input field.
2. **Record Audio**: Click on "Start Recording" to begin recording audio. Once done, click "Stop Recording".
3. **Submit**: Click "Process Audio" to submit the recorded audio to the API.
4. **View Results**: Once processed, the transcribed text and summarized text will be displayed. You can also download the summary as an MP3 file.

## Configuration

- **Backend API**: The application is configured to interact with a backend API running on `http://localhost:8000`. You can modify the `baseURL` in `src/axiosInstance.js` if your backend API is hosted elsewhere.

## Notes

- The application uses the React Mic component for recording audio, which supports real-time audio visualizations.
- The backend API needs to be running for the frontend to function properly. Make sure to start the backend API server before using this application.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [React Mic](https://github.com/hackingbeauty/react-mic)
- [Axios](https://axios-http.com/)
- [React](https://reactjs.org/)