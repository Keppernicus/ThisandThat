"""
Encoding and Decoding using the atbash cipher method.
This just inverts the position of a letter with it's inverse
in the alphabet, then breaks the message into 5 character chunks.
For example: "I like to move it" encodes to "rorpv glnle vrg"
Punctuation is dropped and digits remain intact. 

"""

def encode(plain_text):
    """
    Encoding the enciphered text and smashing it together
    since we can't deduce from the encipherment which
    groups form cohesive words.
    
    """
    sumnum = ord("a") + ord("z")
    answer = "".join(
        [
            chr(sumnum - ord(letter)) if letter.isalpha() else letter
            for letter in plain_text.lower()
            if letter.isalnum()
        ]
    )
    answer = (
        " ".join(answer[i : i + 5] for i in range(0, len(answer), 5))
        if len(answer) > 5
        else answer
    )
    return answer

def decode(plain_text):
    """
    Decoding the enciphered text and smashing it together
    since we can't deduce from the encipherment which
    groups form cohesive words.
    
    """
    sumnum = ord("a") + ord("z")
    answer = "".join(
        [
            chr(sumnum - ord(letter)) if letter.isalpha() else letter
            for letter in plain_text.lower()
            if letter.isalnum()
        ]
    )
    return answer

print(encode('Fol,low 12 yo.ur 34 heart.'))
print(decode('ulool d12bl fi34s vzig'))
