from .helpers import get_wordpattern

class Word(object):
    def __init__(self, word, pos, position, form, info, impl, prev, next, chunk,
                 lemma, stem):
        self.word = word
        self.pos = pos
        self.position = position
        self.form = form
        self.info = info
        self.impl = impl
        self.prev = prev
        self.next = next
        self.chunk = chunk
        self.pattern = get_wordpattern(self.word)
        self.prefixes = ['prefix_{}_{}'.format(i, self.word[:i]) for i in [3, 4, 5]]
        self.suffixes = ['suffix_{}_{}'.format(i, self.word[-i:]) for i in [3, 4, 5]]
        self.lemma = lemma
        self.stem = stem

    def get_word(self):
        return self.word

    def get_pos(self):
        return self.pos

    def get_position(self):
        return self.position

    def get_labels(self):
        return self.form, self.info, self.impl

    def get_features(self):
        feats = {
                "IND_" + str(self.position):1.0,
                "POS_" + str(self.pos):1.0,
                "LEM_" + str(self.lemma):1.0,
                "STM_" + str(self.stem):1.0,
                "PAT_" + str(self.pattern):1.0,
                "CUR_" + str(self.word):1.0,
                "CNK_" + str(self.chunk):1.0,
            }
        if self.prev is not None:
            feats.update({"PRV_" + str(self.prev):1.0})
        if self.next is not None:
            feats.update({"NXT_" + str(self.next):1.0})
        for p in self.prefixes:
            feats.update({"PRE_" + str(p):1.0})
        for s in self.suffixes:
            feats.update({"SUF_" + str(s):1.0})

        return feats
