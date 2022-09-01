import streamlit as st
from gsheetsdb import connect
import pandas as pd


st.title('M5Stackテスト')
conn = connect()
def run_query(query):
    rowdata = conn.execute(query, headers=1)
    return rowdata

sheet_url = "https://docs.google.com/spreadsheets/d/1WPqQRH6kuuQLrPsI18r-qQbDmN0oYR8QUuKKw0VKmJQ/edit?usp=sharing"
rowdata = run_query(f'SELECT * FROM "{sheet_url}"')
# # # スプレッドシートの内容をstreamlitに表示する
# st.write('''## スプレッドシートの内容を行ごとに表示する''')
# for row in rowdata: st.write(f"{row}")
# # それぞれの列の情報を個別に抽出する
# st.write('''## それぞれの列の情報を個別に抽出する''')
# for row in rowdata: st.write(f"{row.データNo.}の{row.名前}の{row.値段}円です。")
# データフレームに変換し表示する
st.write('''## M5Stackスプレッドシート収集データ一覧''')
row_list = []
for row in rowdata: row_list.append(row)
df=pd.DataFrame(row_list)
st.table(df)