# https://github.com/bdoey/FUjkal/blob/master/SCR-20221215-spp-2v1.jpg


import streamlit as st

st.markdown("# This fuckin guy...")

if st.button('Do you like this guy?'):
    st.write("We don't either!")
# else:
#     st.write('Goodbye')

# Display an image from a URL
image_url = "https://github.com/bdoey/FUjkal/blob/master/SCR-20221215-spp-2v1.jpg?raw=true"
st.image(image_url, width=700)

