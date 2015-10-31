class SimpleSentiments():
    def __init__(self):
        self.lexicon_lines = None
    
    def read_dictionary(self,filepath):
        with open(filepath, "rb") as f:
            lines = f.readlines()
        self.lexicon_lines = []
        for line in lines:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            self.lexicon_lines.append(parts)
            
    def crunch_scores(self):
        tempscores = {}
        self.scores = {}        
        for sentence in self.lexicon_lines:
            try:
                pos_score = sentence[2].strip()
                neg_score = sentence[3].strip()
                words = [x.split("#")[0] for x in sentence[4].strip().split(" ")]
                for word in words:
                    try:
                        tempscores[word].append(float(pos_score))
                        tempscores[word].append(-float(neg_score))
                    except:
                        tempscores[word]=[]
                        tempscores[word].append(float(pos_score))
                        tempscores[word].append(-float(neg_score))
            except:
                pass
                    
        for word in tempscores.keys():
            # print word, sum(scores[word])/len(scores[word])
            self.scores[word] = sum(tempscores[word])/len(tempscores[word])
            
    def get_sentiment(self, sentence):
        # 1. Convert to lowercase
        # 2. Stop words. Remove punctuation
        # 3. Split sentence
        # 4. For each word, get it's score and save in a list
        # 5. Get average of scores and return 
        pass

if __name__ == '__main__':
    print "Loading Lexicon"

    simple = SimpleSentiments()
    simple.read_dictionary("C:\\Users\\admin\\Desktop\\senti.txt")
    simple.crunch_scores()

    print "Done"
    simple.get_sentiment("This is so awesome")

#    print simple.scores["storm"]
