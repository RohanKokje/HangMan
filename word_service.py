import json
import random
class WordService:
    def loadDictonary(self):
        with open("dictionary.json") as f:
            self.dictonary=json.load(f)
    def showDictonary(self):
        print(len(self.dictonary))
    def getRandomWord(self):
        num=random.randint(1,len(self.dictonary))
        print(num)
        keys=list(self.dictonary.items())
        wordmeaning=keys[num]
        print(wordmeaning) 
        return wordmeaning
word_service_instance=WordService()
word_service_instance.loadDictonary()
word_service_instance.getRandomWord()