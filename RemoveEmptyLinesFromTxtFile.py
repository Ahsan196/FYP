with open('Desktop/New Text Document (12).txt') as infile, open('Downloads/newsId.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)
