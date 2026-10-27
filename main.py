# Case folding
txt = "Hello,And Welcome to My World"
# print(txt)
x = txt.casefold()
# print(x)
y = txt.lower()
# print(y)

# Special Character removal
import re
# Input string
input_str = "hello how are & you"
clean_str = re.sub(r"[^a-zA-z0-9\s]","",input_str)
# print(clean_str)
import spacy
# Load spacy model
nlp = spacy.load("en_core_web_sm")
# Function to define clean string
def clean_text(text):
    cleaned_text = ''.join(char for char in text if char.isalpha() or char.isspace())
    doc = nlp(cleaned_text)
    return ' '.join(token.text for token in doc)
# Final output
# clean_str2 = clean_text(input_str)
# print(clean_str2)
import nltk
nltk.download('punkt')
# Tokenize
tokens = nltk.word_tokenize(input_str)
# print(tokens)
# Remove special characters
clean_tokens = [token for token in tokens if token.isalnum()]
clean_str3 = ' '.join(clean_tokens)
# print(clean_str3)

# HANDLING CONTRACTIONS
import contractions
txt2 = "I can't believe it's already raining"
expanded_text = contractions.fix(txt2)
print(expanded_text)
# Method for dealing with cntractions
def expand_contractions(text):
    contractions_pattern = {
        r"(?i)can't" : "cannot",
        r"(?i)won.t" : "will not",
        r"(?i)it's" : "it is",
        r"(?i)weren't" : "were not",
        r"(?i)I'm" : "I am",
    }
    for contraction,expansion in contractions_pattern.items():
        text = re.sub(contraction,expansion,text)
    return text
expanded_text = expand_contractions(txt2)
print(expanded_text)

# TOKENIZATION
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
# Sample text for tokenization
txt3 = "NLTK provides powerful tools for tokenization. It includes word tokenization and sentence tokenization"
# Word tokenization
words = word_tokenize(txt3)
print(words)
# Sentence tokenization
sentence = sent_tokenize(txt3)
print(sentence)

# STOP WORDS REMOVAL
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Sample sentence
sentence = "This is a sample sentence,showing off the stop words filtration."
words = word_tokenize(sentence)
# Filter stop words
new_sentence = [word for word in words if word.lower() not in stopwords.words('english')]
print(sentence)
print(new_sentence)

# N-grams(Unigrams,Bigrams,Trigrams)
import nltk
from nltk.tokenize import word_tokenize
from nltk import ngrams
nltk.download('punkt')

def generate_ngrams(text,n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens,n))
    return n_grams
# Example text
txt4 = "N-Grams are a sequence of n items from a given sample of text or speech"
unigrams = generate_ngrams(txt4,1)
bigrams = generate_ngrams(txt4,2)
trigrams = generate_ngrams(txt4,3)
print(unigrams)
print(bigrams)
print(trigrams)