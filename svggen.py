#textloader
lines = open("ingest.txt").read().splitlines()

class songline:
    def __init__(self, no, words):
        self.no = no
        self.words = words

lineobs = []

linecounter = 0
for line in lines:
    currentLine = lines[linecounter]
    currentLine = currentLine.split()
    lineobs.append(songline(linecounter, currentLine))
    linecounter = linecounter + 1

letterfreq = list("eothasinrdluymwfgcbpkvjqxzEOTHASINRDLUYMWFGCBPKVJQXZ")

def wordweight(word):
    weight = 0
    for letter in word:
        weight = weight + (letterfreq.index(letter)+1)
    return weight

def lineweight(line):
    weight = 0
    for word in songline:
        weight = weight + (wordweight(word))
    return weight 

print(lineweight(0))

for obj in lineobs:
    print(obj.words)

f=open("img.svg","w+")
#initialize the svg file with header;
f.write("""<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 19.2.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.0" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 666 666" enable-background="new 0 0 666 666" xml:space="preserve">
     """)


f.write("""<rect x="312.308" y="287.092" fill="none" stroke="#000000" stroke-miterlimit="10" width="66.6" height="66.6"/>
""")

f.write("""</svg>
""")
f.close()
print("file written successfully")


