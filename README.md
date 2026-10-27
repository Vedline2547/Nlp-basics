# NLP Basics: Text Preprocessing and Tokenization

## 📌 Project Overview

This project explores fundamental Natural Language Processing (NLP) techniques using Python. It demonstrates how raw text can be cleaned, normalized, and transformed into structured text representations for further analysis and machine learning applications.

The project implements essential NLP preprocessing methods, including case folding, special character removal, contraction expansion, word and sentence tokenization, stop-word removal, and n-gram generation.

It serves as a practical introduction to text preprocessing and the foundational techniques used in NLP pipelines.

## 🎯 Objectives

- Understand fundamental text preprocessing techniques.
- Normalize text using lowercase conversion and case folding.
- Remove unwanted special characters using regular expressions.
- Expand English contractions to their full forms.
- Perform word and sentence tokenization.
- Remove common English stop words.
- Generate unigrams, bigrams, and trigrams.
- Explore Python libraries commonly used in NLP applications.

## 🛠️ Technologies and Libraries

- **Python** — Core programming language.
- **NLTK** — Tokenization, stop-word removal, and n-gram generation.
- **spaCy** — Text processing and linguistic analysis.
- **Regular Expressions (`re`)** — Pattern matching and special character removal.
- **contractions** — Expansion of common English contractions.

## 📚 Features and Implementation

### 1. Case Folding
Converts text into a consistent case representation using Python's `lower()` and `casefold()` methods.

Example:

Input:
```text
Hello, And Welcome to My World
```

Output:
```text
hello, and welcome to my world
```

### 2. Special Character Removal
Uses regular expressions and Python string operations to remove unwanted characters from text.

Example:

Input:
```text
hello how are & you
```

Output:
```text
hello how are you
```

### 3. Text Cleaning with spaCy
Implements a custom text-cleaning function that removes non-alphabetic characters, processes the cleaned text using spaCy, and returns the resulting tokens as a string.

### 4. Contraction Expansion
Expands common English contractions into their full forms using the `contractions` library and a custom regular-expression-based function.

Example:

Input:
```text
I can't believe it's already raining
```

Output:
```text
I cannot believe it is already raining
```

### 5. Word and Sentence Tokenization
Uses NLTK to split text into individual word tokens and sentences.

This technique is a foundational step in many NLP workflows.

### 6. Stop-Word Removal
Uses NLTK's English stop-word list to filter common words from tokenized text.

This demonstrates how text can be simplified before selected NLP tasks, although stop-word removal is not appropriate for every application.

### 7. N-gram Generation
Generates contiguous sequences of tokens to explore relationships between neighboring words.

The project implements:

- **Unigrams:** Sequences of one token.
- **Bigrams:** Sequences of two consecutive tokens.
- **Trigrams:** Sequences of three consecutive tokens.

These representations are useful for exploring word patterns and preparing text for certain language modelling and text classification tasks.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version.
- Basic familiarity with Python.
- Git installed on your system.

### 1. Clone the repository

```bash
git clone https://github.com/Vedline2547/Nlp-basics.git
```

### 2. Navigate to the project directory

```bash
cd Nlp-basics
```

### 3. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the required libraries

```bash
python -m pip install spacy nltk contractions
```

### 5. Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

### 6. Download the required NLTK resources

Run the following Python commands:

```python
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

### 7. Run the project

Execute the main Python script:

```bash
python main.py
```

Replace `main.py` with your script's actual filename if necessary.

## 📂 Project Structure

```text
Nlp-basics/
│
├── main.py
├── README.md
└── .gitignore
```

*Note: This is a suggested structure. Adjust the filenames to match your repository.*

## 💡 Learning Outcomes

Through this project, I explored:

- Text normalization and cleaning.
- Regular expressions for text manipulation.
- The differences between case folding and lowercase conversion.
- Word and sentence tokenization.
- Contraction expansion.
- Stop-word filtering.
- N-gram representations of text.
- Practical applications of NLTK and spaCy in NLP workflows.

## 🚀 Future Improvements

Potential extensions include:

- Lemmatization and stemming.
- Part-of-speech tagging.
- Named Entity Recognition (NER).
- Sentiment analysis using machine learning.
- Text vectorization using Bag of Words and TF-IDF.
- Building a reusable NLP preprocessing pipeline.
- Comparing the effects of different preprocessing strategies on model performance.

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | Machine Learning Enthusiast | Python Developer

GitHub: [Vedline2547](https://github.com/Vedline2547)

LinkedIn: [Vedline Ochieng](https://www.linkedin.com/in/vedline-ochieng-025146290/)

## 📄 License

This project is intended for educational and learning purposes. A license can be added to specify the terms under which others may use, modify, and distribute the code.
