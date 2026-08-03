import streamlit as st

st.title("welcome to academy")
st.image("https://facts.net/wp-content/uploads/2023/07/16-facts-about-football-1689928910.jpg",width=200,caption="sports")
st.subheader("here is your application")
st.text("name:and other details")
st.write("i am hear to help you")
game=st.selectbox("select your fav game:",["cricket","foot ball","tennis","dhagudumuthalu"])
st.write(f"your choice is {game}")
games=st.multiselect("select your fav game:",["cricket","foot ball","tennis","dhagudumuthalu"])
st.write(games)
join=st.checkbox("are you willing to join")
if join :
    st.success("you are in")
    pur=st.radio("select one",["training","visit","other"])
    if pur == "training":
        level = st.slider("what is your level??", 0, 10, 5)
        dob = st.date_input("enter your date of birth")
        st.button("click here for training")
    elif pur == "visit":
        st.write("you can go for visit")
        st.number_input("how many members are visiting:", 1, 5)
    else:
        if st.text_input("enter hear"):
            st.success("thank you,come again later")
else:
    st.error("sorry")


with st.expander("know about academy"):
    st.write("""
    1. this academy is to train players from 0 to hero
    2. compared to academys in all over india we are the first every time like a monarch
    """)
st.sidebar.subheader("menu bar")
st.sidebar.text_input("search hear",width=600)

st.markdown("# welcome back")
st.markdown(">good morning")
st.markdown("`how are you`")
st.markdown("```import streamlit as st```")
st.markdown("[open instagram](https://r.search.yahoo.com/_ylt=Awr99cPUd2tolbgUKydXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1753083093/RO=10/RU=https%3a%2f%2fwww.instagram.com%2f/RK=2/RS=ogyUSdlyFOLCfKxNzxv5rQ60Tws-)")

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 30px;
        font-size: 16px;
        border: none;
        border-radius: 100px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)
c=st.button("click hear")
st.button("gjymkjh")

# st.markdown(f"[](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://web.whatsapp.com/&ved=2ahUKEwjc8Kn1nqqOAxXsyzgGHco4HHcQFnoECCcQAQ&sqi=2&usg=AOvVaw1V09js0t2A_u6GXzP1jPsR)")

vid=open("../../WhatsApp Video 2025-07-01 at 5.04.13 PM.mp4", "rb")
vid1=vid.read()
st.video(vid1)
st.text_area("give me feedback")