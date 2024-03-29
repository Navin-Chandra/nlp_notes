# Import necessary modules
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
scene_one="SCENE 1: [wind] [clop clop clop] \nKING ARTHUR: Whoa there!  [clop clop clop] \nSOLDIER #1: Halt!  Who goes there?\nARTHUR: It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England!\nSOLDIER #1: Pull the other one!\nARTHUR: I am, ...  and this is my trusty servant Patsy.  We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.  I must speak with your lord and master.\nSOLDIER #1: What?  Ridden on a horse?\nARTHUR: Yes!\nSOLDIER #1: You're using coconuts!\nARTHUR: What?\nSOLDIER #1: You've got two empty halves of coconut and you're bangin' 'em together.\nARTHUR: So?  We have ridden since the snows of winter covered this land, through the kingdom of Mercea, through--\nSOLDIER #1: Where'd you get the coconuts?\nARTHUR: We found them.\nSOLDIER #1: Found them?  In Mercea?  The coconut's tropical!\nARTHUR: What do you mean?\nSOLDIER #1: Well, this is a temperate zone.\nARTHUR: The swallow may fly south with the sun or the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land?\nSOLDIER #1: Are you suggesting coconuts migrate?\nARTHUR: Not at all.  They could be carried.\nSOLDIER #1: What?  A swallow carrying a coconut?\nARTHUR: It could grip it by the husk!\nSOLDIER #1: It's not a question of where he grips it!  It's a simple question of weight ratios!  A five ounce bird could not carry a one pound coconut.\nARTHUR: Well, it doesn't matter.  Will you go and tell your master that Arthur from the Court of Camelot is here.\nSOLDIER #1: Listen.  In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right?\nARTHUR: Please!\nSOLDIER #1: Am I right?\nARTHUR: I'm not interested!\nSOLDIER #2: It could be carried by an African swallow!\nSOLDIER #1: Oh, yeah, an African swallow maybe, but not a European swallow.  That's my point.\nSOLDIER #2: Oh, yeah, I agree with that.\nARTHUR: Will you ask your master if he wants to join my court at Camelot?!\nSOLDIER #1: But then of course a-- African swallows are non-migratory.\nSOLDIER #2: Oh, yeah...\nSOLDIER #1: So they couldn't bring a coconut back anyway...  [clop clop clop] \nSOLDIER #2: Wait a minute!  Supposing two swallows carried it together?\nSOLDIER #1: No, they'd have to have it on a line.\nSOLDIER #2: Well, simple!  They'd just use a strand of creeper!\nSOLDIER #1: What, held under the dorsal guiding feathers?\nSOLDIER #2: Well, why not?\n"
# sentences = ['SCENE 1: [wind] [clop clop clop] \nKING ARTHUR: Whoa there!',
#  '[clop clop clop] \nSOLDIER #1: Halt!',
#  'Who goes there?',
#  'ARTHUR: It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.',
#  'King of the Britons, defeator of the Saxons, sovereign of all England!',
#  'SOLDIER #1: Pull the other one!',
#  'ARTHUR: I am, ...  and this is my trusty servant Patsy.',
#  'We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.',
#  'I must speak with your lord and master.',
#  'SOLDIER #1: What?',
#  'Ridden on a horse?',
#  'ARTHUR: Yes!',
#  "SOLDIER #1: You're using coconuts!",
#  'ARTHUR: What?',
#  "SOLDIER #1: You've got two empty halves of coconut and you're bangin' 'em together.",
#  'ARTHUR: So?',
#  "We have ridden since the snows of winter covered this land, through the kingdom of Mercea, through--\nSOLDIER #1: Where'd you get the coconuts?",
#  'ARTHUR: We found them.',
#  'SOLDIER #1: Found them?',
#  'In Mercea?',
#  "The coconut's tropical!",
#  'ARTHUR: What do you mean?',
#  'SOLDIER #1: Well, this is a temperate zone.',
#  'ARTHUR: The swallow may fly south with the sun or the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land?',
#  'SOLDIER #1: Are you suggesting coconuts migrate?',
#  'ARTHUR: Not at all.',
#  'They could be carried.',
#  'SOLDIER #1: What?',
#  'A swallow carrying a coconut?',
#  'ARTHUR: It could grip it by the husk!',
#  "SOLDIER #1: It's not a question of where he grips it!",
#  "It's a simple question of weight ratios!",
#  'A five ounce bird could not carry a one pound coconut.',
#  "ARTHUR: Well, it doesn't matter.",
#  'Will you go and tell your master that Arthur from the Court of Camelot is here.',
#  'SOLDIER #1: Listen.',
#  'In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right?',
#  'ARTHUR: Please!',
#  'SOLDIER #1: Am I right?',
#  "ARTHUR: I'm not interested!",
#  'SOLDIER #2: It could be carried by an African swallow!',
#  'SOLDIER #1: Oh, yeah, an African swallow maybe, but not a European swallow.',
#  "That's my point.",
#  'SOLDIER #2: Oh, yeah, I agree with that.',
#  'ARTHUR: Will you ask your master if he wants to join my court at Camelot?!',
#  'SOLDIER #1: But then of course a-- African swallows are non-migratory.',
#  'SOLDIER #2: Oh, yeah...',
#  "SOLDIER #1: So they couldn't bring a coconut back anyway...  [clop clop clop] \nSOLDIER #2: Wait a minute!",
#  'Supposing two swallows carried it together?',
#  "SOLDIER #1: No, they'd have to have it on a line.",
#  'SOLDIER #2: Well, simple!',
#  "They'd just use a strand of creeper!",
#  'SOLDIER #1: What, held under the dorsal guiding feathers?',
#  'SOLDIER #2: Well, why not?']

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)


# //////
import re
# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w]+:"
print(re.match(pattern2, sentences[3]))


# regexp_tokenize and TweetTokenizer

# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

tweets = ['This is the best #nlp exercise ive found online! #python',
 '#NLP is super fun! <3 #learning',
 'Thanks @datacamp :) #nlp #python']

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@#]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)

# fsdhfkjjsdhfksdhfghsdfkghjksdhgjkhf jdsjf

german_text = "Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕"

# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
capital_words = r"[A-ZÜ]\w+"
# print(regexp_tokenize(capital_words, all_words))
print(regexp_tokenize(german_text, capital_words))


# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))

#  plot the npl token in hist
# Split the script into lines: lines
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, "\w+") for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()