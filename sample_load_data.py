import opencorpora
corpus = opencorpora.load('/wiki_corpus_2.01/BDS/BDS00389.xml')
corpus.getchildren()
corpus[1][0].text
encoded_data = corpus[1][0].text.encode('utf-8')
for each_unicode_character in encoded_data.decode('utf-8'):
    print each_unicode_character
