import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Creating Funtions for Text_cleaning(TEXT_preprocess)
def lowers_text(x):
    return x.str.lower()
def special_char(x):
    return x.apply(lambda x : re.sub(r'[^\w\s]',"",x))
def Digits(x):
    return x.apply(lambda x: re.sub(r'\d+', '',x))
def lemma(x):
    from nltk.tokenize import word_tokenize as wt
    list_stp = stopwords.words('english')
    wl = WordNetLemmatizer()
    
    def lemmatize_text(text):
        words = wt(text)
        lemmatized_words = [wl.lemmatize(word,pos="v") for word in words if word not in list_stp ]
        return " ".join(lemmatized_words)
    return x.apply(lemmatize_text)

        

