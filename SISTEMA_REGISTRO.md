# 🔐 Sistema de Registro y Autenticación - Portfolio Management Suite

## 🎯 **Características Implementadas**

### ✅ **Sistema de Registro Completo**
- **Formulario de registro** elegante y futurista
- **Validación automática** de emails duplicados
- **Almacenamiento seguro** en archivos Excel
- **Notificaciones por email** automáticas al admin

### ✅ **Panel de Administración**
- **Gestión de solicitudes** pendientes
- **Aprobación/Rechazo** con un clic
- **Visualización de usuarios** aprobados
- **Estadísticas del sistema** en tiempo real

### ✅ **Sistema de Autenticación Híbrido**
- **Usuarios predeterminados:** admin, demo
- **Usuarios registrados:** sistema dinámico
- **Contraseñas hasheadas** con SHA-256
- **Sesiones seguras** con Streamlit

### ✅ **Notificaciones por Email**
- **Email al admin** cuando hay nueva solicitud
- **Email al usuario** cuando es aprobado/rechazado
- **Plantillas HTML** profesionales
- **Credenciales automáticas** generadas

## 🚀 **Cómo Funciona**

### **1. Proceso de Registro**
```
Usuario → Formulario Registro → Validación → Base de Datos → Email al Admin
```

### **2. Proceso de Aprobación**
```
Admin → Panel Admin → Aprobar/Rechazar → Email al Usuario → Acceso Habilitado
```

### **3. Proceso de Login**
```
Usuario → Credenciales → Validación → Dashboard → Acceso a Herramientas
```

## 👥 **Tipos de Usuario**

### 🔑 **Administrador (admin)**
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **Permisos:** 
  - Acceso completo al sistema
  - Panel de administración
  - Gestión de usuarios
  - Aprobación de solicitudes

### 🎯 **Demo (demo)**
- **Usuario:** `demo`
- **Contraseña:** `demo123`
- **Permisos:**
  - Acceso a todas las herramientas
  - Sin permisos administrativos

### 👤 **Usuarios Registrados**
- **Usuario:** Su email
- **Contraseña:** Generada automáticamente
- **Permisos:**
  - Acceso a todas las herramientas
  - Sin permisos administrativos

## 📊 **Archivos del Sistema**

### **Archivos Principales:**
- `landing_page.py` - Aplicación principal
- `user_management.py` - Gestión de usuarios
- `email_config.py` - Configuración de emails

### **Archivos de Datos:**
- `pending_users.xlsx` - Solicitudes pendientes
- `approved_users.xlsx` - Usuarios aprobados
- `users_credentials.md` - Documentación de credenciales

### **Archivos de Configuración:**
- `SETUP_EMAIL.md` - Instrucciones de configuración
- `SISTEMA_REGISTRO.md` - Este archivo

## 🔧 **Configuración Inicial**

### **1. Instalar Dependencias**
```bash
pip install streamlit pandas openpyxl
```

### **2. Configurar Email (Opcional)**
- Edita `email_config.py` con tus credenciales
- Sigue las instrucciones en `SETUP_EMAIL.md`

### **3. Ejecutar la Aplicación**
```bash
streamlit run landing_page.py
```

## 🎨 **Interfaz de Usuario**

### **Pantalla de Login/Registro**
- **Tabs elegantes** para Login y Registro
- **Diseño glassmorphism** futurista
- **Validación en tiempo real**
- **Mensajes informativos** claros

### **Dashboard Principal**
- **Navegación superior** con info del usuario
- **Grid de herramientas** con efectos hover
- **Botón de logout** siempre visible
- **Panel de admin** (solo para administradores)

### **Panel de Administración**
- **Solicitudes pendientes** con acciones rápidas
- **Lista de usuarios** aprobados
- **Estadísticas del sistema**
- **Configuración** y ayuda

## 📧 **Sistema de Emails**

### **Tipos de Email:**

#### **1. Notificación al Admin**
- Se envía cuando hay nueva solicitud
- Incluye datos del solicitante
- Diseño profesional HTML

#### **2. Aprobación al Usuario**
- Se envía cuando es aprobado
- Incluye credenciales de acceso
- Instrucciones de uso

#### **3. Rechazo al Usuario**
- Se envía cuando es rechazado
- Incluye motivo (opcional)
- Mensaje profesional

## 🔒 **Seguridad Implementada**

### **Autenticación:**
- ✅ Contraseñas hasheadas (SHA-256)
- ✅ Validación de sesiones
- ✅ Protección contra acceso directo
- ✅ Logout seguro

### **Validación:**
- ✅ Emails únicos
- ✅ Campos obligatorios
- ✅ Formato de email válido
- ✅ Prevención de duplicados

### **Almacenamiento:**
- ✅ Archivos Excel seguros
- ✅ Separación de datos sensibles
- ✅ Backup automático
- ✅ Estructura organizada

## 🎯 **Casos de Uso**

### **Caso 1: Nuevo Usuario**
1. Usuario visita la aplicación
2. Ve que necesita registro
3. Llena formulario en pestaña "Registro"
4. Recibe confirmación de solicitud enviada
5. Admin recibe email de notificación
6. Admin aprueba desde panel
7. Usuario recibe credenciales por email
8. Usuario puede acceder al sistema

### **Caso 2: Usuario Existente**
1. Usuario visita la aplicación
2. Usa sus credenciales en pestaña "Login"
3. Accede directamente al dashboard
4. Puede usar todas las herramientas

### **Caso 3: Administrador**
1. Admin hace login con credenciales admin
2. Ve panel de administración adicional
3. Gestiona solicitudes pendientes
4. Revisa usuarios aprobados
5. Monitorea estadísticas del sistema

## 📈 **Estadísticas y Monitoreo**

### **Métricas Disponibles:**
- 📊 Solicitudes pendientes
- 👥 Usuarios aprobados
- 📈 Total de solicitudes
- 📧 Emails enviados (en logs)

### **Archivos de Seguimiento:**
- `pending_users.xlsx` - Estado de solicitudes
- `approved_users.xlsx` - Historial de aprobaciones
- Logs de Streamlit - Errores y actividad

## 🚀 **Próximas Mejoras**

### **Funcionalidades Planeadas:**
- 🔄 Renovación automática de contraseñas
- 📱 Autenticación de dos factores
- 🎨 Temas personalizables
- 📊 Dashboard de analytics avanzado
- 🔗 Integración con bases de datos
- 🌐 API REST para gestión externa

### **Mejoras de Seguridad:**
- 🔐 Encriptación de archivos
- 🕒 Expiración de sesiones
- 🚫 Rate limiting
- 📝 Logs de auditoría
- 🔍 Detección de anomalías

## 🎉 **¡Sistema Listo!**

Tu Portfolio Management Suite ahora tiene:
- ✅ **Autenticación completa** y segura
- ✅ **Sistema de registro** profesional
- ✅ **Panel de administración** funcional
- ✅ **Notificaciones automáticas** por email
- ✅ **Interfaz futurista** y elegante

**¡Disfruta tu nueva plataforma de gestión de portafolios!** 🚀📊💼