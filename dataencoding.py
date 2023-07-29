from constants import ERROR_LEVELS, MODE_INDICATOR, CAPACITIES, ALPHA_NUMERIC_MAPPING

# text = input("Write the text for QR code : ")
text = "HELLO WORLD"
# error_level = input("Select your error correction level (L M H Q) : ")
error_level = "Q"
print(text, error_level)
character_count = len(text)
print("Length => ", character_count)


# suitable version of qr code
def findVersion(textLength, error):
    # find all possible combinations of error level with different versions
    for i in range(40):
        versionWithError = str(i + 1) + error
        if int(CAPACITIES[versionWithError][0]) > textLength:
            return i + 1, int(CAPACITIES[versionWithError][1])


def encodeToBinary(value, length):
    binValue = ""
    while value > 0:
        a = value % 2
        binValue += str(a)
        value = int(value / 2)
    # print(binValue[::-1])
    binValue = binValue[::-1]
    # print("pre binary length => ", len(binValue), length)
    if len(binValue) < length:
        diff = length - len(binValue)
        padding = "0" * diff
        # print(padding)
        binValue = padding + binValue
    # print("length of binary => ", len(binValue))
    return binValue


version, character_count_indicator = findVersion(character_count, error_level)
print("QR version => ", version)
mode = MODE_INDICATOR["alpha"]
print("mode and character count =>  ", mode, encodeToBinary(11, 9))

text_pairs = []
alpha_summation_text_pairs = []
initial_position = 0
while initial_position < len(text):
    text_pairs.append(''.join(text[initial_position: initial_position + 2]))
    initial_position += 2
print("Text in pairs => ", text_pairs)

for i in text_pairs:
    # print(i[0], i[1])
    if(len(i) == 1):
        alpha_summation_text_pairs.append(ALPHA_NUMERIC_MAPPING[i[0]])
    else:
        alpha_summation_text_pairs.append(ALPHA_NUMERIC_MAPPING[i[0]] * 45 + ALPHA_NUMERIC_MAPPING[i[1]])

print("Alpha numeric summation => ", alpha_summation_text_pairs)
text_pairs_binary = []
if(len(text) % 2 == 0):
    for i in alpha_summation_text_pairs:
        text_pairs_binary.append(encodeToBinary(i, 11))
else:
    alpha_summation_text_pairs_last = alpha_summation_text_pairs[len(alpha_summation_text_pairs) - 1]
    alpha_summation_text_pairs = alpha_summation_text_pairs[0: len(alpha_summation_text_pairs) - 1]
    for i in alpha_summation_text_pairs:
        text_pairs_binary.append(encodeToBinary(i, 11))
    text_pairs_binary.append(encodeToBinary(alpha_summation_text_pairs_last, 6))
    # text_pairs_binary.append(encodeToBinary(i, 6))

    

print("Binary => ", text_pairs_binary)