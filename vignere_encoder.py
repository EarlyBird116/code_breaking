def vigenere_encoder(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZABCDEFGHIJKLMONPQRSTUVWXYZ"
    decoded_string = []
    key_index = []
    for letter in key:
        key_index.append(alphabet.find(letter))
            
    key_index_count = 0

    for letter in range(0,len(string)):
        if alphabet.find(string[letter]) == -1:
            decoded_string.append(string[letter])
        else:
            decoded_string.append(alphabet[alphabet.find(string[letter])+26-(key_index[key_index_count%len(key_index)])])
            key_index_count+=1
            
    return "".join(decoded_string)
print(vigenere_encoder("you were able to decode this? nice work! you are becoming quite the expert at crytography!", "friends"))