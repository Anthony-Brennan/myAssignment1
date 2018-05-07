import sys
import json






def lines(fp):
    print str(len(fp.readlines()))


def main():
    afinnfile = open("AFINN-111.txt")
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    sent_file = open("output.json")
    tweet_file = open("AFIN-111.txt")

    lines(sent_file)
    lines(tweet_file)


if __name__ == '__main__':
    main()
