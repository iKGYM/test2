import os
from google.cloud import texttospeech

import io
import streamlit as st
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'lunar-box-356903-d0e739cfd10d.json'

def synthesize_speech(text, lang, gender, pit, sprate):
    """Synthesizes speech from the input string of text or ssml.
    Make sure to be working in a virtual environment.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    gender_type = {
        'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }

    lang_code = {
        '英語': 'en-US',
        '日本語': 'ja-JP',
        '中国語(簡体字)': '',
        '中国語(繁体字)': 'zh-TW'


    }



    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender])

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=pit,
        speaking_rate=sprate
    )


    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response


lang = '日本語'
gender = 'defalut'
text = "テスト"
pit = -6
sprate=1
    
response = synthesize_speech('日本語', 'male', '日本語', -6, 1)
   # response = synthesize_speech('日本語', 'defalut', '日本語', -6, 1)
    
    #from IPython.display import Audio
    #Audio(response.audio_content)

 