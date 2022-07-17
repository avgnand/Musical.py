# Musical.py
A small project that allows the user to find which musical keys contain a given note. Runs in the terminal.

`all_modes.json` contains a dictionary of all notes of the A Chromatic scale, mapped to arrays of scales in the six basic modes (i.e., *Ionian* through *Locrian*).

## Work in Progess
Currently, the program just asks the user to enter a note name to see which key signatures it is a member of.

## Basic Usage
Run the `main.py` file in a console to start searching for notes among all key signatures.

#### Example
```
PS C:\...\Musical_py> python .\main.py
Enter a note to find the keys in which it appears: a
['A', 'A#', 'C', 'D', 'F', 'G']
Start new search?[y/n] y
Enter a note to find the keys in which it appears: c
['A#', 'C', 'C#', 'D#', 'E', 'F', 'G', 'G#']
Start new search?[y/n] n
PS C:\...\Musical_py>
```
