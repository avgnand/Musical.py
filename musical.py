from enum import Enum, unique

NATURALS = [i for i in "ABCDEFG"]
SHARPS = [i+"#" for i in NATURALS]
FLATS = [i+"b" for i in NATURALS]
NON_NOTES = ["B#", "E#", "Cb", "Fb"]

# Number of Semitones
WHOLE_STEP = 2
HALF_STEP = 1

# Removing "non-notes" from SHARPS and FLATS
for note in SHARPS:
    if note in NON_NOTES:
        SHARPS.remove(note)

for note in FLATS:
    if note in NON_NOTES:
        FLATS.remove(note)

# Constructing the A Chromatic Scale, off which other scales can be derived
A_CHROMATIC = []

for note in NATURALS:
    A_CHROMATIC.append(note)
    for n in SHARPS:
        if note in n:
            A_CHROMATIC.append(n)

# Constant for refering to length of the A Chromatic scale
CHROM_LEN = len(A_CHROMATIC)

@unique
class MusicMode(Enum):
    IONIAN = 0
    DORIAN = 1
    PHRYGIAN = 2
    LYDIAN = 3
    MIXOLYDIAN = 4
    AEOLIAN = 5
    LOCRIAN = 6
    # IONIAN = 7

def add_whole_step(idx) -> int:
    """
    Helper function for navigating A Chromatic by whole steps.
    This handles wrapping behavior when close to the end of A Chromatic.
    """
    if idx + WHOLE_STEP > CHROM_LEN:
        return 1
    elif idx + WHOLE_STEP == CHROM_LEN:
        return 0
    return idx + WHOLE_STEP

def add_half_step(idx) -> int:
    """
    Helper function for navigating A Chromatic by half steps.
    This handles wrapping behavior when close to the end of A Chromatic.
    """
    if idx + HALF_STEP > CHROM_LEN:
        return 0
    elif idx + HALF_STEP == CHROM_LEN:
        return -1
    return idx + HALF_STEP

def major_scale(note) -> list:
    """
    W-W-H-W-W-W-H.
    This function will return a major scale (list) based on given argument note.
    """
    scale = []
    start = A_CHROMATIC.index(note)
    this_idx = start

    scale.append(note)

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_half_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_half_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    return scale

def minor_scale(note) -> list:
    """
    W-H-W-W-H-W-W.
    This function will return a minor scale (list) based on given argument note.
    """
    scale = []
    start = A_CHROMATIC.index(note)
    this_idx = start

    scale.append(note)

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_half_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_half_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    this_idx = add_whole_step(this_idx)
    scale.append(A_CHROMATIC[this_idx])

    return scale

def make_modes(scale, pos) -> dict:
    """
    Takes a base scale and starting position, and constructs relevant mode.
    Returns dictionary of mode name and scale of notes as key, value, respectively.
    'pos' is the index in 'scale', so it will only accept values in range(7).
    e.g. : 'make_modes(M_scales["C"], 5)' is A Natural Minor.

    Legend (pos values -> returned modes):
    0 -> Ionian;
    1 -> Dorian;
    2 -> Phrygian;
    3 -> Lydian;
    4 -> Mixolydian;
    5 -> Aeolian;
    6 -> Locrian;
    (7 -> Ionian);
    """

    # For crashing if bad 'pos' passed to function:
    # if pos not in range(7):
    #     raise ValueError("Passed argument must be in range of 0 ~ 7.")

    # For silently converting passed argument to valid value:
    if pos > 7:
        pos %= 7

    label = MusicMode(pos).name
    mode = []
    k = pos
    for _ in range(len(scale)):
        mode.append(scale[k])
        k = (k + 1) % (len(scale) - 1)
    return {label: mode}

def construct_mode_space(note) -> dict:
    """
    Given a note (string), construct and aggregate all modes of the relevant key. 
    Requires M_scales to find given note's Major scale.
    Indices of returned "mode space" indicate 
    relative position above the tonic of the note's major scale.
    i.e. : 'mode_space[5]' indicates 6 semitones above tonic, or natural minor.
    Returns dict of modes labelled by name.
    """
    scale = M_scales[note]
    mode_space = {}
    for i in range(7):
        mode_space.update(make_modes(scale, i))
    return mode_space

def get_search_note():
    msg = "Enter a note to find the keys in which it appears: "
    search_note = input(msg)
    return search_note

def do_search(search_note):
    search_results = []
    for musKey in Mode_Master.keys():
        modes = Mode_Master.get(musKey)
        search_mode = modes["IONIAN"]
        if search_note in search_mode:
            search_results.append(musKey)
    return search_results

M_scales = {"tag": "major"}
for note in A_CHROMATIC:
    M_scales.update({f"{note}": major_scale(f"{note}")})

# m_scales = {"tag": "minor"}
# for note in A_CHROMATIC:
#     m_scales.update({f"{note}": minor_scale(f"{note}")})

# A master dictionary containing all notes in A Chromatic, and respective keys' mode-spaces
Mode_Master = {key: construct_mode_space(key) for key in A_CHROMATIC}

# Experiment: Search mode-spaces for all modes that contain a given note
# Insights: If one mode for a key contains a note, all the key's modes will also; 
#   So, searching one mode is sufficient to searching a given key for a note
# msg = "Enter a note to find the keys in which it appears: "
# search_note = input(msg)
# search_results = []

# # SEARCH v1 // Searches all modes of a key, but one is enough
# # All notes in A_CHROMATIC
# # for musKey in Mode_Master.keys():
# #     # Single mode space
# #     musModes = Mode_Master.get(musKey)
# #     # All modes for given mode space
# #     for mode in musModes.keys():
# #         # The notes for a mode
# #         musScale = musModes.get(mode)
# #         if search_note in musScale:
# #             search_results.append((musKey, mode))

# # SEARCH v2 // Searches first mode of a key only
# for musKey in Mode_Master.keys():
#     modes = Mode_Master.get(musKey)
#     search_mode = modes["IONIAN"]
#     if search_note in search_mode:
#         search_results.append(musKey)
# print(search_results)

def main():
    while True:
        note = get_search_note()
        results = do_search(note)
        print(results)
        cont = input("Start new search?[y/n] ")
        if cont != "y":
            break

if __name__ == '__main__':
    main()