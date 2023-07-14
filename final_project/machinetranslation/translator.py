"""Translation methods"""

from deep_translator import MyMemoryTranslator

#Method take in english text and outputs french translated text
def englishToFrench(englishText):
    
    """Use MyMemoryTranslator API to convert english text to french"""
    frenchText = MyMemoryTranslator(source='auto', target='french').translate(englishText)
    
    return frenchText

#Method takes in french text and outputs english translated text
def frenchToEnglish(frenchText):

    """Use MyMemoryTranslator API to convert french text to english"""
    englishText = MyMemoryTranslator(source='auto', target='english').translate(frenchText)
