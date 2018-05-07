class Anagram:
    def __init__(self, inner_text):
        self.inner_text = inner_text

    def __repr__(self):
        return 'inner: ' + self.inner_text

    def is_anagram_with(self, another_text):
        return self.inner_text

    def is_same(self, text_base, text_to_compare):
        return str(text_base).lower().__eq__(str(text_to_compare).lower())
