import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
    const [file, setFile] = useState(null);
    const [chords, setChords] = useState([]);
    const [isLoading, setIsLoading] = useState(false); 

    const onFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const onFileUpload = () => {
        if (!file) {
            alert("Please select a file first.");
            return;
        }

        setIsLoading(true); 

        const formData = new FormData();
        formData.append("file", file);

        //axios.post('http://127.0.0.1:5000/upload', formData)
        axios.post('https://chordgetter-flaskbackend-5c25f170aab7.herokuapp.com/upload', formData)
            .then(response => {
                setChords(response.data.chords.slice(0, 10)); 
            })
            .catch(error => {
                console.error(error);
            })
            .finally(() => {
                setIsLoading(false); 
            });
    };

    return (
        <div className="flex flex-col items-center justify-start w-full max-w-md bg-gray-100 p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">Upload MP3 and Get Chords</h2>
            
            <div className="w-full">
                <label className="block">
                    <span className="sr-only">Choose File</span>
                    <input 
                        type="file" 
                        onChange={onFileChange} 
                        className="hidden"
                        id="file-upload"
                    />
                    <label 
                        htmlFor="file-upload"
                        className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded cursor-pointer transition duration-300 inline-block text-center"
                    >
                        Choose File
                    </label>
                </label>
                
                <button 
                    onClick={onFileUpload} 
                    className="w-full mt-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300"
                    disabled={isLoading} 
                >
                    {isLoading ? "Uploading..." : "Upload"}  
                </button>
            </div>
            
            <div className="mt-8 w-full">
                {isLoading && (
                    <div className="text-2xl font-bold text-gray-800 mb-6">Loading, please wait...</div> 
                )}
                {!isLoading && chords.length > 0 && (
                    <ul className="bg-white shadow-md rounded-lg p-4">
                        {chords.map((chord, index) => (
                            <li key={index} className="text-gray-700 py-2 border-b last:border-b-0">
                                {chord}
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
}

export default FileUpload;
