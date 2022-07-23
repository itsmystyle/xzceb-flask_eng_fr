from machinetranslation.translator import language_translator


def englishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText, model_id="en-fr"
    ).get_result()
    frenchText = translation["translations"][0]["translation"]
    return frenchText
