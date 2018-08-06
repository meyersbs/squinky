from pkg_resources import resource_filename

FORM_CLASSIFIER_PATH = resource_filename('squinky', 'models/form_classifier.p')
FORM_VECTORIZER_PATH = resource_filename('squinky', 'vectorizers/form_vectorizer.p')

INFO_CLASSIFIER_PATH = resource_filename('squinky', 'models/info_classifier.p')
INFO_VECTORIZER_PATH = resource_filename('squinky', 'vectorizers/info_vectorizer.p')

IMPL_CLASSIFIER_PATH = resource_filename('squinky', 'models/impl_classifier.p')
IMPL_VECTORIZER_PATH = resource_filename('squinky', 'vectorizers/impl_vectorizer.p')

FORM_LABS = ['F', 'R'] # Formal vs. Informal
INFO_LABS = ['N', 'A'] # Informative vs. Ambiguous
IMPL_LABS = ['I', 'V'] # Implicative vs. Verbose
