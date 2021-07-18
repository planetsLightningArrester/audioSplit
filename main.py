from pydub import AudioSegment
import sys
import os

if (len(sys.argv) < 2):
    print('[ERROR] Pass the file as argument')
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("[ERROR] Can't find the file '" + sys.argv[1] + "'")
    sys.exit()

print('Reading file "' + sys.argv[1] + '"...')
sound = AudioSegment.from_mp3(sys.argv[1])

print('OK')

total = len(sound) #ms
# total = 1*60*60*1000 + 22*60*1000 + 10*10000 #min
# total = total*60*1000 #ms

times = [
    (0)*60*1000,
    (1 + 37/60)*60*1000,
    (4 + 9/60)*60*1000,
    (6 + 0/60)*60*1000,
    (10 + 52/60)*60*1000,
    (13 + 25/60)*60*1000,
    (15 + 32/60)*60*1000,
    (17 + 10/60)*60*1000,
    (19 + 25/60)*60*1000,
    (23 + 42/60)*60*1000,
    (28 + 26/60)*60*1000,
    (30 + 57/60)*60*1000,
    (35 + 14/60)*60*1000,
    (39 + 24/60)*60*1000,
    (44 + 16/60)*60*1000,
    (47 + 41/60)*60*1000,
    (50 + 23/60)*60*1000,
    (52 + 40/60)*60*1000,
    (58 + 4/60)*60*1000,
    total
]

print(times)

tracks = []
for i in range(len(times) - 1):
    tracks.append(sound[times[i]:times[i+1]])
    print("Track" + str(i+1) + ': ' + str(times[i]/(60*1000)) + 'min - ' + str(times[i + 1]/(60*1000)) + 'min')
    print(times[i])
    print(times[i-2])

for i in range(len(tracks)):
    print('Generating file ./v4/v4t' + str(i+1))
    tracks[i].export("./v4/v4t" + str(i+1) + '.mp3', format='mp3')

print('Done!')

