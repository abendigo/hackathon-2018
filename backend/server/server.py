import uuid
import base64
import os
import sys
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from midiutil import MIDIFile
from midi2audio import FluidSynth

app = Flask(__name__)
CORS(app)

note_to_midi = {
    "D4": 62,
    "E4": 64,
    "F4": 65,
    "G4": 67,
    "A4": 69,
    "B4": 71,
    "C5": 72,
    "D5": 74,
    "E5": 76,
    "F5": 77,
    "G5": 79,
}

type_to_duration = {
    "Q": 1,
    "H": 2,
    "W": 4,
}

sample_list = [["F5", "Q"], ["G5", "H"], ["F5", "W"]]

@app.route("/")
def hello():
    return "Moody is cool!"

@app.route("/img2mus", methods = ['POST'])
def parse_request():
    #request.get_data()
    #image_data = request.data
    #image_data = request.json
    image_data_encode = request.json.get('image')
    
    # constants
    track = 0
    channel = 0
    time = 0
    tempo = request.json.get('tempo')
    volume = request.json.get('volume')

    my_midi = MIDIFile(1)
    my_midi.addTempo(track, time, tempo)
    prev_duration = 0
    for counter, my_tuple in enumerate(sample_list):
        note = my_tuple[0]
        note_type = my_tuple[1]
        midi_note = note_to_midi[note]
        duration = type_to_duration[note_type]
        my_midi.addNote(track, channel, midi_note, time, duration, volume)
        time += duration

    with open("test.mid", "wb") as output_file:
        my_midi.writeFile(output_file)

    fs = FluidSynth()
    fs.midi_to_audio('test.mid', 'test.wav')

    with open("test.wav", "r") as input_file:
        encoded_midi = base64.b64encode(input_file.read())

    img_id = uuid.uuid4().hex
    file_name = img_id + '.png'

    image_data_url, image_encode = image_data_encode.split(',')
    fh = open(file_name, "wb")
    fh.write(image_encode.decode('base64'))
    fh.close()

    return jsonify({'audio': { 'content': encoded_midi }})
