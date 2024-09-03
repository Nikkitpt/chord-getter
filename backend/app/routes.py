from flask import Blueprint, request, jsonify, make_response
import os
import librosa
import numpy as np
from .utils import extract_chords, allowed_file
from flask_cors import CORS, cross_origin

main = Blueprint('main', __name__)


@main.route('/upload', methods=['POST','OPTIONS'])
def upload_file():
    print("The Request \n", request.files)
    # if 'file' not in request.files:
    #     return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = file.filename
   

        # file_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
        file_path = './uploads/audio.mp3'
        # file.save(file_path)

        chords = extract_chords(file_path)
        return jsonify({'chords': chords}), 200

    return jsonify({'error': 'Invalid file type'}), 400
