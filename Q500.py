class Solution(object):
    def findWords(self, words):
        """
        :param words: list[str]
        :return: list[str]
        """
        fuhao = {'{':1,'[':1,'}':1,']':1,':':2,';':2,'"':2,'\'':2,'<':3,',':3,'>':3,'.':3,'?':3,'/':3}
        alpha = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2}
        number = 0
        other_fuhao = 0
        other_alpha = 3
        lenw = len(words)
        result = []
        for i in list(range(lenw)):
            word = words[i].lower()
            lens = len(word)
            loc = -1
            temp = -1
            flag = 0
            for j in list(range(lens)):
                if word[j].isalpha():
                    if alpha.get(word[j]) == None:
                        temp = other_alpha
                    else:
                        temp = alpha.get(word[j])
                    pass
                elif word[j].isdigit():
                    temp = 0
                else:
                    if word[j].isspace():
                        temp = 4
                    else:
                        if fuhao.get(word[j]) == None:
                            temp = 0
                        else:
                            temp = fuhao.get(word[j])
                    pass
                # print("temp:",temp)
                if loc == -1:
                    loc = temp
                else:
                    if loc != temp:
                        flag = -1
                        break
            if flag == 0:
                result.append(words[i])
        return result
        pass

if __name__ == "__main__":
    lists = ["Hello","Alaska","Dad","Peace","!@@!12","121qw","{}"]
    print(Solution().findWords(lists))