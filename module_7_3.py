class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = ""
                for line in file:
                    text += line.replace("\n"," ").lower()
                    # replace symbols
                for symbol in symbols:
                    text = text.replace(symbol, "")

                # write words
                all_words[file_name] = text.split(" ")
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        search = {}
        for key, value in all_words.items():
            if word.lower() in value:
                search[key] = value.index(word.lower()) + 1
        return search

    def count(self, word):
        all_words = self.get_all_words()
        search = {}

        for key, value in all_words.items():
            count = value.count(word.lower())
            if count > 0:
                search[key] = count

        return search


finder2 = WordsFinder('test_file.txt', 'products.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
