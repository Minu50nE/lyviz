#ah yolo, jumping in naked into code.

text    = open("ingest.txt").read().splitlines() #read from file into list of lines.
print(text)
txet    = [] #text.reverse() #< this shit reverses lists that can be handy AF.

#this part breaks up every line into seperate characters
for line in text:
    l = list(line)
    txet.append(l)

"""and now for the fun part.
Basically, I want to visualize lyrics in some other way than text. 

Some balancing system, or pathfinding rendering for fun."""
#def want to output into a vector line format as you know, finite scaling and stuff :>
