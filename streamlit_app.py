# https://github.com/bdoey/FUjkal/blob/master/SCR-20221215-spp-2v1.jpg


import streamlit as st

st.markdown("# This fuckin guy...")
st.markdown("\n Do you like this guy?")

if st.button('Nope!'):
    st.write("We don't either!")
else:
    st.button('Yup!')
    st.write('Goodbye, loser.')

# Display an image from a URL
image_url = "https://github.com/bdoey/FUjkal/blob/master/SCR-20221215-spp-2v1.jpg?raw=true"
st.image(image_url, width=300)

