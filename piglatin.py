"""
A little pig latin translator

"""
def translate(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    special = ('xr', 'yt')
    def rules(word):
        if word.startswith(vowels + special):
            return word + 'ay'
        elif 'qu' in word[:3]:
            return word[word.index('qu') + 2:] + word[:word.index('qu') + 2] + 'ay'
        else:
            for ltr, letter in enumerate(word):
                if letter in vowels:
                    return word[ltr:] + word[:ltr] + 'ay'
            for ltr, letter in enumerate(word):
                if letter == 'y':
                    return word[ltr:] + word[:ltr] + 'ay'
        return word

    words = text.split()
    if len(words) > 1:
        processed_text = ' '.join(rules(word) for word in words)
        return processed_text
    else:
        return rules(words[0])
