"""Translation methods"""

from deep_translator import MyMemoryTranslator

#Method take in english text and outputs french translated text
def english_to_french(english_text):
    """Use MyMemoryTranslator API to convert english text to french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

#Method takes in french text and outputs english translated text
def french_to_english(french_text):
    """Use MyMemoryTranslator API to convert french text to english"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
