import streamlit as st
import numpy as np
import time
import datetime
from  PIL import Image as i


st.set_page_config("sivi",page_icon="heart")
st.title("💗sivi a cute love-story💗")
base="light"
backgroundColor="#dc69ba"
font="serif"
love=st.text_input("***enter your loveee to see this cute page of ours***")
if not love:
    st.error("enter your lovee in few words❤️")
    st.stop()
st.success("now you will enter the magical and sweet love story of siviiiiiiiiiii🩷🩷🩷!!!!!!!!!!!!!!!!")
st.subheader("Chalooo baby abb shuruuu karteee okkkk majhaa cutuuuu❤️❤️❤️")
st.text("abb suno cutu this is all how it starteddd!!!!!!!!!")
sona1=i.open("images/sona1stimage.jpg")
st.image(sona1,width=300)
click=st.button("karoo karoo click")

if click:
    st.write('''dekhliyaaaa naaa iss cute face ko tum bolo kon nahi flat hoga
           iss cute saa pyaara sa face dekh kee haaaaaaa tho mai tho
           fidhaaaa hogayaaa bygod❤️❤️❤️''')
time.sleep(5)
with st.expander("chalo dekhooo yeh apnii pyaari pyaari eyes see"):
    sona2=i.open("images/sona2ndimage.jpg")
    st.image(sona2,width=300)
with st.empty():
    for clock in range(8):

        st.write("wait karooo arahaii next part🩷")
        time.sleep(1)
with st.expander("abb iski kahanii padoo"):
    st.markdown('''***haaaa abb stacking chalu hogaya tha yeh photo
                           maine tumare birthday ke din bhanu see li thi
                           haa haa hasiii arii hainaa haslooo😚😚***''')

st.write('''padliii yaa cutu aur bohot haiiii karoo karoo wait
               haaa baby yeh tha mere bday ke din jab hum gaye the
               walk peyyyy🚶‍♀️🚶‍♀️
         ''')
image1=i.open("images/image 4.jpg")
st.image(image1,width=200)
st.write("yeh mai hu tumse bohot intrest see chat kartehue")
me=i.open("images/myimagech.jpg")
st.image(me,width=200)
st.write("ha baby jaise taise karke maine tume patalia😚😚😚😚")
st.subheader("baby yaha see cute cute memories hai apniii sweet sii")
tab1,tab2=st.tabs(["amritsar trip","vrindhavan trip"])
with tab1:
    amr=i.open("images/amritsar1.jpg")
    st.image(amr,width=300)
    amr2=i.open("images/amritsar2.jpg")
    st.image(amr2,width=300)
    st.write('''yeh tho apne pyaare photos yaad hai baby
                yeh kichate time shua bhi padathaa😂😂😂
    ''')
with tab2:
    vrind1=i.open("images/vrindhavan1.jpg")
    st.image(vrind1,width=300)
    vrid2=i.open("images/vrindhavan2.jpg")
    st.image(vrid2,width=300)
    st.write('''bubuuu acha laganaa apni first trip to 
                vrindhavan ek saat wali photos dekhke
                ''')

st.subheader("pyaari hai naa photos")
st.write("abb dekho apne sweet sweet dates ki photo")
tab1,tab2=st.tabs(["19/11/2023","18/2/2024"])
with tab1:
    date1=i.open("images/date1.jpg")
    st.image(date1,width=300)
    date11=i.open("images/date11.jpg")
    st.image(date11,width=300)
    date111=open("images/date111.mp4","rb")
    st.video(date111)
with tab2:
    date2 = i.open("images/date2.jpg")
    st.image(date2, width=300)
    date22 = i.open("images/date22.jpg")
    st.image(date22, width=300)

st.subheader("abb chota game khelo like lovetester")
st.title("LOVE CALCULATOR")
with st.form("love calculator"):
    col1,col2,col3=st.columns([3,2,1])
with col1:
    scale=st.number_input("enter your love for sivi in scale of 1-10")
with col2:
    word=st.text_input("guess only 1 word about sivi which sivi loves")
with col3:
    submit=st.form_submit_button(label="calculate")
if submit:
    if scale==10 and word=="nunnu munnu bacha"or word=="ihitha":
        st.success("good my husband correct tumare love 100% hai")
    else:

        st.error("baby yaar sonchooooooo")
st.subheader("baby yeh favorite lohrii hai pata hai!!!!")
audioo=open("images/sona_lorimp3.mp3","rb")
st.audio(audioo.read())

st.header("bubuuu last me apna pyaara dance dekhooo")
with st.empty():
    for process_completed in range(101):
        time.sleep(.1)
        st.progress(process_completed,text="videoo coming")

pyara=open("images/dance.mp4","rb")
st.video(pyara)
st.balloons()
images/amritsar1.jpg
