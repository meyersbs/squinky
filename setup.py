from setuptools import setup

setup(
        name='squinky',
        version='0.1.0',
        packages=[
            'squinky', 'squinky.data', 'squinky.lib', 'squinky.lib.nlp'
        ],
        package_data={
            'squinky': ['models/*.p', 'vectorizers/*.p'],
            'squinky.lib.nlp': ['verbs.txt']
        },
        install_requires=[
            'numpy==1.12.1',
            'scipy==0.19.0',
            'scikit-learn==0.18.1',
            'nltk==3.2.2'
        ],
        license='The MIT License (MIT) Copyright (c) 2017 Benjamin S. Meyers',
        description='Classifiers for formality, informativeness, and '
                    'implicature trained on the SQUINKY! corpus.',
        author='Benjamin S. Meyers',
        author_email='bsm9339@rit.edu',
        url='https://github.com/meyersbs/squinky',
        test_suite='squinky.tests',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Linguistic'
        ],
        keywords=[
            'nlp', 'natural language', 'natural language processing',
            'formality', 'informativeness', 'implicature', 'squinky'
        ]
    )
