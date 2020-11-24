import glob
import os

print("Mario Kart Tour SoundExtractor v1.0 by inkuringu-ika")

print("Extracting...")

for file_path in glob.glob("./input_nabe/b/*"):
    file = open(file_path,"br")
    file_byte = file.read()
    offset = 0
    while True:
        match_index = file_byte.find(b"RIFF",offset)
        if(not match_index == -1):
            start_byte = match_index
            end_byte = int.from_bytes(file_byte[match_index + 4:match_index + 8],"little") + match_index + 8
            out = file_byte[start_byte:end_byte]
            with open("./output_nabe/" + os.path.basename(file_path) + "_" + str(match_index) + '.wem', 'bw') as f:
                f.write(out)
            offset = end_byte
        else:
            break

print("Extracted!")
