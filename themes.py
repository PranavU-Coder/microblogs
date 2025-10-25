import streamlit as st

def initialize_theme_state():
    if "themes" not in st.session_state:
        st.session_state.themes = {
            "current_theme": "dark",
            "refreshed": False,
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "white",
                "theme.primaryColor": "#5591f5",
                "theme.secondaryBackgroundColor": "#82E1B9",
                "theme.textColor": "#0a1464",
                "button_face": "🌙",
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "black",
                "theme.primaryColor": "#29af4f",
                "theme.secondaryBackgroundColor": "#261480",
                "theme.textColor": "white",
                "button_face": "☀️",
            },
        }


def apply_theme(theme_key):
    theme = st.session_state.themes[theme_key]
    for key, value in theme.items():
        if key.startswith("theme"):
            st._config.set_option(key, value)


def change_theme():
    current = st.session_state.themes["current_theme"]
    new_theme = "dark" if current == "light" else "light"
    st.session_state.themes["current_theme"] = new_theme
    apply_theme(new_theme)
    st.session_state.themes["refreshed"] = False


def render_theme_toggle(col_ratio=[1, 12, 1]):
    col1, col2, col3 = st.columns(col_ratio)
    with col3:
        current_theme = st.session_state.themes["current_theme"]
        button_icon = st.session_state.themes[current_theme]["button_face"]
        st.button(button_icon, on_click=change_theme, key="theme_toggle_btn")


def handle_theme_refresh():
    if not st.session_state.themes["refreshed"]:
        st.session_state.themes["refreshed"] = True
        st.rerun()


def setup_theme():
    initialize_theme_state()
    apply_theme(st.session_state.themes["current_theme"])