import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
// import YoutubeLink from './components/YoutubeLink';

function App() {
    return (
        <div className="App">
            <h1>Chordify App</h1>
            <FileUpload />
            {/* <YoutubeLink /> */}
        </div>
    );
}

export default App;
