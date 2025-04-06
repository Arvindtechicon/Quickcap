from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    """Translates the summary into the desired language."""
    try:
        translation = GoogleTranslator(source="auto", target=target_language).translate(text)
        return translation
    except Exception as e:
        return str(e)