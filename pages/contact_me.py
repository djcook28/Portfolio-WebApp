import streamlit as st
import send_email
import pandas

subjects = []
topics_csv = pandas.read_csv("topics.csv")

with st.form('Contact Me'):
    user_email = st.text_input(label='Enter your email: ',key='email input')
    user_subject = st.selectbox('Subject of communication', topics_csv['topic'])
    user_message = st.text_area(label='Enter your message: ', key='message input')

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        message = f"""
        Subject: New email regarding {user_subject}
        
        From {user_email}
        {user_message}
        """

        send_email.send_email(message)

        st.info('Message sent successfully')