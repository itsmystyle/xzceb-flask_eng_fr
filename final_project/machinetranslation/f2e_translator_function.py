from translator import language_translator


def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText, model_id="fr-en"
    ).get_result()
    englishText = translation["translations"][0]["translation"]
    return englishText
