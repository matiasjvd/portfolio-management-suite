import streamlit as st

# --- Config ---
st.set_page_config(
    page_title="BVC Portfolio Suite",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def show_dashboard():
    """Main dashboard with modules"""
    st.markdown(
        """
        <div style="text-align:center; padding: 2rem 0 1.5rem 0;">
          <h1 style="color:#fff; font-size:2.5rem; margin:0 0 .5rem; font-weight:300;">
            BVC Portfolio Suite
          </h1>
          <p style="color:rgba(255,255,255,.55); font-size:1rem; margin:0;">
            Buena Vista Capital
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### Available Modules")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(card("Funds Ranking", "Analysis and ranking of investment funds"), unsafe_allow_html=True)
        st.markdown(link("Open Funds Ranking",
                         "https://matiasjvd-ranking-fondos-funds-dashboard-oll7la.streamlit.app/"),
                    unsafe_allow_html=True)

    with c2:
        st.markdown(card("Macro Dashboard", "Macroeconomic analysis and markets"), unsafe_allow_html=True)
        st.markdown(link("Open Macro Dashboard", "https://dashboard-macro-bvc.streamlit.app/"),
                    unsafe_allow_html=True)

    with c3:
        st.markdown(card("Black-Litterman", "Advanced portfolio optimization"), unsafe_allow_html=True)
        st.markdown(link("Open Black-Litterman", "https://black-litterman-app.streamlit.app/"),
                    unsafe_allow_html=True)

    with c4:
        st.markdown(card("Portfolio Analysis", "Detailed portfolio analysis"), unsafe_allow_html=True)
        st.markdown(link("Open Portfolio Analysis", "https://portfolio-analysis-bvc.streamlit.app/"),
                    unsafe_allow_html=True)

def card(title: str, desc: str) -> str:
    return f"""
    <div style="background: rgba(255,255,255,.03); padding: 1.25rem; border-radius: 10px;
                text-align: center; border: 1px solid rgba(255,255,255,.1); height: 200px;
                display: flex; flex-direction: column; justify-content: center;">
        <h4 style="color:#fff; margin:0 0 .75rem; font-weight:400;">{title}</h4>
        <p style="color: rgba(255,255,255,.65); font-size:.9rem; margin:0;">{desc}</p>
    </div>
    """

def link(label: str, url: str) -> str:
    return f"""
    <p style="text-align:center; margin:.75rem 0 0;">
      <a href="{url}" target="_blank"
         style="display:inline-block; padding:.6rem 1rem; border:1px solid rgba(255,255,255,.2);
                border-radius:8px; text-decoration:none; color:#fff;">
        {label}
      </a>
    </p>
    """

# --- Estilos globales básicos ---
st.markdown(
    """
    <style>
      .stApp{background:linear-gradient(135deg,#0e1117 0%,#1a1a1a 100%);}
      #MainMenu, footer, header {visibility:hidden;}
      .stButton > button{
        background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1);
        border-radius:6px; color:#fff; font-weight:400; padding:.7rem 1.1rem;
      }
      .stButton > button:hover{
        background:rgba(255,255,255,.08); border-color:rgba(255,255,255,.2);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    show_dashboard()

if __name__ == "__main__":
    main()
