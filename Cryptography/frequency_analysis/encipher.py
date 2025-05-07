import string
from collections import Counter
import json

ENGLISH_FREQ_ORDER = 'etaoinshrdlcumwfgypbvkjxqz'

def banner():
    print("""
CRYTOGRAPHY FREQUENCY ANALYSIS ENCIPHERING

Author: Ps7ch0
...........................................
""")

def clean_text(text):
    return ''.join(filter(str.isalpha, text.lower()))

def get_letter_frequency_order(text):
    freq_counts = Counter(clean_text(text))
    sorted_letters = [item[0] for item in freq_counts.most_common()]
    return sorted_letters

def create_substitution_map(from_order, to_order):
    return {f: t for f, t in zip(from_order, to_order)}

def substitute_text(text, substitution_map, remove_spaces=False, remove_punctuation=False):
    result = ''
    for char in text:
        if char in string.whitespace and remove_spaces:
            continue
        if char in string.punctuation and remove_punctuation:
            continue

        lower_char = char.lower()
        if lower_char in substitution_map:
            new_char = substitution_map[lower_char]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def format_ciphertext(ciphertext, chunk_size):
    clean = ''.join(filter(str.isalpha, ciphertext.upper()))
    return ' '.join([clean[i:i+chunk_size] for i in range(0, len(clean), chunk_size)])

def encrypt(plaintext, chunk_size, format_chunks=True, show_mapping=True):
    plain_order = get_letter_frequency_order(plaintext)
    substitution_map = create_substitution_map(plain_order, ENGLISH_FREQ_ORDER)

    if show_mapping:
        print("\nSubstitution Mapping (Plain → Cipher):")
        for plain, cipher in sorted(substitution_map.items()):
            print(f"  {plain.upper()} → {cipher.upper()}")

    raw_cipher = substitute_text(plaintext, substitution_map, remove_spaces=True, remove_punctuation=True)
    formatted_cipher = format_ciphertext(raw_cipher, chunk_size) if format_chunks else raw_cipher

    return formatted_cipher

if __name__ == "__main__":
    banner()
    plaintext = input("""ENTER THE PLAIN TEXT:
""")
    print(" ")
    chunk_size = int(input("ENTER THE SIZE OF CHUNK: "))
    ciphertext = encrypt(plaintext, chunk_size, format_chunks=True, show_mapping=True)
    print("\nCiphertext:", ciphertext)
