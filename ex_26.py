def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
# This part is ok

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
# This part is ok

def print_first_word(words): # Needed a colon at the end
	"""Prints the first word after popping it off."""
	word = words.pop(0) # Changed poop to pop
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1) # Added closing parenthesis
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
# This part is ok

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
# This part is ok

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
# This part is ok

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# This part is ok

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""
# This part is ok

print "--------------"
print poem
print "--------------"
# This part is ok

five = 10 - 2 + 3 - 6 # Changed the last number to 6 so the result is 5
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000 # Changed the backslash to foward slash
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # Changed == to =

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) # Changed jeans to beans

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # Changed crabapples to crates and "start_pont" to "start_point"


sentence = "All good things come to those who wait." # Removed \t, changed got to good and weight to wait

words = break_words(sentence) # Removed ex.25
sorted_words = sort_words(words)

print_first_word(words) # Removed "."
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) # Removed ex.25
print sorted_words # Changed prin to print

print_first_and_last(sentence) # changed irst to first

print_first_and_last_sorted(sentence) # Removed white space, changed "a" to "and" and "senance" to "sentance"
