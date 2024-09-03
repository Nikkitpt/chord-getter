import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
    const [file, setFile] = useState(null);
    const [chords, setChords] = useState([]);

    const onFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const onFileUpload = () => {
        const formData = new FormData();
        formData.append("file", file);

        axios.post('http://127.0.0.1:5000/upload', formData)
            .then(response => {
                setChords(response.data.chords);
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h2>Upload MP3 and Get Chords</h2>
            <input type="file" onChange={onFileChange} />
            <button onClick={onFileUpload}>Upload</button>
            <div>
                {chords.length > 0 && (
                    <ul>
                        {chords.map((chord, index) => (
                            <li key={index}>{chord}</li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
}

export default FileUpload;
