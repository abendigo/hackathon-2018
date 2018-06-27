import uuid
import base64
import os
import sys
from flask import Flask
from flask import request
from flask_cors import CORS
from midiutil import MIDIFile
from midi2audio import FluidSynth

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Moody is cool!"

@app.route("/img2mus", methods = ['POST'])
def parse_request():
    request.get_data()
    image_data = request.data
    
    # temp code
    freq = 60
    track = 0
    channel = 0
    time = 0
    duration = 1
    tempo = 60
    volume = 100

    my_midi = MIDIFile(1)
    my_midi.addTempo(track, time, tempo)
    my_midi.addNote(track, channel, freq, time, duration, volume)
    my_midi.addNote(track, channel, freq + 2, time + 1, duration, volume)

    with open("test.mid", "wb") as output_file:
        my_midi.writeFile(output_file)


    fs = FluidSynth()
    os.chdir('/home/matt.lewis/hackathon/hackathon-2018/backend/server/')
    fs.midi_to_audio('test.mid', 'test.wav')

    with open("test.wav", "r") as input_file:
        encoded_midi = base64.b64encode(input_file.read())

    img_id = uuid.uuid4().hex
    file_name = img_id + '.png'

    image_data_url, image_data_encode = image_data.split(',')
    fh = open(file_name, "wb")
    fh.write(image_data_encode.decode('base64'))
    fh.close()

    return "Okay"
