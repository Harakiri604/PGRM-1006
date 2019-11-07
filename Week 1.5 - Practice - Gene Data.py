#Open the file
file = open("sequence.fasta", 'r')

#Base type counts
g = 0
a = 0
t = 0
c = 0

#Skip the header
file.readline()

#Loop through this file (first "for" gives us each string, i.e. each line in the file, next "for" gives us the character)
for line in file:
    for char in line:
        char = char.lower()
        if char == 'g': g+=1
        elif char == 'a': a+=1
        elif char == 't': t+=1
        elif char == 'c': c+=1

#Do some calcs
total = (g+a+t+c)/100

#Output in specific format
print("g: %d, a: %d, t: %d, c: %d" % (g, a, t, c))
print("%%g: %.0f, %%a: %.0f, %%t: %.0f, %%c: %.0f" % (g/total, a/total, t/total, c/total))
