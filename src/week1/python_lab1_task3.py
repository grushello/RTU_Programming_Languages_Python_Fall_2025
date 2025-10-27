"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""


def analyze_sentence(text):
    length = len(text)
    wcount = len(text.split())
    contPython = "python" in text.lower()
    return length, wcount, contPython


if __name__ == "__main__":
    sentence = input("Enter your sentence, please! ")
    length, wcount, contPython = analyze_sentence(sentence)
    print("Length: ", length)
    print("Word count: ", wcount)
    print("Contains 'python':", contPython)
    pass
