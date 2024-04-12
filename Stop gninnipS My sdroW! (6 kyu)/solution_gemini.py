def spin_words(sentence):
  """Reverses each word in a sentence while keeping punctuation intact.

  Args:
      sentence: The sentence to be processed.

  Returns:
      A new sentence with each word reversed.
  """
  words = sentence.split()
  reversed_words = []
  for word in words:
    if word.isalpha() and len(word) >= 5:
      reversed_words.append(word[::-1])
    else:
      reversed_words.append(word)
  return " ".join(reversed_words)
