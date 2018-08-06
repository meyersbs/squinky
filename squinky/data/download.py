from urllib.request import urlretrieve
from urllib.parse import urljoin

DATASETS = ['mturk_merged.csv']
URL = 'http://people.rc.rit.edu/~bsm9339/corpora/squinky_corpus/'


def download():
    print('Download Training Data Files')
    for (index, dataset) in enumerate(DATASETS):
        url = urljoin(URL, dataset)
        urlretrieve(url, dataset)
        print('  [{}/{}] {}'.format(index + 1, len(DATASETS), dataset))


if __name__ == "__main__":
    download()
