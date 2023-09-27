class WordDictionary:

    def __init__(self, document):
        self.document = document # The text
        self.dictionary = {}  # Initialize an empty dictionary


    def count_words(self):
        words = self.document.split()
        return words

    def add_word(self, word, position):
        if word in self.dictionary:
            self.dictionary[word].append(position)
        else:
            self.dictionary[word] = [position]

    def add_words_and_positions(self):
        words = self.count_words()
        for position, word in enumerate(words):
            self.add_word(word, position)

    def print_word_locations(self):
        print("Word locations:", self.dictionary)

    def print_word_count(self):
        words = self.count_words()
        word_count = len(words)
        print("Number of words:", word_count)

    def final(self):
        self.add_words_and_positions()
        self.print_word_locations()
        self.print_word_count()



thing = "Greg understood that this situation would make Michael terribly uncomfortable. Michael simply had no idea what was about to come and even though Greg could prevent it from happening, he opted to let it happen. It was quite ironic, really. It was something Greg had said he would never wish upon anyone a million times, yet here he was knowingly letting it happen to one of his best friends. He rationalized that it would ultimately make Michael a better person and that no matter how uncomfortable, everyone should experience racism at least once in their lifetime."
Call = WordDictionary(document=thing)
