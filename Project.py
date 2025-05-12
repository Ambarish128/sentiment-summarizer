import nltk
import transformers
import numpy as np

try:
    nltk.download('punkt_tab')
    print('NLTK data downloaded Successfully.')
except Exception as e:
    print(f'Error downloading NLTK Data: {e}')

print(f"Transformers version: {transformers.__version__}")
print(f"NumPy version: {np.__version__}")
#Test sentence tokenization with a sample text
sample_text = """The new product is amazing. Some users reported bugs. Overall, feedback is positive.
"""
sentences = nltk.sent_tokenize(sample_text)
print("\nSample text sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

