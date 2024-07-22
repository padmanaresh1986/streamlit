import streamlit as st
import pandas as pd
#remove hamburger menu in the top right corner
#play with CSS
st.markdown("""
<style>
.st-emotion-cache-w3nhqi.ef3psqc4
{
visibility:hidden;
}
<style>
""", unsafe_allow_html=True)


table=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [8,9,10,11,12,13,14]})

st.title("Hi I am streamlit web app")
st.subheader("Hi I am your sub header")
st.header("Hi I am header")
st.text("This is a paragraph text")
st.markdown("**hello** world ")
st.markdown("[Google](https://www.google.com)")
st.markdown("-----")
# more markdown examples on https://markdownguide.offshoot.io/cheat-sheet/
st.caption("Hi I am caption")
st.latex(r"\begin{pmatrix}a&b&c\\c&d&e\end{pmatrix}")
# more math formulas on https://katex.org/
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
def func():
    return e
"""
st.code(code,language="python")

javaCode = """
public static void main(String[] args){
  System.out.println("Hellow World")
}
"""
st.code(javaCode,language="java")

st.write("## h2 Tag")

st.metric(label="Wind Speed", value='120ms\^-1',delta="1.4ms\^-1")

st.table(table)
st.dataframe(table)

st.image(image="images/_0b5b80a7-ae96-4823-9433-8fa6db6c9d85.jpeg")
st.audio("audio/OAF_back_angry.wav")
#st.video("video.mp4)

state = st.checkbox("This is a checkbox")
if state:
    st.write("Check box is checked")
else:
    pass

def checkbox_clicked():
    print(st.session_state.values) ## need to access checkbox state here

st.checkbox("Checkbox callback test", on_change=checkbox_clicked(),key="chk")

radio_btn = st.radio("In which country you live",options=("US","UK","India"))
print(radio_btn)

def button_clicked():
    print("button clicked")

btn=st.button("Click me", on_click=button_clicked())

def value_selected():
    print("value selected")
select = st.selectbox("What is your favorite car",options=("Tata","Mahindra","Force"),on_change=value_selected())

multi_select = st.multiselect("This is multi select",options=["Microsoft","Apple","Amazon","Oracle"])
st.write(multi_select)






