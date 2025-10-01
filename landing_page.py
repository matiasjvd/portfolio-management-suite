import streamlit as st
import time
import traceback

# --- Config ---
st.set_page_config(
    page_title="BVC Portfolio Suite",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Auth bootstrap (con fallback si falta el módulo) ---
try:
    from auth_manager import AuthManager  # debe existir en /Files
    auth_manager = AuthManager()
except Exception:
    auth_manager = None  # fallback para que la app no muera
    st.sidebar.warning("AuthManager no disponible. Modo demo.")
    st.sidebar.code(traceback.format_exc())

def show_login_page():
    """UI de login minimalista"""
    st.markdown(
        """
        <div style="text-align:center; padding: 3rem 0 2rem 0;">
          <h1 style="color:#fff; font-size:2.2rem; margin:0 0 .5rem; font-weight:300;">
            BVC Portfolio Suite
          </h1>
          <p style="color:rgba(255,255,255,.55); font-size:.95rem; margin:0;">
            Buena Vista Capital
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        with st.form("login_form", clear_on_submit=False):
            st.markdown(
                "<div style='text-align:center; margin-bottom:1rem;'>"
                "<h4 style='color:#fff; font-weight:400;'>Acceso</h4></div>",
                unsafe_allow_html=True,
            )
            username = st.text_input("Usuario", placeholder="Ingresa tu usuario", label_visibility="collapsed")
            password = st.text_input("Contraseña", type="password", placeholder="Ingresa tu contraseña", label_visibility="collapsed")
            login_btn = st.form_submit_button("Ingresar", use_container_width=True)

    if login_btn:
        if not (username and password):
            st.error("Completa todos los campos")
            return
        with st.spinner("Verificando..."):
            time.sleep(0.4)
        if auth_manager:
            try:
                ok, msg = auth_manager.authenticate(username, password)
            except Exception:
                st.error("Error ejecutando autenticación")
                st.code(traceback.format_exc())
                return
        else:
            # Modo demo si no hay AuthManager
            ok, msg = (True, "demo")

        if ok:
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
            st.success("Acceso autorizado")
            time.sleep(0.4)
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

    st.markdown(
        """
        <div style="text-align:center; margin-top:1.25rem; padding:1rem;
             background:rgba(255,255,255,.03); border-radius:8px;
             border:1px solid rgba(255,255,255,.1);">
          <p style="margin:0; color:rgba(255,255,255,.55); font-size:.85rem;">
            Contacta al administrador para obtener credenciales de acceso
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_dashboard():
    """Dashboard principal con módulos"""
    c1, c2 = st.columns([4, 1])
    with c1:
        st.markdown(
            f"""
            <div style="padding: .75rem 0 0;">
              <h2 style="margin:0; color:#fff; font-weight:300;">BVC Portfolio Suite</h2>
              <p style="margin:0; color:rgba(255,255,255,.55); font-size:.9rem;">
                Usuario: {st.session_state.get('user','')}
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        if st.button("Salir", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    st.markdown("---")
    st.markdown("### Módulos Disponibles")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(card("Ranking de Fondos", "Análisis y ranking de fondos de inversión"), unsafe_allow_html=True)
        st.markdown(link("Abrir Ranking de Fondos",
                         "https://matiasjvd-ranking-fondos-funds-dashboard-oll7la.streamlit.app/"),
                    unsafe_allow_html=True)

    with c2:
        st.markdown(card("Dashboard Macro", "Análisis macroeconómico y mercados"), unsafe_allow_html=True)
        st.markdown(link("Abrir Dashboard Macro", "https://dashboard-macro-bvc.streamlit.app/"),
                    unsafe_allow_html=True)

    with c3:
        st.markdown(card("Black-Litterman", "Optimización de portfolios avanzada"), unsafe_allow_html=True)
        st.markdown(link("Abrir Black-Litterman", "https://black-litterman-app.streamlit.app/"),
                    unsafe_allow_html=True)

    with c4:
        st.markdown(card("Análisis Portafolios", "Análisis detallado de portafolios"), unsafe_allow_html=True)
        st.markdown(link("Abrir Análisis Portafolios", "https://analisis-portafolios-bvc.streamlit.app/"),
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

def check_auth() -> bool:
    if st.session_state.get("authenticated", False):
        return True
    show_login_page()
    return False

# --- Estilos globales básicos ---
st.markdown(
    """
    <style>
      .stApp{background:linear-gradient(135deg,#0e1117 0%,#1a1a1a 100%);}
      #MainMenu, footer, header {visibility:hidden;}
      .stTextInput > div > div > input{
        background:rgba(255,255,255,.03); border:1px solid rgba(255,255,255,.1);
        border-radius:6px; color:#fff; padding:.75rem; font-weight:300;
      }
      .stTextInput > div > div > input:focus{
        border-color:rgba(255,255,255,.3);
        box-shadow:0 0 0 2px rgba(255,255,255,.1);
      }
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
    if check_auth():
        show_dashboard()

if __name__ == "__main__":
    main()
