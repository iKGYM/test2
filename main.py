import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write("２カラム")
# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラムです。')

st.write('プレグレスバーの表示')
st.write('Start!!')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i)
    time.sleep(0.1)
st.write('Done!!!1')





# with st.expander("問い合わせ"):
#      st.markdown("問い合わせ内容1")
#      st.markdown("問い合わせ内容2")
#expander.wirte('問い合わせ内容を書く')

# st.write('レイアウトを整える')
# st.sidebar.write('サイドバー表示')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# st.write('あなたの今の調子は', condition, 'です。')

# st.write('テキストボックス')
# text = st.sidebar.text_input('あなたの趣味を教えて下さい')
# st.write('あなたの趣味は', text, 'です。')


st.write('Interactive Widgets')
st.write('スライダー')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
st.write('あなたの今の調子は', condition, 'です。')

st.write('テキストボックス')
text = st.text_input('あなたの趣味を教えて下さい')
st.write('あなたの趣味は', text, 'です。')

st.write('セレクトボックス')
option = st.selectbox(
    'あなたが好きな数字を教えて下さい：', 
    list(range(1,11))

)
'あなたの好きな数字は', option, 'です。'


st.write('Display Image')
st.write('チェックボックス')
if st.checkbox('Show Image'):
    img = Image.open('image01.jpeg')
    st.image(img, caption='りんごとうさぎ（use_column_width=False）',use_column_width=False)



st.write('DataFrame')
df3  = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)
st.dataframe(df3)
st.map(df3)

df2  = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

st.dataframe(df2)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

st.write(df)

st.dataframe(df.style.highlight_max(axis = 0), width = 300, height = 300)

st.table(df.style.highlight_max(axis = 0))

