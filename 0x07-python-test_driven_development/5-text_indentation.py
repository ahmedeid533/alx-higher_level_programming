#!/usr/bin/python3g
"""text example"""

def text_indentation(text):
    """text tokens"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    text = text.replace('.', '.\n\n@')
    text = text.replace('?', '?\n\n@')
    text = text.replace(':', ':\n\n@')
    text = text.split("@")
    for stR in text:
        print(stR.strip(" "),end="")
