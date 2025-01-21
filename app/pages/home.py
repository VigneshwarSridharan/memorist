import streamlit as st

st.write("""
# Hello memorist
This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique properties:

- You can pass in multiple arguments, all of which will be written.
- Its behavior depends on the input types as follows.
- It returns None, so its "slot" in the App cannot be reused.
""")

st.button("Click Me!",type="primary")