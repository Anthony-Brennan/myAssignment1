import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    linescores = []
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    with  open(sys.argv[2]) as tf:
        afinnfile = open(sys.argv[1])
        scores = {}  # initialize an empty dictionary
        for line in afinnfile:
            term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
            scores[term] = int(score)  # Convert the score to an integer.
        for line in tf:
            tj = json.loads(line)
            if "text" in tj:
                ts = tj.get('text')
                ta = ts.split()
                x = 0
                for word in ta:
                    x = x + scores.get(word,0)
                linescores.append(x)
                sys.stdout.write(str(x)+"\n")


if __name__ == '__main__':
    main()
