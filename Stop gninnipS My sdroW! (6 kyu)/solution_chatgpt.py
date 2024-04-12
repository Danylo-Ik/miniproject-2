def spin_words(sentence):
    words = sentence.split()
    spun_sentence = []
    for word in words:
        if len(word) >= 5:
            spun_word = word[::-1]  # Reverse the word
            spun_sentence.append(spun_word)
        else:
            spun_sentence.append(word)
    return ' '.join(spun_sentence)