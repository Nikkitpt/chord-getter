from flask import Blueprint, request, jsonify, make_response
import os
import librosa
import numpy as np
from .utils import extract_chords, allowed_file
from flask_cors import CORS, cross_origin
import tempfile

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return "API is up and running"

@main.route('/upload', methods=['POST','OPTIONS'])
def upload_file():
    print("The Request \n", request.files)

    file = request.files.get('file')

    if file is None or file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            file.save(temp_file.name)
            temp_file_path = temp_file.name
        
        try:
            # Process the file
            chords = extract_chords(temp_file_path)
            # return jsonify({'chords': chords}), 200
            response = make_response(jsonify({"message": "Upload route working"}))
            response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
            return response
        finally:
            # Clean up the temp file after processing
            os.remove(temp_file_path)

    return jsonify({'error': 'Invalid file type'}), 400
