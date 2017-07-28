def main():

    layers = int(raw_input("Enter the number of layers: "))
    plain_text = raw_input("Enter the plain text: ")
    if layers<10:
        cipher_text = encrypt(layers, plain_text)

        print("Encrypted text: " + cipher_text)
    else:
        print"enter layers less than 10"

def encrypt(layers, plain_text):
    plain_text = plain_text.replace(" ", "")

    plain_text = plain_text.upper()
    rail = [""] * layers

    layer = 0
    for character in plain_text:
        rail[layer] += character

        if layer >= layers - 1:
            layer = 0
        else:

            layer += 1

    cipher = "".join(rail)

    return cipher
if __name__ == '__main__':
    main()

