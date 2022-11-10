# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_original.txt', 'w') as data:
    data.write("AuuBBBCCCCCCcccccCCCCCCCCCA")

with open('file_original.txt', 'r') as data:
    original_string = data.read()

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j + 1]): 
                count += 1
                j += 1
            else: 
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decode_message(our_message):
    decoded_string = ""
    i = 0
    j = 0
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        for j in range(run_count):
            decoded_string = decoded_string + run_word
            j += 1
        i += 2
    return decoded_string


with open('file_encode.txt', 'w') as file:
    encoded_message = encode_message(original_string)
    file.write(encoded_message)

with open('file_encode.txt', 'r') as file:
    encoded_message = file.read()

with open('file_decode.txt', 'w') as file:
    decoded_message = decode_message(encoded_message)
    file.write(decoded_message)

    print("Исходная строка: [" + original_string + "]")
    print("Закодированная строка: [" + encoded_message +"]")
    print("Восстановленная строка: [" + decoded_message +"]")
    print(f'Коэффициент сжатия: {round(len(original_string) / len(encoded_message), 1)}')




