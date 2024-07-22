import streamlit as st
from datetime import time

#upload image files
st.title("Uploading files")
image= st.file_uploader("please upload file here",type=["jpeg"])
if image is not None:
    st.image(image=image)

    #upload multiple images

st.title("Uploading multiple files")
images = st.file_uploader("please upload multiple files here",type=["jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image=image)


#slider

val = st.slider(label="This is slider", min_value=0 , max_value=10, value= 2)
st.write(val)

input = st.text_input("Enter your data", max_chars=60)
st.write(input)

input1 = st.text_area("Enter your data", max_chars=60)
st.write(input1)

date = st.date_input("enter date")
st.write(date)

def converter(val):
    m,s,ms = val.split(":")
    t_s=int(m)*60+int(s)+int(ms)/1000
    return t_s

tim = st.time_input("Set timer", value=time(0,0,0))
print(type(tim))
if str(tim) == "00:00:00":
    st.write("please set timer")
else:
    sec = converter(str(tim))
    bar = st.progress(0)
    per = sec/100
    status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        status.write(str(i+1)+ " %")
        #sleep(par)

