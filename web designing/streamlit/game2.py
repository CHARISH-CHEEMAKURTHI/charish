import random as rd
from logging import exception
import streamlit as st
import smtplib

num=[1,2,3,4,5,6,7,8,9,0]
otp=rd.choices(num,k=6)
otp1=""
for i in otp:
    otp1+=str(i)

accounts=[]
st.title("   welcome to ingenuity games")
st.text("if you already have an account click on login.html for loging in")
st.link_button("login.html", " http://localhost:8501")
st.write("if you are new to ingenuity games!.so,sign up first")
st.write("      Then Enter:")
name=st.text_input("name:")
if len(name)==0:
    st.error("please enter your name")
    st.stop()
username=st.text_input("username:")
if len(username) <= 5:
    st.error("username must at least 5  characters")
    st.stop()
dob=st.date_input("date of birth")
gmail = st.text_input("gmail:")
if gmail not in accounts:
    generate_OTP = st.button("generate OTP ")
    if generate_OTP:
        st.session_state.otp2 = otp1
        try:
            full_msg=f"subject:{"ingenuity games"}\n\n{"if you want to sigen in ingenuity games account then here is your one time password:",otp1 }"
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("storybook8688@gmail.com", "wfls nlpb tddq axbd")
            server.sendmail("storybook8688@gmail.com", gmail,full_msg)
            server.quit()
        except Exception as e :
            st.error(f"faild to login.html sender email:{e}")
OTP = st.text_input("enter OTP:")
if st.button("submit OTP"):
    if OTP == st.session_state.otp2:
        st.success("sign in successful")
        accounts+= [gmail]
        st.text("click on login.html for loging in")
        st.link_button("login.html", " http://localhost:8501")
    else:
        st.error("incorrect OTP")

