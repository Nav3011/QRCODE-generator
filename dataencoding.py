from constants import ERROR_LEVELS, MODE_INDICATOR, CAPACITIES, ALPHA_NUMERIC_MAPPING, CAPACITIES2

print(CAPACITIES2[8])
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


version, character_count_value = findVersion(character_count, error_level)
print("QR version => ", version)
mode = MODE_INDICATOR["alpha"]
character_count_indicator = encodeToBinary(character_count_value, 9)
print("mode and character count =>  ", mode, character_count_indicator)

text_pairs = []
alpha_summation_text_pairs = []
initial_position = 0
while initial_position < len(text):
    text_pairs.append(''.join(text[initial_position: initial_position + 2]))
    initial_position += 2
print("Text in pairs => ", text_pairs)

for i in text_pairs:
    # print(i[0], i[1])
    if (len(i) == 1):
        alpha_summation_text_pairs.append(ALPHA_NUMERIC_MAPPING[i[0]])
    else:
        alpha_summation_text_pairs.append(
            ALPHA_NUMERIC_MAPPING[i[0]] * 45 + ALPHA_NUMERIC_MAPPING[i[1]])

print("Alpha numeric summation => ", alpha_summation_text_pairs)
text_pairs_binary = []
if (len(text) % 2 == 0):
    for i in alpha_summation_text_pairs:
        text_pairs_binary.append(encodeToBinary(i, 11))
else:
    alpha_summation_text_pairs_last = alpha_summation_text_pairs[len(
        alpha_summation_text_pairs) - 1]
    alpha_summation_text_pairs = alpha_summation_text_pairs[0: len(
        alpha_summation_text_pairs) - 1]
    for i in alpha_summation_text_pairs:
        text_pairs_binary.append(encodeToBinary(i, 11))
    text_pairs_binary.append(encodeToBinary(
        alpha_summation_text_pairs_last, 6))
    # text_pairs_binary.append(encodeToBinary(i, 6))

print("Binary => ", text_pairs_binary)
final_text_binary = ''.join(text_pairs_binary)

# For the above QR code with version 1 and error level Q, we require 13 data code words
# (TABLE: Error Correction Code Words and Block Information)
total_data_codewords = 13
total_bits_required = total_data_codewords * 8
bit_string = mode + character_count_indicator + final_text_binary
bit_string_length = len(bit_string)
print("Bit string length 1 => ", bit_string_length)

terminator = ""
if (bit_string_length < total_bits_required):
    diff_l = total_bits_required - bit_string_length
    if (diff_l > 4):
        terminator = "0000"
    else:
        terminator = "0" * (4 - diff_l)

print("Terminator => ", terminator)
bit_string += terminator
final_padding_required_count = (8 - len(bit_string) % 8)
final_padding_required = "0" * final_padding_required_count
bit_string += final_padding_required
print("Bit string length 2 => ", len(bit_string))
ultimate_padding = total_bits_required - len(bit_string)
ultimate_padding = int(ultimate_padding / 8)

# 11101100 00010001 to be added 3 times one after the other
times = int(ultimate_padding / 2)
remaining = ultimate_padding % 2
ultimate_padding_value_times = "1110110000010001" * times
ultimate_padding_value_remaining = "11101100" * remaining
bit_string += ultimate_padding_value_times + ultimate_padding_value_remaining


print("FINAL ===>   ", bit_string)
