# Import necessary modules
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)


# //////

# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w]+:"
print(re.match(pattern2, sentences[3]))