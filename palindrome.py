def clean_text(text):
    text = text.lower()
    cleaned_text = ""
    for s in text:
       if s.isalnum():
           cleaned_text += s
       
    return cleaned_text

def is_palindrome(text):
    cleaned_text = clean_text(text)
    return cleaned_text == cleaned_text[::-1]



assert is_palindrome("kajak") == True
assert is_palindrome("Kajak") == True
assert is_palindrome("czekolada") == False
assert is_palindrome("12345654321") == True
assert is_palindrome("kobyła ma mały bok") == True
assert is_palindrome("Kobyła ma Mały bok!") == True
assert is_palindrome("Dobrze że jest przerwa") == False















      





















































