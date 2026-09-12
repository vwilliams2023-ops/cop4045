def caesar_cipher(text, shift):
    """Encrypt text by shifting each letter by shift positions."""
    result = ""
    for char in text:
        if char.isalpha():
            # Get the base ('a' or 'A') depending on case
            base = ord('a') if char.islower() else ord('A')
            # Shift within 0-25 using modulo
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


def caesar_decipher(cyphertext, shift):
    """Decrypt by shifting in the opposite direction."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    """Count occurrences of each letter (case-insensitive)."""
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts


def main():
    text = ""
    shift = 0
    ciphertext = ""

    while True:
        print("\n1. Enter message")
        print("2. Enter shift")
        print("3. Encrypt")
        print("4. Letter frequency")
        print("5. Decrypt")
        print("6. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            text = input("Message: ")
        elif choice == "2":
            shift = int(input("Shift: "))
        elif choice == "3":
            ciphertext = caesar_cipher(text, shift)
            print("Encrypted:", ciphertext)
        elif choice == "4":
            print("Frequency:", letter_frequency(text))
        elif choice == "5":
            print("Decrypted:", caesar_decipher(ciphertext, shift))
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()