import nltk

file = open("log.txt")
corpus = file.read()

num_dialog = StringUtils.countMatches("corpus", "<dialog>")
num_utt = StringUtils.countMatches("corpus", "<utt>")

corpus_string = corpus.re.sub('([$@*&?]).*?\1(.*)', ' ', corpus)

stop_words = set(stopwords.words('spanish'))

tokens =  nltk.word_tokenize(corpus)
num_tokens = len(tokens)

words_filtered = []
for token in tokens:
    if token not in stop_words:
        words_filtered.append(token)

num_words =  len(words_filtered)

fdist = FreqDist(words)
top_twenty = fdist.most_common(20)


