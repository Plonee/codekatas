class Anagram:
    def __init__(self, inner_text):
        self.inner_text = inner_text

    def __repr__(self):
        return 'inner: ' + self.inner_text

    def is_anagram_with(self, another_text):
        return self.is_same(self.inner_text,another_text)

    def is_same(self, text_base, text_to_compare):
        return self.sorted_words_equals(text_base, text_to_compare)

    def sorted_words_equals(self, text, text_to_compare):
        return self.sort_word(text).__eq__(self.sort_word(text_to_compare))

    def sort_word(self, text):
        return sorted(text, key=str.lower)