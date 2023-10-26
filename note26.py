from midiutil import MIDIFile

base_note = 35
soup = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",\
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",\
    ".", ",",\
    "=", "+", "-", "*", "/",\
    "(", ")"]

midi_notes = []
i = base_note
while i <= (len(soup) + base_note):
    midi_notes.append(i)
    i += 1

# Checking if each character of the string is in the list of allowed characters
string = input("Texte à convertir / Text to convert: ")
if not string:
    print("Vous devez entrer quelque chose / You must enter something")
    exit(1)

# Converting notes to MIDI characters
masterwork = []
for element in string:
    if element not in soup:
        print("Caractère invalide / Invalid character: " + element)
        print("Liste des caractères acceptés / Accepted characters list:")
        print(soup)
        exit(1)
    for index, character in enumerate(soup, start = 0):
        if character == element:
            masterwork.append(midi_notes[index])
print(masterwork)

# Credit goes to https://stackoverflow.com/a/11060178 for the MIDI library code
mf = MIDIFile(1)
track = 0
time = 0
mf.addTrackName(track, time, "note26")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

time = 0

for note in masterwork:
    pitch = note         # MIDI code
    duration = 1         # 1 beat long
    mf.addNote(track, channel, pitch, time, duration, volume)
    time += 1

# Write MIDI file
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
    outf.close()
