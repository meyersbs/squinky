from nltk import word_tokenize, pos_tag

from .lib.nlp.chunktagger import ChunkTagger
from .lib.nlp.lemmatizer import NLTKLemmatizer
from .lib.nlp.stemmer import Stemmer
from .word import Word
from .constants import FORM_LABS, INFO_LABS, IMPL_LABS

CHUNKER = ChunkTagger()

class Sentence(object):
    def __init__(self, sentence, formality=0, informativeness=0, implicature=0):
        self.sentence = sentence
        self.form = FORM_LABS[0] if formality > 4 else FORM_LABS[1]
        self.info = INFO_LABS[0] if informativeness > 4 else INFO_LABS[1]
        self.impl = IMPL_LABS[0] if implicature > 4 else IMPL_LABS[1]
        self.words = list()

        tokens = word_tokenize(self.sentence)
        pos_tags = pos_tag(tokens)
        chunks = CHUNKER.parse(pos_tags)

        lemmatizer = NLTKLemmatizer(tokens)
        stemmer = Stemmer(tokens)

        lemmas = lemmatizer.execute()
        stems = stemmer.execute()

        for i, token in enumerate(pos_tags):
            prev_word = pos_tags[i-1][0] if i-1 >= 0 else None
            next_word = pos_tags[i+1][0] if i+1 < len(pos_tags) else None
            w = Word(token[0], token[1], i, self.form, self.info, self.impl,
                     prev_word, next_word, chunks[i], lemmas[i], stems[i])
            self.words.append(w)

    def get_sentence(self):
        return self.sentence

    def get_labels(self):
        return self.form, self.info, self.impl

    def get_words(self):
        return self.words

    def get_features(self):
        feats = dict()
        for word in self.words:
            feats.update(word.get_features())

        return feats
