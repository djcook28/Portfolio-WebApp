import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout='wide')

app_dict = pandas.read_csv('appTable.csv',sep=",")
app_dict_len = len(app_dict)

st.title('Home')
st.write("Below you will find some Python Apps that I built.  Feel free to contact me.")

col1, empty_col, col2 = st.columns([2, 0.5, 2])
col_len = int(app_dict_len / 2)

with col1:
    for int, app in app_dict[:col_len].iterrows():
        st.subheader(app['Title'])
        st.write(app['Description'])
        st.image(f"images/{app['image']}")
        #you can either have a URL as text as below or a link button
        # st.link_button(label=f'{app['Title']} Source Code', url=app['URL'])
        st.write(f"[Source Code]({app['URL']})")


with col2:
    for int, app in app_dict[col_len:].iterrows():
        st.subheader(app['Title'])
        st.write(app['Description'])
        st.image(f"images/{app['image']}")
        #st.link_button(label=f'{app['Title']} Source Code', url=app['URL'])
        st.write(f"[Source Code]({app['URL']})")
