def caesar_cypher(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZABCDEFGHIJKLMONPQRSTUVWXYZ"
    decoded_string = []
    all_decoded_strings = []
    i=0
    while i < 26:
        for letter in string:
            if alphabet.find(letter) == -1:
                decoded_string.append(letter)
            else:
                decoded_string.append(alphabet[alphabet.find(letter)+i])
        all_decoded_strings.append("".join(decoded_string))
        decoded_string = []
        i+=1
    return "\n".join(all_decoded_strings)
print(caesar_cypher("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."))