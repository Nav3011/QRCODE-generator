from galoisField import galoisFieldValueInverse, galoisFieldValue
# Here the message polynomial is divided by generator polynomial to get the error correction words

# gen_poly = x10 + α251x9 + α67x8 + α46x7 + α61x6 + α118x5 + α70x4 + α64x3 + α94x2 + α32x + α45
gen_poly = {10: 0, 9: 251, 8: 67, 7: 46, 6: 61,
            5: 118, 4: 70, 3: 64, 2: 94, 1: 32, 0: 45}
message_poly = {15: 32, 14: 91, 13: 11, 12: 120, 11: 209, 10: 114, 9: 220,
                8: 77, 7: 67, 6: 64, 5: 236, 4: 17, 3: 236, 2: 17, 1: 236, 0: 17}
error_correction_count = 10

# =========================================================================================================


# # 1. Mulitply the message polynomial with error correction count power i.e. here 10

message_poly_power = {}
for x_power, alpha_power in message_poly.items():
    message_poly_power[x_power+error_correction_count] = alpha_power
# print("MSG POLY 1 : ", message_poly_power)

# # 2. Normalizing the powers b/w generator and message polynomial
# difference = list(message_poly_power.items())[0][0] - list(gen_poly.items())[0][0]

# # 3. multiply the generator polynomial with this power to notmalize powers of x
# generator_poly_power = {}
# for x_power, alpha_power in gen_poly.items():
#     generator_poly_power[x_power + difference] = alpha_power
# print("GEN POLY 1 : ", generator_poly_power)

# # 4. Make the coefficients equal for the first term ==> Here 32
# alpha_0_power = galoisFieldValueInverse(list(message_poly_power.items())[0][1])

# # 5. add this to the generator polynomial alpha powers
# # if alpha power exceeding 255, do mod 255
# for x_power, alpha_power in generator_poly_power.items():
#     generator_poly_power[x_power] = alpha_power + alpha_0_power if alpha_power + alpha_0_power < 255 else (alpha_power + alpha_0_power) % 255
# print("GEN POLY 2 : ", generator_poly_power)

# # 6. Convert the generator polynomial to numeric values.
# # Bring to the length of message polynomial - replace the other values with 0
# for x_power, alpha_power in message_poly_power.items():
#     # print("Test => ", x_power)
#     generator_poly_power[x_power] = 0 if x_power not in generator_poly_power else galoisFieldValue(generator_poly_power[x_power])
# print("GEN POLY 3 : ", generator_poly_power)

# # 7. Perform XOR for the coefficients
# for x, alpha in message_poly_power.items():
#     # print("Test ==> ", x, alpha, message_poly_power[x], generator_poly_power[x], message_poly_power[x] ^ generator_poly_power[x])
#     message_poly_power[x] = message_poly_power[x] ^ generator_poly_power[x]
# print("MSG POLY 2 : ", message_poly_power)
# # for x, alpha in message_poly_power.items():
# #     if message_poly_power[x] == 0:
# #         del message_poly_power[x]
# message_poly_power = dict(list(message_poly_power.items())[1:])
# generator_poly_power = dict(list(generator_poly_power.items())[1:])
# print("MSG POLY 3 : ", message_poly_power)
# print("GEN POLY 4 : ", generator_poly_power)


# ===========================================================================================================

loop_count = len(message_poly.items())
print(loop_count)
# message_poly_power = {}
for i in range(loop_count):
    # for x_power, alpha_power in message_poly.items():
    #     message_poly_power[x_power+error_correction_count] = alpha_power
    # print("MSG POLY 1 : ", message_poly_power)
    difference = list(message_poly_power.items())[
        0][0] - list(gen_poly.items())[0][0]
    generator_poly_power = {}
    for x_power, alpha_power in gen_poly.items():
        generator_poly_power[x_power + difference] = alpha_power
    print("GEN POLY 1 : ", generator_poly_power)
    alpha_0_power = galoisFieldValueInverse(
        list(message_poly_power.items())[0][1])
    for x_power, alpha_power in generator_poly_power.items():
        generator_poly_power[x_power] = alpha_power + alpha_0_power if alpha_power + \
            alpha_0_power < 255 else (alpha_power + alpha_0_power) % 255
    print("GEN POLY 2 : ", generator_poly_power)
    for x_power, alpha_power in generator_poly_power.items():
        generator_poly_power[x_power] = galoisFieldValue(
            generator_poly_power[x_power])
    print("GEN POLY 3 : ", generator_poly_power)
    for x, alpha in generator_poly_power.items():
        # print("msg => ", x, generator_poly_power[x])
        message_poly_power[x] = (message_poly_power[x] if x in message_poly_power.keys(
        ) else 0) ^ generator_poly_power[x]
    print("MSG POLY 2 : ", message_poly_power)
    message_poly_power = dict(list(message_poly_power.items())[1:])
    generator_poly_power = dict(list(generator_poly_power.items())[1:])
    print("MSG POLY 3 : ", message_poly_power)
    print("GEN POLY 4 : ", generator_poly_power)
    print("=======================================================================================================================================")
