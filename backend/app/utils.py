import librosa
import numpy as np
from collections import Counter

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3'}

def filter_unique_chords(chord_sequence):
    unique_chords = []
    last_chord = None
    
    for chord in chord_sequence:
        if chord != "N/A" and chord != last_chord:
            unique_chords.append(chord)
            last_chord = chord
    
    return unique_chords

def extract_chords(file_path):
    y, sr = librosa.load(file_path)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chord_sequence = []

    # Mapping from chroma index to note name
    pitch_to_note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Define basic chord templates
    chord_templates = {
        'major': np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]),
        'minor': np.array([1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]),
        'diminished': np.array([1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]),
        'augmented': np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]),
        'suspended2': np.array([1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]),
        'suspended4': np.array([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0])
    }

    def identify_chord(chroma_vector):
        # Threshold the chroma vector to consider only strong notes
        chroma_vector = (chroma_vector > 0.5).astype(int)
        
        possible_chords = []

        for root_note in range(12):
            for chord_quality, template in chord_templates.items():
                rotated_template = np.roll(template, root_note)
                if np.array_equal(chroma_vector, rotated_template):
                    possible_chords.append(f"{pitch_to_note[root_note]} {chord_quality}")
        
        if possible_chords:
            # Return the most common chord (if there's ambiguity)
            return Counter(possible_chords).most_common(1)[0][0]
        else:
            return "N/A"

    for i in range(chroma.shape[1]):
        chord = identify_chord(chroma[:, i])
        chord_sequence.append(chord)
    
    chord_sequence = filter_unique_chords(chord_sequence)

    return chord_sequence

