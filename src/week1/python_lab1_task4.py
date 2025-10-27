"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""


def count_characters(text):
    return len(text.replace(" ", ""))


def count_words(text):
    return len(text.split())


def extract_numbers(text):
    nums = []
    for word in text.split():
        if word.isdigit():
            nums.append(int(word))
    return nums


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    nums = extract_numbers(text)
    total = sum(nums)
    if len(nums) == 0:
        avg = 0
    else:
        avg = total / len(nums)
    return total, avg


if __name__ == "__main__":
    text = input("Please, enter your text\n")
    total, avg = analyze_text(text)
    word_count = count_words(text)
    chars = count_characters(text)

    print("Character count: ", chars)
    print("Word count: ", word_count)
    print("Sum of all numbers: ", total)
    print("Average of numbers: ", avg)
    pass
