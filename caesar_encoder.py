alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZABCDEFGHIJKLMONPQRSTUVWXYZ"
coded_msg = "This is my last message. Do not try to contact me. Over."
def caesar_encoder(msg, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZABCDEFGHIJKLMONPQRSTUVWXYZ"
    encoded_string = []
    for letter in msg:
        if alphabet.find(letter) == -1:
            encoded_string.append(letter)
        else:
            encoded_string.append(alphabet[alphabet.find(letter)+26-offset])
    return "".join(encoded_string)

print(caesar_encoder(coded_msg, 10))