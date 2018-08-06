import csv

from os import path

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split as TTS

from . import constants, helpers
from .sentence import Sentence


class Classifier(object):
    def __init__(self):
        self.form_classifier = None
        self.form_vectorizer = None
        self.info_classifier = None
        self.info_vectorizer = None
        self.impl_classifier = None
        self.impl_vectorizer = None


    def validate(self, filepath, split=0.25):
        if not path.exists(filepath):
            raise FileNotFoundError('No such file: {}'.format(filepath))

        with open(filepath, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            next(csv_reader, None) # Skip header row

            sents = dict()
            for sentence in csv_reader:
                sent = Sentence(sentence[-1], float(sentence[1],),
                                float(sentence[2]), float(sentence[3]))
                sents[int(sentence[0])] = sent

        X, y_form, y_info, y_impl = list(), list(), list(), list()
        for key, sent in sents.items():
            X.append(sent.get_features())
            labs = sent.get_labels()
            y_form.append(labs[0])
            y_info.append(labs[1])
            y_impl.append(labs[2])

        # FORMALITY
        X_form_train, X_form_test, y_form_train, y_form_test = \
            TTS(X, y_form, test_size=split)

        self.form_vectorizer = DictVectorizer()
        X_form_train = self.form_vectorizer.fit_transform(X_form_train)
        self.form_classifier = LogisticRegression()
        self.form_classifier.fit(X_form_train, y_form_train)

        X_form_test = self.form_vectorizer.transform(X_form_test)
        y_preds_form = self.form_classifier.predict(X_form_test)

        print(classification_report(y_form_test, y_preds_form))
        print("\n")
        tn, fp, fn, tp = confusion_matrix(y_form_test, y_preds_form).ravel()
        print("TP: {}".format(tp))
        print("TN: {}".format(tn))
        print("FP: {}".format(fp))
        print("FN: {}".format(fn))
        
        # INFORMATIVENESS
        X_info_train, X_info_test, y_info_train, y_info_test = \
            TTS(X, y_info, test_size=split)

        self.info_vectorizer = DictVectorizer()
        X_info_train = self.info_vectorizer.fit_transform(X_info_train)
        self.info_classifier = LogisticRegression()
        self.info_classifier.fit(X_info_train, y_info_train)

        X_info_test = self.info_vectorizer.transform(X_info_test)
        y_preds_info = self.info_classifier.predict(X_info_test)

        print(classification_report(y_info_test, y_preds_info))
        print("\n")
        tn, fp, fn, tp = confusion_matrix(y_info_test, y_preds_info).ravel()
        print("TP: {}".format(tp))
        print("TN: {}".format(tn))
        print("FP: {}".format(fp))
        print("FN: {}".format(fn))

        # IMPLICATURE
        X_impl_train, X_impl_test, y_impl_train, y_impl_test = \
            TTS(X, y_impl, test_size=split)

        self.impl_vectorizer = DictVectorizer()
        X_impl_train = self.impl_vectorizer.fit_transform(X_impl_train)
        self.impl_classifier = LogisticRegression()
        self.impl_classifier.fit(X_impl_train, y_impl_train)

        X_impl_test = self.impl_vectorizer.transform(X_impl_test)
        y_preds_impl = self.impl_classifier.predict(X_impl_test)

        print(classification_report(y_impl_test, y_preds_impl))
        print("\n")
        tn, fp, fn, tp = confusion_matrix(y_impl_test, y_preds_impl).ravel()
        print("TP: {}".format(tp))
        print("TN: {}".format(tn))
        print("FP: {}".format(fp))
        print("FN: {}".format(fn))


    def train(self, filepath):
        if not path.exists(filepath):
            raise FileNotFoundError('No such file: {}'.format(filepath))

        with open(filepath, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            next(csv_reader, None) # Skip header row

            sents = dict()
            for sentence in csv_reader:
                sent = Sentence(sentence[-1], float(sentence[1],),
                                float(sentence[2]), float(sentence[3]))
                sents[int(sentence[0])] = sent

        X, y_form, y_info, y_impl = list(), list(), list(), list()
        for key, sent in sents.items():
            X.append(sent.get_features())
            labs = sent.get_labels()
            y_form.append(labs[0])
            y_info.append(labs[1])
            y_impl.append(labs[2])

        # Formality
        self.form_vectorizer = DictVectorizer()
        Xx = self.form_vectorizer.fit_transform(X)
        self.form_classifier = LogisticRegression()
        self.form_classifier.fit(Xx, y_form)
        # Informativeness
        self.info_vectorizer = DictVectorizer()
        Xx = self.info_vectorizer.fit_transform(X)
        self.info_classifier = LogisticRegression()
        self.info_classifier.fit(Xx, y_info)
        # Implicature
        self.impl_vectorizer = DictVectorizer()
        Xx = self.impl_vectorizer.fit_transform(X)
        self.impl_classifier = LogisticRegression()
        self.impl_classifier.fit(Xx, y_impl)

        self._dump()


    def predict(self, data):
        if self.form_classifier is None or self.form_vectorizer is None or \
            self.info_classifier is None or self.info_vectorizer is None or \
            self.impl_classifier is None or self.impl_vectorizer is None:

            self._load()

        sent = Sentence(data)
        X = sent.get_features()

        Xx = self.form_vectorizer.transform(X)
        y_probs = list(self.form_classifier.predict_proba(Xx))
        form_preds = {"formal": y_probs[0][0], "informal": y_probs[0][1]}
        print(self.form_classifier.predict(Xx))
        Xx = self.info_vectorizer.transform(X)
        y_probs = list(self.info_classifier.predict_proba(Xx))
        info_preds = {"informative": y_probs[0][1], "ambiguous": y_probs[0][0]}
        print(self.info_classifier.predict(Xx))
        Xx = self.impl_vectorizer.transform(X)
        y_probs = list(self.impl_classifier.predict_proba(Xx))
        impl_preds = {"implicative": y_probs[0][0], "verbose": y_probs[0][1]}
        print(self.impl_classifier.predict(Xx))

        return form_preds, info_preds, impl_preds


    def _dump(self):
        helpers.dump(self.form_classifier, constants.FORM_CLASSIFIER_PATH)
        helpers.dump(self.form_vectorizer, constants.FORM_VECTORIZER_PATH)

        helpers.dump(self.info_classifier, constants.INFO_CLASSIFIER_PATH)
        helpers.dump(self.info_vectorizer, constants.INFO_VECTORIZER_PATH)

        helpers.dump(self.impl_classifier, constants.IMPL_CLASSIFIER_PATH)
        helpers.dump(self.impl_vectorizer, constants.IMPL_VECTORIZER_PATH)


    def _load(self):
        self.form_classifier = helpers.load(constants.FORM_CLASSIFIER_PATH)
        self.form_vectorizer = helpers.load(constants.FORM_VECTORIZER_PATH)

        self.info_classifier = helpers.load(constants.INFO_CLASSIFIER_PATH)
        self.info_vectorizer = helpers.load(constants.INFO_VECTORIZER_PATH)

        self.impl_classifier = helpers.load(constants.IMPL_CLASSIFIER_PATH)
        self.impl_vectorizer = helpers.load(constants.IMPL_VECTORIZER_PATH)
