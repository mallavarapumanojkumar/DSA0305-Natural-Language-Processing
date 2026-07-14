import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required packages (run once)
nltk.download('wordnet')

ps = PorterStemmer()
lm = WordNetLemmatizer()

word = input("Enter a word: ")

stem_word = ps.stem(word)
lemma_word = lm.lemmatize(word)

print("Original Word :", word)
print("Stemmed Word  :", stem_word)
print("Lemmatized Word :", lemma_word)
