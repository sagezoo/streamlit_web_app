import streamlit as st
from PIL import Image
import datetime

image=Image.open("logo.png")
st.image(image,width=200)

st.title("ウェアラブルカメラ確認リスト")
st.caption("以下の項目について、映像確認後チェックマークを付けて下さい")
st.subheader("チェックリスト")

eria_name=st.selectbox("拠点名",("柏OPC","千葉OPC","神奈川・東京OPC","沖縄支店"))
print(eria_name)

with st.form(key="check_list"):
    if eria_name=="柏OPC":
        camera_name_kashiwa=st.selectbox("【柏OPC】カメラ使用者",("藤田班","島田班","●●班","××班"))
        print(camera_name_kashiwa)
    elif eria_name=="千葉OPC":
        camera_name_chiba=st.selectbox("【千葉OPC】カメラ使用者",("長妻班","佐藤(淳)班","●●班","××班"))
        print(camera_name_chiba)
    else:
        camera_name_kanagawa_tokyo=st.selectbox("【神奈川・東京OPC】カメラ使用者",("若葉班","横田班","●●班","××班"))

    start_date=st.date_input("工事日",datetime.date.today())
    
    check_list_1=st.checkbox("1.×××")
    check_list_2=st.checkbox("2.×××")
    check_list_3=st.checkbox("3.×××")
    check_list_4=st.checkbox("4.×××")
    print(check_list_1,check_list_2,check_list_3,check_list_4)    
    
    submit_btn=st.form_submit_button("送信")    
    if submit_btn:
        st.text(f"チェックリストが提出されました！")