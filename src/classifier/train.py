from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
import spacy

import string
punctuations = string.punctuation

nlp = spacy.load('en')

class Train:
    def __init__(self):
        self.pipe = None

    def train(self, data):
        #Custom transformer using spaCy
        class predictors(TransformerMixin):
            def transform(self, X, **transform_params):
                return [clean_text(text) for text in X]
            def fit(self, X, y=None, **fit_params):
                return self
            def get_params(self, deep=True):
                return {}

        # Basic utility function to clean the text
        def clean_text(text):
            return text.strip().lower()


        #Create spacy tokenizer that parses a sentence and generates tokens
        #these can also be replaced by word vectors
        def spacy_tokenizer(sentence):
            tokens = nlp(sentence)
            tokens = [tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_ for tok in tokens]
            tokens = [tok for tok in tokens if (tok not in stopwords and tok not in punctuations)]
            return tokens

        #create vectorizer object to generate feature vectors, we will use custom spacy’s tokenizer
        vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
        classifier = LinearSVC()

        # Create the  pipeline to clean, tokenize, vectorize, and classify
        self.pipe = Pipeline([('cleaner', predictors()),
                         ('vectorizer', vectorizer),
                         ('classifier', classifier)])

        labels = []
        fragments = []
        def append(x):
            labels.append(x[1])
            fragments.append(x[0])

        [append(x) for x in data]
        # Create model and measure accuracy
        self.pipe.fit(fragments, labels)

    def get_trained_model(self):
        return self.pipe
