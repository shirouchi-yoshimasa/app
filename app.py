import streamlit as st

def profile():
    st.title('プロフィール')
    nickname = st.text_input('ニックネーム')
    height = st.number_input('身長(cm)', min_value=0.0, max_value=300.0, step=0.1)
    age = st.number_input('年齢', min_value=0, max_value=150, step=1)
    gender = st.selectbox('性別', ['男性', '女性'])
    if st.button('保存'):
        # プロフィール情報を保存する処理
        st.success('プロフィール情報を保存しました。')

#
def weight():
    st.title('体重記録')
    weight = st.number_input('体重(kg)', min_value=0.0, max_value=500.0, step=0.1)
    if st.button('保存'):
        # 体重を保存する処理
        st.success('体重を保存しました。')

#
def meal():
    st.title('食事内容')
    calorie = st.number_input('総カロリー', min_value=0, max_value=10000, step=1)
    if st.button('保存'):
        # カロリーを保存する処理
        st.success('カロリーを保存しました。')


def bmi():
    st.title('体脂肪BMI計算')
    weight = st.number_input('体重(kg)', min_value=0.0, max_value=500.0, step=0.1)
    height = st.number_input('身長(cm)', min_value=0.0, max_value=300.0, step=0.1)
    if st.button('計算'):
        # 体脂肪率とBMIを計算する処理
        st.success('体脂肪率とBMIを計算しました。')

def steps():
    st.title('歩数')
    steps = st.number_input('歩数', min_value=0, max_value=100000, step=1)
    if st.button('保存'):
        # 歩数を保存する処理
        st.success('歩数を保存しました。')

def exercise():
    st.title('筋トレ系運動種類と時間')
    exercise_type = st.text_input('種類')
    exercise_time = st.number_input('時間(分)', min_value=0, max_value=1440, step=1)
    if st.button('保存'):
        # 筋トレ系運動種類と時間を保存する処理
        st.success('筋トレ系運動種類と時間を保存しました。')

        
def reflection():
    st.title('今日の良かったことと反省')
    text = st.text_area('テキスト')
    if st.button('保存'):
        # テキストを保存する処理
        st.success('テキストを保存しました。')

