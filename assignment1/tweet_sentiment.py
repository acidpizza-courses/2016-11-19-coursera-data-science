import sys
import json

scores_ = {} # initialize an empty dictionary

def LoadDictionary():
    afinnfile = open("AFINN-111.txt")
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores_[term] = int(score)  # Convert the score to an integer.

def ParseTweet():
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        score = 0
        tweet = json.loads(line)
        if "text" in tweet:
            tweet_line = tweet["text"]
            tweet_words = tweet_line.split()
            for word in tweet_words:
                if word in scores_:
                    score += scores_[word]
        print score

def main():
    LoadDictionary()
    ParseTweet()
#    print scores_.items() # Print every (term, score) pair in the dictionary

if __name__ == '__main__':
    main()
