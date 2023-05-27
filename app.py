import streamlit as st

profile():
    st.title('プロフィール')
    nickname = st.text_input('ニックネーム')
    height = st.number_input('身長(cm)', min_value=0.0, max_value=300.0, step=0.1)
    age = st.number_input('年齢', min_value=0, max_value=150, step=1)
    gender = st.selectbox('性別', ['男性', '女性'])
    if st.button('保存'):
        # プロフィール情報を保存する処理
        st.success('プロフィール情報を保存しました。')
