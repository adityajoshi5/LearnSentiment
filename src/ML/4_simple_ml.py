'''
Created on Nov 1, 2015

@author: Aditya
'''

class MLSentiment():


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def train(self, trainfile):
        # Load File into list
        # Get tokens for each sentence
        # Use DictVectorizer to create Training Data. Dict Vectorizer must be property of the class
        # Use SKLEARN's SVM to train
        pass
    
    
    def test(self, testfile):
        pass
    
    
if __name__ == '__main__':
    scores = MLSentiment()
    scores.train_corpus("../Extras/lokesh_train_1.txt")
    print scores.evaluate("../Extras/lokesh_test_1.txt")
#    scores.prediction("it's a very lovely morning today.")   