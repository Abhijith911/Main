# (b) Program to Count Words in a Sentence

print("\nProgram to Count Words in a Sentence\n")

sentence = input ("Enter a sentence: ")

words = sentence.split()

wordCount = len(words)

print (f"The number of words in the sentence is: {wordCount}")