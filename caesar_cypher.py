alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZABCDEFGHIJKLMONPQRSTUVWXYZ"
coded_msg = "Drsc sc wi vkcd wocckqo. Oy xyd dbi dy myxdkmd wo. Xfob."
def caesar_cypher(string, offset):
    decoded_string = []
    for letter in string:
        if alphabet.find(letter) == -1:
            decoded_string.append(letter)
        else:
            decoded_string.append(alphabet[alphabet.find(letter)+offset])
    return "".join(decoded_string)

print(caesar_cypher("Jxyi yi co bqij cuiiqwu. Te dej jho je sedjqsj cu. Dluh.", 10))

