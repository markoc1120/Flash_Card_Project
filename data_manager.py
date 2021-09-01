import pandas
import random


class Data:

    def __init__(self):
        try:
            self.data = pandas.read_csv('./data/words_to_learn.csv').to_dict(orient='records')
        except FileNotFoundError:
            self.data = pandas.read_csv('./data/deutsch_words.csv').to_dict(orient='records')
        self.row = None

    def random_row(self):
        self.row = random.choice(self.data)

    def remove_row(self):
        self.data.remove(self.row)
        df = pandas.DataFrame(self.data)
        df.to_csv('./data/words_to_learn.csv', index=False)
