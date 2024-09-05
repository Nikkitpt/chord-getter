import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
// import YoutubeLink from './components/YoutubeLink';

function App() {
    return (
        <div className="flex flex-col items-center justify-center h-screen bg-gray-200">
            <h1 className="text-4xl font-bold text-blue-500 mb-5">Chord Getter</h1>
            <FileUpload />
            {/* <YoutubeLink /> */}
        </div>
    );
}

export default App;
