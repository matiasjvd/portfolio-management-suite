import streamlit as st
import time
from auth_manager import AuthManager

# Configuración de la página
st.set_page_config(
    page_title="BVC Portfolio Suite",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicializar el gestor de autenticación
auth_manager = AuthManager()

def show_login_page():
    """Página de login minimalista"""
    
    # Título principal
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0 2rem 0;">
        <h1 style="color: #ffffff; font-size: 2.5rem; margin-bottom: 0.5rem; font-weight: 300;">BVC Portfolio Suite</h1>
        <p style="color: rgba(255, 255, 255, 0.5); font-size: 1rem;">Buena Vista Capital</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Login form centrado
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        with st.form("login_form", clear_on_submit=False):
            st.markdown("<div style='text-align: center; margin-bottom: 1.5rem;'><h4 style='color: #ffffff; font-weight: 400;'>Acceso</h4></div>", unsafe_allow_html=True)
            
            username = st.text_input("Usuario", placeholder="Ingresa tu usuario", label_visibility="collapsed")
            password = st.text_input("Contraseña", type="password", placeholder="Ingresa tu contraseña", label_visibility="collapsed")
            
            login_button = st.form_submit_button("Ingresar", use_container_width=True)
            
            if login_button:
                if username and password:
                    with st.spinner('Verificando...'):
                        time.sleep(0.5)
                        success, message = auth_manager.authenticate(username, password)
                    
                    if success:
                        st.session_state["authenticated"] = True
                        st.session_state["user"] = username
                        st.success("Acceso autorizado")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error("Credenciales incorrectas")
                else:
                    st.error("Completa todos los campos")
        
        # Nota de contacto (sin mostrar credenciales)
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: rgba(255, 255, 255, 0.03); border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1);">
            <p style="margin: 0; color: rgba(255, 255, 255, 0.5); font-size: 0.85rem;">
                Contacta al administrador para obtener las credenciales de acceso
            </p>
        </div>
        """, unsafe_allow_html=True)

def show_dashboard():
    """Dashboard principal con módulos"""
    
    # Header minimalista
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown(f"""
        <div style="padding: 1rem 0;">
            <h2 style="margin: 0; color: #ffffff; font-weight: 300;">BVC Portfolio Suite</h2>
            <p style="margin: 0; color: rgba(255, 255, 255, 0.5); font-size: 0.9rem;">
                Usuario: {st.session_state.get('user', '')}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("Salir", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    st.markdown("---")
    
    # Módulos principales
    st.markdown("### Módulos Disponibles")
    
    # Grid de módulos
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.03); padding: 1.5rem; border-radius: 10px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1); height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <h4 style="color: #ffffff; margin-bottom: 1rem; font-weight: 400;">Ranking de Fondos</h4>
            <p style="color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; margin-bottom: 1rem;">Análisis y ranking de fondos de inversión</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Abrir Ranking de Fondos", key="fondos", use_container_width=True):
            st.markdown("""
            <meta http-equiv="refresh" content="0; url=https://matiasjvd-ranking-fondos-funds-dashboard-oll7la.streamlit.app/" target="_blank">
            """, unsafe_allow_html=True)
            st.success("Redirigiendo a Ranking de Fondos...")
            st.markdown("**[Haz clic aquí si no se abre automáticamente](https://matiasjvd-ranking-fondos-funds-dashboard-oll7la.streamlit.app/)**")
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.03); padding: 1.5rem; border-radius: 10px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1); height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <h4 style="color: #ffffff; margin-bottom: 1rem; font-weight: 400;">Dashboard Macro</h4>
            <p style="color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; margin-bottom: 1rem;">Análisis macroeconómico y mercados</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Abrir Dashboard Macro", key="macro", use_container_width=True):
            st.markdown("""
            <meta http-equiv="refresh" content="0; url=https://dashboard-macro-bvc.streamlit.app/" target="_blank">
            """, unsafe_allow_html=True)
            st.success("Redirigiendo a Dashboard Macro...")
            st.markdown("**[Haz clic aquí si no se abre automáticamente](https://dashboard-macro-bvc.streamlit.app/)**")
    
    with col3:
        st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.03); padding: 1.5rem; border-radius: 10px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1); height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <h4 style="color: #ffffff; margin-bottom: 1rem; font-weight: 400;">Black-Litterman</h4>
            <p style="color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; margin-bottom: 1rem;">Optimización de portfolios avanzada</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Abrir Black-Litterman", key="blacklitterman", use_container_width=True):
            st.markdown("""
            <meta http-equiv="refresh" content="0; url=https://black-litterman-app.streamlit.app/" target="_blank">
            """, unsafe_allow_html=True)
            st.success("Redirigiendo a Black-Litterman...")
            st.markdown("**[Haz clic aquí si no se abre automáticamente](https://black-litterman-app.streamlit.app/)**")
    
    # Enlaces directos como alternativa
    st.markdown("---")
    st.markdown("### Enlaces Directos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("[Ranking de Fondos](https://matiasjvd-ranking-fondos-funds-dashboard-oll7la.streamlit.app/)")
    
    with col2:
        st.markdown("[Dashboard Macro](https://dashboard-macro-bvc.streamlit.app/)")
    
    with col3:
        st.markdown("[Black-Litterman](https://black-litterman-app.streamlit.app/)")

def check_auth():
    """Verificar autenticación"""
    if st.session_state.get("authenticated", False):
        return True
    show_login_page()
    return False

# CSS minimalista
st.markdown("""
<style>
/* Fuentes */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

/* Variables */
:root {
    --primary: #ffffff;
    --secondary: #888888;
    --bg-dark: #0e1117;
    --surface: #1a1a1a;
    --border: rgba(255, 255, 255, 0.1);
}

/* Global */
.stApp {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, var(--bg-dark) 0%, var(--surface) 100%);
}

/* Ocultar elementos */
#MainMenu, footer, header {visibility: hidden;}

/* Inputs */
.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: white;
    padding: 0.75rem;
    font-weight: 300;
}

.stTextInput > div > div > input:focus {
    border-color: rgba(255, 255, 255, 0.3);
    box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.1);
}

/* Botones */
.stButton > button {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: white;
    font-weight: 400;
    padding: 0.75rem 1.5rem;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

/* Responsive */
@media (max-width: 768px) {
    .stColumns {
        flex-direction: column;
    }
}
</style>
""", unsafe_allow_html=True)

# Función principal
def main():
    if check_auth():
        show_dashboard()

if __name__ == "__main__":
    main()