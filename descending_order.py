''' Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''


def descending_order(num):
    array = [int(i) for i in str(num)]
    array.sort(reverse=True)
    result =''.join([str(c) for c in array])
    return int(result)