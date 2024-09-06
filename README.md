# Chord Getter

Chord Getter is a web-based application that allows users to extract chords from audio files. The app provides musicians and music enthusiasts with an easy way to visualize and access the chords for their favorite songs.

## Features

- **Upload MP3 Files**: Users can upload an audio file in MP3 format, and the app will extract the chords in real time.

## Technologies Used

- **Frontend**: React, Tailwind
- **Backend**: Flask, Python, Heroku
- **Deployment**: Heroku
- **Audio Processing**: Web Audio API, librosa (for future enhancements in chord extraction)

## Upcoming Features

In future updates, the following features will be implemented to enhance the functionality and user experience:

- **Chord Playback**: An audio playback feature to play the detected chords in sync with the uploaded file
- **Basic guitar tab feature**

## Installation

To run this project locally, follow these steps:

### Prerequisites

- [Node.js](https://nodejs.org/) (for frontend)
- [Python 3.8+](https://www.python.org/) (for backend)
- [Flask](https://flask.palletsprojects.com/) (backend framework)
- [React](https://reactjs.org/) (frontend framework)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Nikkitpt/chord-getter.git
    cd chord-getter
    ```

2. Install dependencies for both frontend and backend:

    - **Backend (Flask)**:

      ```bash
      cd backend
      pip install -r requirements.txt
      ```

    - **Frontend (React)**:

      ```bash
      cd frontend
      npm install
      ```

3. Start the development servers:

    - **Backend**:

      ```bash
      cd backend
      flask run
      ```

    - **Frontend**:

      ```bash
      cd frontend
      npm start
      ```

4. Access the app locally at `http://localhost:3000` for the frontend, and the backend API will be served at `http://localhost:5000`.

