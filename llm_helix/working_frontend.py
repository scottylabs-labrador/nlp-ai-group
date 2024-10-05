import streamlit as st



message = st.chat_message("The Corpse of Andrew Carnegie",avatar="Andrew-Carnegie.jpg")
message.write('Good day, what can I help you with in this beautiful day?')
prompt = st.chat_input('Talk to Sir Carnegie!')

if prompt:
    st.write(f'the user has sent the follow prompt {prompt}')
