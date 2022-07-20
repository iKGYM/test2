import os
from google.cloud import texttospeech

import io
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

def synthesize_speech(text, lang, gender, pit, sprate):
    """Synthesizes speech from the input string of text or ssml.
    Make sure to be working in a virtual environment.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    gender_type = {
        #'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }

    lang_code = {
        '英語': 'en-US',
        '日本語': 'ja-JP'
    }    
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

# main
st.title('テキスト読み上げ君')

input_option = st.selectbox(
    '入力データの選択',
    ('直接入力', 'テキストファイル')
)
input_data = None

if input_option == '直接入力':
    input_data = st.text_area('こちらにテキストを入力してください。')
else:
    uploaded_file = st.file_uploader('テキストファイルをアップロードしてください。', ['txt'])    
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()

st.sidebar.write("""
## パラメーター設定
""")

st.sidebar.write("""
## 言語の指定
""")
lang = '日本語'
lang = st.sidebar.selectbox(
    '言語を選択してください。',
    ('日本語', '英語')
)

st.sidebar.write("""
## 性別の指定
""")
gender = 'neutral'
gender = st.sidebar.selectbox(
    '話者の性別を選択してください',
    ('male', 'female', 'neutral')
)

st.sidebar.write("""
## ピッチの指定
""")
pit = st.sidebar.slider(
    'ピッチを指定してください。', -20.0, 20.0, 0.0
)

st.sidebar.write("""
## スピーキングレイトの指定
""")
sprate = st.sidebar.slider(
    'スピーキングレイトを指定してください。', 0.25, 4.0, 1.0
)



if input_data is not None:
    st.write('入力データ')
    st.write(input_data)
    st.markdown('### 音声合成')
    st.write('こちらの文章で音声ファイルの生成を行いますか？')
    if st.button('開始'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_speech(input_data, lang, gender, pit, sprate)
        st.audio(response.audio_content)
        comment.write('完了しました')
else:
    st.error('テキストが入力されていません。')
