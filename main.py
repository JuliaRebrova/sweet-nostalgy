import streamlit as st
import random

st.write("""
# Welcome to 2007 year
This app change the register of your text to 'fEnCE' register


""")


def fence(strr):
    s_fence = ''
    for i in range(len(strr)):
        a = random.randint(0,1)
        if a == 0:
            s_fence += strr[i].lower()
        else:
            s_fence += strr[i].upper()
    return s_fence
        
text = st.text_input('Input your text here:')

st.write('Output:')

st.write(fence(text))

if st.button('Change register'):
    st.markdown("![(ˆ(oo)ˆ)](https://i.gifer.com/embedded/download/4KBJ.gif)")
