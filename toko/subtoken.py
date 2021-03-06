# -*- coding: utf-8 -*-

class Subtoken(object):
    
    
    def __init__(self, form):
        '''
        Construct a new Token instance

        - form - basically a sentence (whatever is written on each
        line of the input file)
        - __spaces -- a list of 0s and 1s indicating whether a subtoken
        is followed by a whitespace.
        - __sub_tokens -- a list of strings (subtokens)
        - __sub_tokens_cat -- a list of strings indicating the
        character classes of the subtokens in __sub_tokens
        '''
        self.__form = form
        self.__spaces = list()
        self.__sub_tokens = list()
        self.__sub_tokens_cats = list()
        self.__ptb_special_cases = ["Gonna", "gonna", "Gimme", "gimme", \
                                    "Gotta", "gotta", "lemme", "Lemme", \
                                    "wanna", "Wanna", "cannot", "Cannot"]


    def __get_category(self, ch):
        '''
        given a character, __get_category returns its class if the
        character doens't belong to any class, then its class will be
        the character itself.
        
        - ch -- input character
        returns a `string', ch. class
        '''

        # first, the category of any char. would be the char. itself.
        category = ch

        
        if (ch.isupper() and ch.isalpha()):
            category = "alphaC"
            
        elif ch.isalpha():
            category = "alpha"
            
        elif ch.isdigit():
            category = "num"
            
        elif ch.isspace():
            category = "SPACE"
            
        elif ch == '-':
            category = "hyphen"	
            
        elif (ch == '(') or (ch == '{') or (ch == '[') or (ch == '<'):
            category = "OP"	
            
        elif (ch == ')') or (ch == '}') or (ch == ']') or (ch == '>'):
            category = "CP"
            
        elif ch == ',':
            category = "comma"
            
        elif ch == '.':
            category = "dot"
            
        elif ch == ':':
            category = "colon"
            
        elif ch == ';':
            category = "semicolon"
            
        elif ch == '\'':
            category = "SQ"
            
        elif ch == '"':
            category = "DQ"
            
        elif ch == '`':
            category = "OQ"
            
        elif ch == '—':
            category = "dash"
            
        elif ch == '/':
            category = "fslash"
            
        elif ch == '\\':
            category = "bslash"
            
        return category;	 
        

    def subtokenize(self):
        '''
        Given a stream of characters, returns, inter alia, a list of
        so-called subtokens.

        the function reads char. by char. from the input text, as long
        as the character class (ch. class) of the chars being read is
        the same the chars are grouped in one subtoken.
        returns: 
        - self.__sub_tokens -- a list of subtokens
        - self.__sub_tokens_cats -- a list of character classes
        (categories)
        - self.__spaces -- a list indicating whether or not the
        subtoken is followed by a space
        '''
        wasSpace = True
        index = begin = 0
        prev_cat = self.__get_category(self.__form[index])

        while index < len(self.__form):
            current_cat = self.__get_category(self.__form[index])
            if self.__same_category(prev_cat, current_cat) == 0:

                if prev_cat == "SPACE":
                    self.__spaces.append(1)
                    wasSpace = True
                else:
                    if wasSpace:
                        wasSpace = False
                    else:
                        self.__spaces.append(0)
                    self.__sub_tokens_cats.append(prev_cat)

                if not(self.__form[begin:index].isspace()):
                    self.__sub_tokens.append(self.__form[begin:index])
                begin = index
                prev_cat = current_cat
            elif self.__same_category(prev_cat, current_cat) == 2:
                prev_cat = "alphaC"
            index += 1
            
        if prev_cat == "SPACE":
            self.__spaces.append(1)

        else:
            self.__spaces.append(0)
            self.__sub_tokens_cats.append(prev_cat)
            if not(self.__form[begin:index].isspace()):
                self.__sub_tokens.append(self.__form[begin:index])                

        if len(self.__spaces) == ( len(self.__sub_tokens) - 1 ):
            self.__spaces.append(0)
        elif len(self.__spaces) <> len(self.__sub_tokens):
            raise Exception, 'Error in feature extraction, please report the problem'


        # ===========================
        # Handling contractions according to PTB conventions
        # ===========================
        self.__tokenize_contractions()
        

        return self.__sub_tokens, self.__sub_tokens_cats, self.__spaces


    def __same_category(self, prev, current):
        '''
        very simple equivalence function for character classes

        makes sure that a capitalized word wouldn't be split into two
        subtokens, e.g. `Tonight' consists of `T' alphaC (capitalized
        character) and `onight' alpha, but the whole word must be
        treated as alphaC (alpha with the first char capitalized).
        '''
        if prev == "alphaC" and current == "alpha":
            return 2
        elif prev == current:
            return 1
        else:
            return 0


        
    def __tokenize_contractions(self):
        '''
        Handle contractions such as don't, wouldn't and cannot.
        
        In the character classes approach, `cannot' is one subtoken
        (alpha) and `wouldn't' is `wouldn', `'' and `t', whereas in
        the PTB `cannot' must be `can' and `not'; and `wouldn't' must
        be `would' and `n't'.

        The cases considered below can be found in the original
        tokenization script of PTB:
        http://www.cis.upenn.edu/~treebank/tokenizer.sed
        '''
        
        new_sub_tokens = list()

        for i in range( len(self.__sub_tokens) - 2):
            '''
            wouldn't, couldn't, etc.
            '''
            if self.__sub_tokens[i+1] == "'" \
                and (self.__sub_tokens[i+2] == "t" or self.__sub_tokens[i+2] == "T") \
                and (self.__sub_tokens[i][-1] == 'n' or self.__sub_tokens[i][-1] == "N"):
                
                new_sub_tokens.append(self.__sub_tokens[i][0:-1])
                new_sub_tokens.append(self.__sub_tokens[i][-1])
                self.__spaces.insert(len(new_sub_tokens) - 1, 0)            
                self.__sub_tokens_cats.insert(len(new_sub_tokens) - 1, \
                                              self.__get_category(self.__sub_tokens[i][-1]))
                
            elif self.__sub_tokens[i] in self.__ptb_special_cases:
                new_sub_tokens.append(self.__sub_tokens[i][0:3])
                new_sub_tokens.append(self.__sub_tokens[i][3:])
                self.__spaces.insert(len(new_sub_tokens) - 2, 0)            
                self.__sub_tokens_cats.insert(len(new_sub_tokens) - 1, \
                                              self.__get_category(self.__sub_tokens[i][-1]))
                                              
                #elif self.__sub_tokens[i] == "'" and \
                # self.__sub_tokens[i+1] in ["tis", "Tis", "Twas", "twas"]:            
              
                    
            else:
                new_sub_tokens.append(self.__sub_tokens[i])

        for i in range( ( len(self.__sub_tokens) - 2), len(self.__sub_tokens)):
            if i >= 0:
                if self.__sub_tokens[i] in self.__ptb_special_cases:
                    new_sub_tokens.append(self.__sub_tokens[i][0:3])
                    new_sub_tokens.append(self.__sub_tokens[i][3:])
                    self.__spaces.insert( len(new_sub_tokens) - 1, 0)            
                    self.__sub_tokens_cats.insert( len(new_sub_tokens) - 2,\
                                                  self.__get_category(self.__sub_tokens[i][-1]))
                else:
                    new_sub_tokens.append(self.__sub_tokens[i])

        if len(self.__sub_tokens) <> len(self.__spaces):
            self.__sub_tokens = new_sub_tokens
                
