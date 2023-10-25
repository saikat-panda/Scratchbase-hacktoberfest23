# Function to convert decimal to binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2
    return binary

# Function to perform bitwise addition (OR operation)


def bitwise_addition(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ""
    for i in range(max_len):
        if a[i] == '1' or b[i] == '1':
            result += '1'
        else:
            result += '0'
    return result


# Convert numbers to binary
num1 = int(input("1st Number: "))
num2 = int(input("2nd Number: "))

binary_num1 = decimal_to_binary(num1)
binary_num2 = decimal_to_binary(num2)

# Perform bitwise addition
result_binary = bitwise_addition(binary_num1, binary_num2)

# Convert the result back to decimal
result_decimal = int(result_binary, 2)

print("Binary Addition:", result_binary)
print("Decimal Result:", result_decimal)
