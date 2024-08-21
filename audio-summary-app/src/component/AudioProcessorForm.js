import React, { useState } from 'react';
import { ReactMic } from 'react-mic';
import axiosInstance from '../api/axiosInstance';
import './AudioProcessorForm.css';

const AudioProcessorForm = () => {
    const [record, setRecord] = useState(false);
    const [apiKey, setApiKey] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState('');
    const [blob, setBlob] = useState(null);

    const startRecording = () => {
        setRecord(true);
        console.log("Recording started.");
    };

    const stopRecording = () => {
        setRecord(false);
        console.log("Recording stopped.");
    };

    const onData = (recordedBlob) => {
        console.log('Real-time data:', recordedBlob);
    };

    const onStop = (recordedBlob) => {
        console.log('Recorded Blob:', recordedBlob);
        setBlob(recordedBlob.blob);
        console.log('Blob ready for submission:', recordedBlob.blob);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        if (!blob) {
            setError('Please record an audio file first.');
            console.error('No audio file recorded.');
            return;
        }

        const audioFile = new File([blob], 'audio.webm', { type: blob.type });
        const formData = new FormData();
        formData.append('api_key', apiKey);
        formData.append('audio', audioFile);
    
        try {
            const response = await axiosInstance.post('/process-audio', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
    
            console.log('Response from API:', response.data);
            setResult(response.data);
            setError('');
        } catch (err) {
            console.error('Error processing audio:', err);
            setError('Error processing audio.');
            setResult(null);
        }
    };

    return (
        <div className="container">
            <h1>Audio Processor Summary</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>OpenAI API Key:</label>
                    <input
                        type="text"
                        value={apiKey}
                        onChange={(e) => setApiKey(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <button type="button" onClick={startRecording} disabled={record}>Start Recording</button>
                    <button type="button" onClick={stopRecording} disabled={!record}>Stop Recording</button>
                </div>
                <ReactMic
                    record={record}
                    className="sound-wave"
                    onStop={onStop}
                    onData={onData}
                    strokeColor="#fff"
                    backgroundColor="#a86161"
                />
                <button type="submit">Process Audio</button>
            </form>
            {result && (
                <div className="result">
                    <h2>Result</h2>
                    <p><strong>Transcribed Text:</strong> {result.transcribed_text}</p>
                    <a href={result.transcription_link} download="transcription.txt">Download Transcription as TXT</a>
                    <p><strong>Summarized Text:</strong> {result.summarized_text}</p>
                    <a href={result.summary_link} download="summary.txt">Download Summary as TXT</a>
                </div>
            )}
            {error && <p className="error">{error}</p>}
        </div>
    );
};

export default AudioProcessorForm;
