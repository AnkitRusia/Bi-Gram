#para = """My name is Ankit Rusia. He is Great."""
para = 'My name is Ankit Rusia. He is great. India is Amazing. Science is great with every aspect'
#para = open('paragraph.txt', 'r').read()




from nltk.tokenize import WordPunctTokenizer as WPT
from nltk.tokenize import sent_tokenize
from tqdm import tqdm


class Table():
        def __init__(self, word, p):
                self.word = word
                self.p = p
        def give(self):
                return [self.word, self.p]

class Suggestion():
        def __init__(self, para = para):
                self.para = para
                self.word_tokenize = WPT()
                self.words = self.word_tokenize.tokenize(self.para)
                self.sents = sent_tokenize(self.para)
                self.word_pred = {}
                self.iter_sent_RFS()
                self.memorize()

                
        def remove_fullStop(self, text):
                if '.' in text :
                        text = text[:-1]
                return text

        def iter_sent_RFS(self):
                for i in range(len(self.sents)):
                        self.sents[i] = self.remove_fullStop(self.sents[i])
                

        def memorize(self):
                words_set = []
                
                for i in self.words :
                        if i not in words_set :
                                words_set.append(i)
                self.words = words_set

                
                for i in tqdm(range(len(self.words))) :
                        each_word = self.words[i]
                        uw = each_word
                        gs = []
                        
                        for es in self.sents :
                                if uw in es.split(' ') :
                                        gs.append(es)

                        tb = []
                        for es in gs :
                                cp, already_calculated = 0, False
                                cur_line_words = es.split(' ')
                                cur_line_words.append('&.&')
                                idx = cur_line_words.index(uw)
                                next_word_in_cur_line = cur_line_words[idx + 1]
                                for t in tb:
                                        if next_word_in_cur_line == t.give()[0]:
                                                already_calculated = True
                                                break
                                if not  already_calculated :
                                        for el in gs :
                                                el = el.split(' ')
                                                el.append("&.&")
                                                nidx = el.index(uw)
                                                nw_inner = el[nidx+1]
                                                if nw_inner == next_word_in_cur_line :
                                                        cp += 1
                                        cp = cp / len(gs)
                                        tb.append(Table(next_word_in_cur_line, cp))
                                self.word_pred[each_word] = tb
                                                                                        
        def show(self,para = False, Dictionary = False, words_set = False):
                if para == 'True':
                        print(self.para)
                if Dictionary == 'True':
                        for key, value in self.word_pred.items():
                                print('\033[1;33;40m--------------  %s  ------------'%key)
                                for t in value :
                                        print(t.give())
                                print('_________________________________\033[1;37;40m\n')
                if words_set == 'True':
                        print('Ye hp raha hai kya')
                        print(self.words)

        def predict(self, spell):
                if spell in self.word_pred.keys() :
                        predictions = self.word_pred[spell]
                        for p in predictions :
                                word, probab = p.give()
                                print("Next Word : \033[0;30;47m",word,"\033[1;37;40m  probability = \033[0;30;47m %f\033[1;37;40m"%probab)
                                
                
                
                

o = Suggestion()
print("\033[1;32;40mDONE :)  \033[1;37;40m\n")



to_print = """
1. show Paragraph Dictionar Word_Set
2. predict word
3. exit
"""
print(to_print)



ip = input()
while ip != 'exit' :
        ip = ip.split(' ')
        if ip[0] == 'show' :
                o.show(ip[1], ip[2], ip[3])
        elif ip[0] == 'predict' :
                o.predict(ip[1])
        ip = input()
        print('\n\n')

##word_pred = {}
##para = 'My name is Ankit Rusia. He is great. India is Amazing. Science is great with every aspect'
##s = ['My name is Ankit Rusia', 'He is great', 'India is Amazing', 'Science is great with every aspect']
##word_tokenize = WPT()
##words = word_tokenize.tokenize(para)

##words_set = []
##for i in words :
##        if i not in words_set :
##                words_set.append(i)


##print(words_set)



##for i in words_set :
##        uw = i
##        gs = []
##        for es in s :
##                if uw in es :
##                        gs.append(es)
##        
##                        
##        tb = []
##        for es in gs :
##                cp, already_calculated = 0, False
##                cur_line_words = es.split(' ')
##                cur_line_words.append('&^&')
##                idx = cur_line_words.index(uw)
##                next_word_in_cur_line = cur_line_words[idx + 1]
##                for t in tb:
##                        if next_word_in_cur_line == t.give()[0]:
##                                already_calculated = True
##                                break
##                if not  already_calculated :
##                        for el in gs :
##                                el = el.split(' ')
##                                el.append("&^&")
##                                nidx = el.index(uw)
##                                nw_inner = el[nidx+1]
##                                if nw_inner == next_word_in_cur_line :
##                                        cp += 1
##                        cp = cp / len(gs)
##                        tb.append(Table(next_word_in_cur_line, cp))
##        word_pred[i] = tb
                

####for key, values in word_pred.items() :
####        print("-------------  %s  ------------"%key)
####        for t in values :
####                print(t.give())
####        print("________________________________\n")
