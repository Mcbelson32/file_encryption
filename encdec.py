import os

def encrypt_file(file_path, encryption_key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = bytearray()
    for i, byte in enumerate(file_data):
        encrypted_data.append(byte ^ ord(encryption_key[i % len(encryption_key)]))

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, encryption_key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = bytearray()
    for i, byte in enumerate(encrypted_data):
        decrypted_data.append(byte ^ ord(encryption_key[i % len(encryption_key)]))

    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    print("Files in the current directory:")
    for i, file in enumerate(os.listdir()):
        print(f"\t{i+1}. {file}")

    file_choice = int(input("Enter the number of the file to encrypt or decrypt: ")) - 1
    file_path = os.listdir()[file_choice]

    operation = input("Do you want to (E)ncrypt or (D)ecrypt? ")

    if operation.upper() == "E":
        encryption_key = input("Enter the encryption key: ")
        encrypt_file(file_path, encryption_key)
        print("File encrypted successfully! \n\t Password: " + encryption_key)
    elif operation.upper() == "D":
        encryption_key = input("Enter the decryption key: ")
        decrypt_file(file_path, encryption_key)
        print("File decrypted successfully!")
    else:
        print("Invalid operation. Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()