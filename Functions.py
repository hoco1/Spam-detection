from contractions import CONTRACTION_MAP
import re
def expand_contractions(text, map=CONTRACTION_MAP):
    '1- Expanding Contraction'
    pattern = re.compile('({})'.format('|'.join(map.keys())), flags=re.IGNORECASE|re.DOTALL)
    def get_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded = map.get(match) if map.get(match) else map.get(match.lower())
        expanded = first_char+expanded[1:]
        return expanded     
    new_text = pattern.sub(get_match, text)
    new_text = re.sub("'", "", new_text)
    return new_text

import string 
import unicodedata
def preprocessStepOne(text):
    '''
    2- lowercase
    3- remove numbers
    4- remove punctuation
    5- remove accented characters
    6- removing extra whitespaces and tabs
    '''
    text = text.lower()
    text = re.sub(r'\d+','',text)
    text = ''.join([c for c in text if c not in string.punctuation])
    text = unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode('utf-8','ignore')
    pattern = r'^\s*|\s\s*'
    text = re.sub(pattern, ' ', text).strip()
    return text

import nltk
# nltk.download('stopwords')
from nltk.tokenize import ToktokTokenizer
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
# custom: removing words from list
stopword_list.remove('not')# function to remove stopwords
def remove_stopwords(text):
    '7- remove stop words'
    # convert sentence into token of words
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    # check in lowercase 
    t = [token for token in tokens if token.lower() not in stopword_list]
    text = ' '.join(t)    
    return text

def get_stem(text):
    '8- text stemming'
    stemmer = nltk.porter.PorterStemmer()
    return ' '.join([stemmer.stem(word) for word in text.split()])

