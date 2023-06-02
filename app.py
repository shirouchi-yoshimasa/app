import streamlit as st
import csv

#ログイン情報
id_pwd = {'test': 'test'}

#ログインページ
def login():
    st.title('ログイン')
    user_id = st.text_input('ユーザーID')
    password = st.text_input('パスワード', type='password')
    if st.button('ログイン'):
        if user_id in id_pwd:
            if password == id_pwd[user_id]:
                st.success('ログインに成功しました')
                st.session_state.login = True  # ログイン状態をTrueに設定
                st.experimental_rerun()  # main()関数を再度実行
            else:
                st.error('パスワードが間違っています')
        else:
            st.error('ユーザーIDが間違っています')

def save_profile(nickname, height, age, gender):
    with open('profile.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nickname, height, age, gender])

def profile():
    st.title('プロフィール')
    nickname = st.text_input('ニックネーム')
    height = st.number_input('身長(cm)', min_value=0.0, max_value=300.0, step=0.1)
    age = st.number_input('年齢', min_value=0, max_value=150, step=1)
    gender = st.selectbox('性別', ['男性', '女性'])
    if st.button('保存', key='profile_save_button'):
        # プロフィール情報を保存する処理
        st.success('プロフィール情報を保存しました。')

def weight():
    st.title('体重記録')
    weight = st.number_input('体重(kg)', min_value=0.0, max_value=500.0, step=0.1)
    if st.button('保存', key='weight_button'):
        # 体重を保存する処理
        st.success('体重を保存しました。')

def meal():
    st.title('食事内容')
    calorie = st.number_input('総カロリー', min_value=0, max_value=10000, step=1)
    if st.button('保存', key='meal_save_button'):
        # カロリーを保存する処理
        st.success('カロリーを保存しました。')

def bmi(weight, height):
    st.title('体脂肪BMI計算')
    if st.button('計算'):
        # 体脂肪率とBMIを計算する処理
        bmi_0 = weight / (height / 100) ** 2
        st.success(f'あなたのBMIは{bmi_0:.2f}です。')

def steps():
    st.title('歩数')
    steps = st.number_input('歩数', min_value=0, max_value=100000, step=1)
    if st.button('保存', key='steps_save_button'):
        # 歩数を保存する処理
        st.success('歩数を保存しました。')

def exercise():
    st.title('筋トレ系運動種類と時間')
    exercise_type = st.text_input('種類')
    exercise_time = st.number_input('時間(分)', min_value=0, max_value=1440, step=1)
    if st.button('保存', key='exercise_save_button'):
        # 筋トレ系運動種類と時間を保存する処理
        st.success('筋トレ系運動種類と時間を保存しました。')

def reflection():
    st.title('今日の良かったことと反省')
    text = st.text_area('テキスト')
    if st.button('保存', key='reflection_save_button'):
        # テキストを保存する処理
        st.success('テキストを保存しました。')
        
#ログアウトページ
def logout():
    if st.button('ログアウト'):
        st.session_state.login = False
        st.session_state.logout = True  # ログアウト状態をTrueに設定
        st.success('ログアウトしました')


#メインページ
def main():
    st.set_page_config(page_title='ダイエット記録アプリ', page_icon=':memo:', layout='wide')
    st.title('ダイエット記録アプリ')
    if 'login' not in st.session_state:
        st.session_state.login = False
    if not st.session_state.login:
        if login():
            st.session_state.login = True
    else:
        # ページを切り替えるためのサイドバーを作成する
        menu = ['プロフィール', '体重記録', '食事内容', '体脂肪BMI計算', '歩数', '筋トレ系運動種類と時間', '今日の良かったことと反省']
        choice = st.sidebar.selectbox('メニュー', menu)
        #choice = st.selectbox('メニュー', menu)
        if choice == 'プロフィール':
            profile()
        elif choice == '体重記録':
            weight()
        elif choice == '食事内容':
            meal()
        elif choice == '体脂肪BMI計算':
            height = st.number_input('身長(cm)', min_value=120, max_value=250, step=0)
            weight = st.number_input('体重(kg)', min_value=30, max_value=500, step=0)
            bmi(weight, height)
        elif choice == '歩数':
            steps()
        elif choice == '筋トレ系運動種類と時間':
            exercise()
        elif choice == '今日の良かったことと反省':
            reflection()
        elif choice == 'ログアウト':
            logout()

if __name__ == '__main__':
    main()
