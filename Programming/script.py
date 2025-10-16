#input_s is input string, input_k is input key, input_e is encoded string


def encode(input_s, input_k):
    encoded = ""
    for char in input_s:
        encoded += chr((ord(char) + input_k) % 256)  # wrap around ASCII table
    return encoded

def decode(input_e, input_k):
    decoded = ""
    for char in input_e:
        decoded += chr((ord(char) - input_k) % 256)
    return decoded


def main():
    print("encoder/decoder")
    choice = input("e for encode, d for decode: ").strip().upper()

    if choice == 'E':
        input_s = input("text to be encoded: ")
        input_k = int(input("key: "))
        encoded = encode(input_s, input_k)
        print(f"\noutput: {encoded}")
        with open("outfile.txt", "w") as f:
            f.write(encoded)
        print("output saved to 'outfile.txt'.")

    elif choice == 'D':
        input_e = input("text to be decoded: ")
        input_k = int(input("key: "))
        decoded = decode(input_e, input_k)
        print(f"\nouput: {decoded}")
    else:
        print("please choose e or d")


if __name__ == "__main__":
    main()
