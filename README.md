# squinky

## Description
This is an interface to a pre-trained _formality_, _informativenes_, and _implicature_ classifier trained on the `SQUINKY!` corpus. The `SQUINKY!` corpus is a collection of 7,032 sentences annotated manually for _formality_, _informativeness_, and _implicature_. For details on the corpus and the annotation process, please see `Lahiri (2015)`:

```
    Lahiri, S. (2015). SQUINKY! A Corpus of Sentence-level Formality, Informativeness, and
    Implicature. Ann Arbor, 1001, 48109. https://arxiv.org/pdf/1506.02306.pdf
```
Each of the three annotations have their own logistic regression classifier trained on various syntactic features of natural language, borrowed from the (unrelated) thesis by `Vincze (2015)`. Please consult the thesis for details on feature selection/generation:

```
    Vincze, V. (2015). Uncertainty detection in natural language texts (Doctoral dissertation, szte).
```

This interface outputs probabilities of the positive and negative classes, for each of the three annotations, for a given sentence. For example, given the sentence "A BIG THANKYOU GOES TO holli!", the output will be:

```
    ({'formal': 0.0041114378047021338, 'informal': 0.99588856219529787},
     {'informative': 0.011593792054814324, 'ambiguous': 0.98840620794518563},
     {'implicative': 0.95996335945188804, 'verbose': 0.040036640548111957})
```

It is strongly recommended that you read `Lahiri (2015)` before attempting to interpret the results -- informativeness and implicature are complicated concepts and their meaning should not be assumed.

## Installation

``` bash
    sudo pip3 install squinky
```

## Usage

``` bash
    # Train the classifiers using the provided training data.
    squinky train /path/to/data.csv
    # Validate the precision, recall, and f1-score for the provided training data
    # using a 25% train/test split.
    squinky validate --split=0.25 /path/to/data.csv
    # Predict the Formality, Informativeness, and Implicature of the given sentence.
    squinky predict "This is a test sentence."
```

## Validation

The formality, informativeness, and implicature classifiers have the following precision, recall, and f1-scores:

```
                        Precision    Recall    F1-Score
          Formality:    0.82         0.82      0.82
    Informativeness:    0.84         0.84      0.84
        Implicature:    0.60         0.60      0.60
```

Lahiri (2015) provided a set of sample sentences with formality, informativeness, and implicature annotations. These classifiers have been validated against those examples. Examples `[3]` and `[6]` fail for informativeness and implicature, respectively.

<table>
  <tr>
    <th></th>
    <th></th>
    <th colspan="3">Expected</th>
    <th colspan="3">Predicted</th>
  </tr>
  <tr>
    <td></td>
    <td>Example from Lahiri (2015)</td>
    <td>FORM</td>
    <td>INFO</td>
    <td>IMPL</td>
    <td>FORM</td>
    <td>INFO</td>
    <td>IMPL</td>
  </tr>
  <tr>
    <td>[1]</td>
    <td>A BIG THANKYOU GOES TO holli!</td>
    <td>Low</td>
    <td>Low</td>
    <td>-</td>
    <td>Low</td>
    <td>Low</td>
    <td>High</td>
  </tr>
  <tr>
    <td>[2]</td>
    <td>As Maoists menace continued to be unabated, the government is all set to launch the much-awaited full-fledged anti-Naxal operations at three different areas, considered trijunctions of worst Naxal-affected states.</td>
    <td>High</td>
    <td>High</td>
    <td>-</td>
    <td>High</td>
    <td>High</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>[3]</td>
    <td>4) 'We find no clear relation between income inequality and class-based voting.'</td>
    <td>High</td>
    <td>Low</td>
    <td>-</td>
    <td>High</td>
    <td>High</td>
    <td>High</td>
  </tr>
  <tr>
    <td>[4]</td>
    <td>2) Just wipe the Mac OS X partition when u install the dapper.</td>
    <td>Low</td>
    <td>High</td>
    <td>-</td>
    <td>Low</td>
    <td>High</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>[5]</td>
    <td>alright, well, i guess i just made a newbie mistake.</td>
    <td>Low</td>
    <td>-</td>
    <td>High</td>
    <td>Low</td>
    <td>Low</td>
    <td>High</td>
  </tr>
  <tr>
    <td>[6]</td>
    <td>All seven aboard the Coast Guard plane are stationed at the Coast Guard Air Station in Sacramento, Calif., where their aircraft was based.</td>
    <td>High</td>
    <td>-</td>
    <td>High</td>
    <td>High</td>
    <td>High</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>[7]</td>
    <td>Maoists sabotaged Essar's 166-mile underground pipeline, which transfers slurry from one of India's most coveted iron ore deposits to the Bay of Bengal.</td>
    <td>High</td>
    <td>-</td>
    <td>Low</td>
    <td>High</td>
    <td>High</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>[8]</td>
    <td>Wait.</td>
    <td>Low</td>
    <td>-</td>
    <td>Low</td>
    <td>Low</td>
    <td>Low</td>
    <td>Low</td>
  </tr>
</table>
