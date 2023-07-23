from galoisField import galoisFieldValue, galoisFieldValueInverse, galoisSum

# for 2 error correction words
# (x1.α0 - x0.α0).(x1.α0 - x0.α1)
poly1 = {1 : 0 , 0 : 0}
poly2 = {1 : 0 , 0 : 1}

def polynomialMultiplication(poly1, poly2):
    result = {}
    for x_pow1, α_pow1 in poly1.items():
        for x_pow2, α_pow2 in poly2.items():
            x_pow_sum = x_pow1 + x_pow2
            α_sum = α_pow1 + α_pow2
            if x_pow_sum in result:
                result[x_pow_sum] = galoisSum(result[x_pow_sum], galoisFieldValue(α_sum))
            else:
                result[x_pow_sum] = galoisFieldValue(α_sum)

    # reversing to α format
    for x_pow, α_value in result.items():
        result[x_pow] = galoisFieldValueInverse(α_value)
    # print(result)
    return result

# for 3 error correction code words

poly3 = polynomialMultiplication(poly1, poly2)
# (x1.α0 - x0.α2)
poly4 = polynomialMultiplication(poly3, {1: 0, 0: 2})
# print(poly4)
# 
# print(galoisFieldValueInverse(galoisFieldValue(257))) 
