import streamlit as st
import random as rd
import smtplib
# from game2 import accounts

import os

num=[1,2,3,4,5,6,7,8,9,0]
otp=rd.choices(num,k=6)
otp1=""
for i in otp:
    otp1+=str(i)

st.title("   welcome to ingenuity games")
st.text("click on sign up if you are new to ingenuity games!")
st.link_button("sign up"," http://localhost:8502")
#st.write("if you are all ready having an account  in ingenuity games!so,just login.html")
st.write("      Then Enter:")
gmail=st.text_input("gmail:")
# if gmail in accounts:
generate_OTP = st.button("generate OTP ")

if generate_OTP :
    st.session_state.otp2=otp1
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("storybook8688@gmail.com","wfls nlpb tddq axbd")
    server.sendmail("storybook8688@gmail.com",gmail,
                        "subject:ingenuity games"
                        f"set_content(if you want to login.html and restore your ingenuity games account"
                        f"then here is your one time password:{otp1})")
    server.quit()

    OTP=st.text_input("enter OTP:")
    if st.button("submit OTP"):
        if OTP==st.session_state.otp2 :
                st.success("login.html successful")
                st.text("click here to start playing now")
                st.link_button("start plying"," http://localhost:8503")
        else:st.error("incorrect OTP")
# else:st.error("there is no existing account with this gmail ");st.stop()

