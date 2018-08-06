#!/usr/bin/env python3

import argparse


def train(args):
    classifier = Classifier()
    classifier.train(args.filepath)


def predict(args):
    classifier = Classifier()
    print('{}: {}'.format(args.sentence, classifier.predict(args.sentence)))


def validate(args):
    classifier = Classifier()
    classifier.validate(args.filepath, args.split)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Classifiers for formality, informativeness, and '
                        'implicature trained on the SQUINKY! corpus.'
        )
    subparsers = parser.add_subparsers(title='Commands', dest='command')
    subparsers.required = True

    parser_train = subparsers.add_parser(
            'train', help='Train SQUINKY! classifier.'
        )
    parser_train.add_argument(
            'filepath',
            help='The absolute path to a file containing the training data.'
        )
    parser_train.set_defaults(handler=train)

    parser_validate = subparsers.add_parser(
            'validate', help='Train the classifiers with the given train/test '
                             'split and report performance.'
        )
    parser_validate.add_argument(
            'filepath',
            help='The absolute path to a file containing the training data.'
        )
    parser_validate.add_argument(
            '-s', '--split', type=float, action="store",
            help='The percentage of data to withhold for testing.'
        )
    parser_validate.set_defaults(handler=validate)

    parser_predict = subparsers.add_parser(
            'predict', help='Predict formality, informativeness, and '
                            'implicature of a sentence.'
        )
    parser_predict.add_argument(
            'sentence',
            help='A sentence for which the formality, informativeness, and '
                 'implicature are to be predicted.'
        )
    parser_predict.set_defaults(handler=predict)
    args = parser.parse_args()

    from squinky.classifier import Classifier
    args.handler(args)
