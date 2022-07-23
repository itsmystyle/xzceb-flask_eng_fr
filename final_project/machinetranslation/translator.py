"""
    Translator
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(f"{apikey}")
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)
language_translator.set_service_url(f"{url}")


def english_to_french(english_text):
    """
        This function translate english to french
    """
    if english_text == '' or english_text is None:
        return ''
    translation = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    return translation["translations"][0].get("translation")


def french_to_english(french_text):
    """
        This function translate french to english
    """
    if french_text == '' or french_text is None:
        return ''
    translation = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    return translation["translations"][0].get("translation")
