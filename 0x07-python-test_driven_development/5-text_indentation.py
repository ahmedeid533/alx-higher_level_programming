#!/usr/bin/python3
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
        stR = stR.replace('\n ', '\n@')
        stR = stR.split("@")
        for i in stR:
            print(i.strip(" "),end="")
