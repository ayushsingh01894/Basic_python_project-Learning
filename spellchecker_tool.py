from spellchecker import SpellChecker
spell = SpellChecker()
text = input("Enter a sentence: ")
words = text.split()
misspelled = spell.unknown(words)

if not misspelled:
    print("No spelling errors found!")
else:
    print("\n Misspelled words and suggestions:")
    for word in misspelled:
        correction = spell.correction(word)
        suggestions = spell.candidates(word)
        print(f"  • {word} → Suggested: {correction} (alternatives: {', '.join(suggestions)})")

    
    corrected_text = ' '.join([spell.correction(w) if w in misspelled else w for w in words])
    print("\nCorrected sentence:")
    print(corrected_text)
