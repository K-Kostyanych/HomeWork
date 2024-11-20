class WordsFinder:
    file_names = []
    def __init__(self, *filenames):
       self.file_names = filenames

    def get_all_words(self):
        all_words = {} # Создаем пустой словарь для хранения слов из файлов
        for file_name in self.file_names:
            with open(file_name, 'r',encoding='utf-8') as file:
                text = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuation,'')
                words = text.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            for i, w in enumerate(words):
                if w == word:
                    result[file_name] = i
        return result

    def count(self,word ):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result




finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words()) # Все слова
print(finder1.find('TEXT')) # 3 слово по счёту
print(finder1.count('teXT')) # 4 слова teXT в тексте всего

finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('the'))
print(finder2.count('the'))








