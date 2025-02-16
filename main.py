import streamlit as st
import csv
from PIL import Image

#col1, col2 = st.columns(2)

appDict = csv.DictReader(open('appTable.csv'))

st.title('Home')

for app in appDict:
    st.subheader(app['Title'])
    st.write(app['Description'])
    app_image = Image.open(f"images/{app['image']}")
    st.image(app_image)
    st.link_button(label=f'{app['Title']}', url=app['URL'])
