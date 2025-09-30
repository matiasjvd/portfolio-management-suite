# 📊 BVC Portfolio Suite

Sistema integrado de gestión de portfolios para Buena Vista Capital.

## 🚀 Características

- **🔐 Autenticación segura** - Sistema de login con credenciales hasheadas
- **📈 Módulos integrados** - Acceso directo a herramientas especializadas
- **🎨 Interfaz minimalista** - Diseño limpio y profesional
- **📱 Responsive** - Compatible con dispositivos móviles

## 🛠️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd portfolio-management-suite
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   streamlit run landing_page.py --server.port 8503
   ```

4. **Acceder al sistema:**
   - Abrir: http://localhost:8503
   - Contactar al administrador para obtener credenciales

## 📦 Módulos Integrados

### 📈 Ranking de Fondos
Análisis y ranking completo de fondos de inversión con métricas avanzadas.
- **URL:** https://matiasjvd-ranking-fondos-funds-dashboard-oll7la.streamlit.app/

### 🌍 Dashboard Macro
Análisis macroeconómico y seguimiento de mercados globales.
- **URL:** https://dashboard-macro-bvc.streamlit.app/

### ⚫ Black-Litterman
Optimización avanzada de portfolios usando el modelo Black-Litterman.
- **URL:** https://black-litterman-app.streamlit.app/

## 🏗️ Arquitectura

```
portfolio-management-suite/
├── landing_page.py          # Interfaz principal
├── auth_manager.py          # Sistema de autenticación
├── requirements.txt         # Dependencias
├── README.md               # Documentación
├── .gitignore              # Archivos excluidos
└── CREDENCIALES_PRIVADAS.md # Credenciales (privado)
```

## 🔧 Configuración

### Cambiar Puerto
```bash
streamlit run landing_page.py --server.port PUERTO_DESEADO
```

### Modo Producción
```bash
streamlit run landing_page.py --server.port 8080 --server.address 0.0.0.0
```

## 🛡️ Seguridad

- ✅ Credenciales hasheadas con SHA-256
- ✅ No hay credenciales en texto plano en el código
- ✅ Archivo de credenciales excluido del control de versiones
- ✅ Autenticación requerida para acceso

## 📋 Requisitos del Sistema

- Python 3.8+
- Streamlit 1.28.0+
- Conexión a internet (para módulos externos)

## 🚀 Despliegue

### Desarrollo Local
```bash
streamlit run landing_page.py
```

### Servidor de Producción
```bash
streamlit run landing_page.py --server.port 8080 --server.address 0.0.0.0 --server.headless true
```

## 🔍 Solución de Problemas

### Puerto Ocupado
```bash
# Cambiar puerto
streamlit run landing_page.py --server.port 8504
```

### Limpiar Caché
```bash
streamlit cache clear
```

### Reinstalar Dependencias
```bash
pip install -r requirements.txt --force-reinstall
```

## 📞 Soporte

Para obtener:
- **Credenciales de acceso**
- **Soporte técnico**
- **Nuevas funcionalidades**

Contactar al administrador del sistema.

## 📄 Licencia

Uso interno de Buena Vista Capital. Todos los derechos reservados.

---

**Nota:** Este sistema requiere credenciales de acceso. Contactar al administrador para obtener acceso autorizado.