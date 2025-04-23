# Print the prompt
print("Enter a sentence ending with a period ('.'):")

# Initialize counters
char_count = 0    # To count total characters
word_count = 0    # To count total words
vowel_count = 0   # To count total vowels

# Initialize the sentence string
sentence = ""

# Read characters one by one
while True:
    ch = input("Enter next character: ")

    # Validate single character input
    if len(ch) != 1:
        print("Please enter only one character at a time.")
        continue

    # Add character to sentence
    sentence += ch
    char_count += 1  # Count this character

    # Check for vowel (both lowercase and uppercase)
    if ch.lower() in 'aeiou':
        vowel_count += 1

    # End when period is entered
    if ch == '.':
        break

# Count words based on spaces
# Remove the final period before counting words
words = sentence[:-1].split(' ')
word_count = len(words)

# Display results
print("\n--- Analysis Complete ---")
print("Sentence:", sentence)
print(f"Total number of characters: {char_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of vowels: {vowel_count}")
