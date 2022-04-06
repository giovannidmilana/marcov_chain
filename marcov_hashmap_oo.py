import nltk



class Chain:
    def __init__(self):
        self.corpus = self.load_file('nirvana.txt')
        print('1')
        self.words = self.clean_corpus()
        print('2')
        self.num_words = len(self.words)
        print(self.num_words)
        print('3')
        self.hashMap = self.make_hash_map()
        print('4')
        
    def load_file(self, fl_name):
        with open(fl_name) as f:
            lines = f.read()
        return lines
        
    def clean_corpus(self):
        
        
        corpus = self.corpus.lower()
        corpus = corpus.encode('ascii', 'ignore').decode()
        corpus = corpus.replace("\n", "*")
        corpus = corpus.replace("\t", "*")
        corpus = corpus.replace("?", "*")
        corpus = corpus.replace(".", "*")
        '''
        corpus = corpus.replace("the", "*")
        corpus = corpus.replace("day", "*")
        corpus = corpus.replace("play", "*")
        corpus = corpus.replace("two", "*")
        corpus = corpus.replace("one", "*")
        corpus = corpus.replace("by", "*")
        '''
        corpus = corpus.replace("!", "*")
        corpus = corpus.replace(" ", "*")
        corpus = corpus.split('*')
        return corpus
        
    def make_hash_map(self):
        dict1 = dict()
        dict2 = dict()
        for j in range(self.num_words):
            dict2[self.words[j]] = dict1
            dict1 = dict()
            for i in range(self.num_words):
                dict1[self.words[i]] = 0.0
               
        for i in range(self.num_words-1):
            dict2[self.words[i]][self.words[i+1]] = dict2[self.words[i]][self.words[i+1]] + 1
            
        for i in range(self.num_words-1):
            dict2[self.words[i]][self.words[i+1]] = dict2[self.words[i]][self.words[i+1]] / self.num_words *100
        
        return dict2
        
    def next_word(self, word, i):
        d = self.hashMap[word]
        bestk = ''
        bestv = -.00001
        for k, v in d.items():
           #print(k)
           if v > bestv:
               d[k] = v  - (1 / self.num_words * 100) 
               bestv = v
               bestk = k
        if i > 100:
            return  None
        print(bestk)
        return self.next_word(bestk, i+1)
               
               
        
test = Chain()
#print(test.hashMap[''])
print(test.next_word('oh', 0))
