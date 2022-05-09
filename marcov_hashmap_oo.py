import nltk






class Chain:
    def __init__(self, corpus):
        self.corpus = corpus
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
    #clean corpus eliminate non alpha and numeric characters    
    def clean_corpus(self):
        corpus = self.corpus.lower()
        corpus = corpus.encode('ascii', 'ignore').decode()
        letters = ['1','2','3','4','5','6','7','8','9',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0']
        for i in corpus:
            if i not in letters:
                corpus = corpus.replace(i, '*')
        corpus = corpus.replace('*', '')
        corpus = corpus.replace('oc', '')
        corpus = corpus.replace('  ', ' ')
        corpus = corpus.split(' ')
        #print(corpus[0:100])
        return corpus
    
    #create hash map of word co-occurrence probability
    def make_hash_map(self):
        dict1 = dict()
        for i in range(self.num_words-1):
            #create new dict if word hasnt been seen yet
            if self.words[i] not in dict1:    
                dict1[self.words[i]] = {self.words[i+1]:1}
            #create new nested dict if the two word accurance is new
            elif self.words[i+1] not in dict1[self.words[i]]:
                dict1[self.words[i]][self.words[i+1]] = 1
            # add one to old key value pair if it already exists
            else:
                dict1[self.words[i]][self.words[i+1]] = dict1[self.words[i]][self.words[i+1]] + 1
                #capped co-occurrence at 1250 1/8th the size of the samples used
                if dict1[self.words[i]][self.words[i+1]] > 1250:
                    dict1[self.words[i]][self.words[i+1]] = 1250
                #dict1[self.words[i]][self.words[i+1]] = dict1[self.words[i]][self.words[i+1]] + 1
                
            
        return dict1
        
    #next word prediction which lowers the probabiity of word co-occurrence upon occurrence
    def next_word(self, word, i, string):
        d = self.hashMap[word]
        bestk = ''
        bestv = -1
        for k, v in d.items():
           #print(k)
           if v > bestv:
               d[k] = v  - 1
               bestv = v
               bestk = k
        if i > 1000:
            return  string
        string = string + ' ' + bestk
        return self.next_word(bestk, i+1, string)



'''
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
        
        corpus = corpus.replace("the", "*")
        corpus = corpus.replace("day", "*")
        corpus = corpus.replace("play", "*")
        corpus = corpus.replace("two", "*")
        corpus = corpus.replace("one", "*")
        corpus = corpus.replace("by", "*")
        
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
'''
               
        
test = Chain()
#print(test.hashMap[''])
print(test.next_word('oh', 0))
