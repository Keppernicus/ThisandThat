def encode(numbers):
    vlq_result = []
    for number in numbers:
        if number == 0:
            vlq_result.append(0x0)
            continue
        vlq_bytes = []
        while number >0:
            last_7_bits = number & 0b01111111
            vlq_bytes.insert(0, last_7_bits)
            number >>= 7

        for i in range(len(vlq_bytes) - 1):
            vlq_bytes[i] |= 0b10000000
        vlq_result.extend(vlq_bytes)
    return vlq_result

def decode(bytes_):
    decoded_numbers = []
    decoded_number = 0
    incomplete_sequence = True
    for byte in bytes_:
        decoded_number = (decoded_number << 7) | (byte & 0b01111111)
        if byte & 0b10000000 == 0:
            decoded_numbers.append(decoded_number)
            decoded_number = 0
            incomplete_sequence = False
    if incomplete_sequence:
        raise ValueError("incomplete sequence")
    return [decoded_number for decoded_number in decoded_numbers]
