import string
from collections import Counter

# Standard English letter frequency (from most to least frequent)
ENGLISH_FREQ_ORDER = 'etaoinshrdlcumwfgypbvkjxqz'

def clean_text(text):
    """Remove non-alphabetical characters and convert to lowercase"""
    return ''.join(filter(str.isalpha, text.lower()))

def get_letter_frequency_order(text):
    """Returns the letter frequency order from most common to least common in the text"""
    freq_counts = Counter(clean_text(text))
    sorted_letters = [item[0] for item in freq_counts.most_common()]
    return sorted_letters

def substitute_text(text, substitution_map, remove_spaces=False, remove_punctuation=False):
    """Substitute letters in text using the provided substitution map"""
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

def format_ciphertext(ciphertext, chunk_size=5):
    """Format ciphertext into chunks of a specified size"""
    clean = ''.join(filter(str.isalpha, ciphertext.upper()))
    return ' '.join([clean[i:i+chunk_size] for i in range(0, len(clean), chunk_size)])

def perform_frequency_analysis(ciphertext):
    """Perform frequency analysis on ciphertext"""
    return get_letter_frequency_order(ciphertext)

def create_substitution_map_from_frequencies(cipher_order):
    """Create a substitution map based on letter frequency"""
    return {cipher: plain for cipher, plain in zip(cipher_order, ENGLISH_FREQ_ORDER)}

def manual_adjustment(substitution_map):
    """Manually adjust the substitution map if needed based on knowledge of the language"""
    # Here we manually adjust some common mappings (you can customize this part)
    # For example, if you know that 'z' in ciphertext is likely to map to 't' in plaintext, you can adjust:
    # Example manual adjustment (for short texts, this is helpful):
    substitution_map['z'] = 't'  # Adjust this if you know 'z' is 't' in the text
    substitution_map['q'] = 'e'  # Adjust similarly for other letters
    return substitution_map

def decrypt(ciphertext):
    """Decrypt the ciphertext using frequency analysis and manual adjustments"""
    # Step 1: Perform frequency analysis
    cipher_order = perform_frequency_analysis(ciphertext)

    # Step 2: Create a substitution map based on the frequency order
    substitution_map = create_substitution_map_from_frequencies(cipher_order)

    # Step 3: Manually adjust the map (if needed for small ciphertexts)
    substitution_map = manual_adjustment(substitution_map)

    # Step 4: Decrypt the ciphertext using the final substitution map
    decrypted_text = substitute_text(ciphertext, substitution_map)
    return decrypted_text

# Example usage
if __name__ == "__main__":
    # Example ciphertext (This should be obtained from the encryption script)
    ciphertext = "TIHNEE ENO EHE HUGA EHHUB BUOTN UOLME CAVMC CCHIW IUNIA TUTMU"
    
    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext)

    print("\nCiphertext: ", ciphertext)
    print("Decrypted:  ", decrypted_text)
