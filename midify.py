from midiutil.MidiFileGenerator import MidiFileGenerator, MidiTrack
from midiutil.Scales import *
from math import ceil
from random import sample
import json
from defaults import note_lookup, root_lookup

def note_to_midi(n):
  if isinstance(n, basestring):
    return note_lookup[n]
  elif isinstance(n, int):
    return n

def root_to_midi(n):
  if isinstance(n, basestring):
    return root_lookup[n]
  elif isinstance(n, int):
    return n

def bpm_time(bpm=120, count=0.25):
  onebar = float((60.0/float(bpm))*4.0)
  return onebar*float(count)

def scale_vec(vec, low, high):
  
  # extract min and max info
  min_vec = min(vec)
  max_vec = max(vec)

  # scale
  return [(int(ceil(v - min_vec)) * (high-low) / (max_vec - min_vec)) for v in vec]

def midify(
    vec, 
    out_file,
    key = "C",
    scale=MAJOR, 
    bpm=120, 
    count=0.25, 
    channel=1, 
    min_note="C-1", 
    max_note="G9"
  ):

  # transform keys and min/max notes
  key = root_to_midi(key)
  min_note = note_to_midi(min_note)
  max_note = note_to_midi(max_note)

  # select notes
  notes = build_scale(key, scale, min_note, max_note)

  # scale notes
  note_indexes = scale_vec(vec, low=0, high=(len(notes)-1))

  # determinte note length
  beat = bpm_time(bpm, count)

  # generate midi file
  m = MidiFileGenerator()
  track = MidiTrack(channel=channel, tempo=bpm)

  t = 0
  for i in note_indexes:
    n = notes[i]
    track.add_note(time=t, duration=beat, note=n, velocity=100)
    t += beat

  m.tracks.append(track)
  m.writeToFile(out_file)

if __name__ == '__main__':
  vec = sample(range(1,10000), 32)
  midify(vec, bpm=130, count= 0.125, out_file="random.mid", scale=CHROMATIC, min_note="C2", max_note="D#3")
  vec = sample(range(1,10000), 32)
  midify(vec, bpm=130, count= 0.125, out_file="bass.mid", key = "E", scale=MAJOR, min_note="E2", max_note="G#4")
  vec = sample(range(1,10000), 32)
  midify(vec, bpm=130, count= 0.125, out_file="arp.mid", key = "E", scale=MAJOR, min_note="B5", max_note="G#7")