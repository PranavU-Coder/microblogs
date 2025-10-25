import streamlit as st
import os

from themes import setup_theme, render_theme_toggle, handle_theme_refresh

st.set_page_config(layout='wide', page_title="A Turning Point")
setup_theme()
render_theme_toggle() 
handle_theme_refresh()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(os.path.join(os.getcwd(), 'public', 'og_cat.jpg'))
    st.caption("my fave catto by far")
    
    st.header("**Pranav U**")
    st.subheader("(Trying) to make good software")
    
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        st.link_button("My Work", "https://github.com/PranavU-Coder", 
                       icon=":material/code:", use_container_width=True)
    
    with btn_col2:
        if st.button("Blogs (please don't read)", icon=":material/article:", 
             use_container_width=True):
             st.switch_page("pages/oversaturation.py")