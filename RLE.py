
def rle_encode(data):
    if data == "":
        return ""
    encoded = []
    length = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            length += 1
        else:
            encoded.extend([str(length), str(data[i-1])])
            length = 1
    encoded.extend([str(length), str(data[-1])])
    return "".join(encoded)

def rle_decode(data):
    if data == "":
        return ""
    decoded = []
    length = 0
    for ch in data:
        if ch.isnumeric():
            length = 10*length + int(ch)
        else:
            decoded.append(length * ch)
            length = 0
    return "".join(decoded)

input_str = input("Please enter the data:  ")
print("Original String is: ", input_str)

encoded_str = rle_encode(input_str)
print("Encoded String is: ", encoded_str )
print("Decoded String is: ", rle_decode(encoded_str))
