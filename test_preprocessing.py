from preprocessing import tokenize_and_clean

sample_texts = [
    "I love this product! It's amazing. 😍 Visit http://example.com",
    "This is the worst experience ever!! #disappointed",
    "Nothing special, just an average service.",
    "Check out our new website at https://brand.com #launch"
]

for i, text in enumerate(sample_texts, 1):
    print(f"\nSample {i}:")
    print("Original:", text)
    print("Processed:", tokenize_and_clean(text))
