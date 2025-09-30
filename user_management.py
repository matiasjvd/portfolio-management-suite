import pandas as pd
import hashlib
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import secrets
import string
from email_config import *

class UserManager:
    def __init__(self):
        self.pending_file = "/Users/matias/Desktop/Proyectos/portfolio-management-suite/pending_users.xlsx"
        self.approved_file = "/Users/matias/Desktop/Proyectos/portfolio-management-suite/approved_users.xlsx"
        self.init_files()
    
    def init_files(self):
        """Inicializar archivos de usuarios si no existen"""
        # Archivo de usuarios pendientes
        if not os.path.exists(self.pending_file):
            df_pending = pd.DataFrame(columns=[
                'name', 'email', 'request_date', 'status', 'admin_notes'
            ])
            df_pending.to_excel(self.pending_file, index=False)
        
        # Archivo de usuarios aprobados
        if not os.path.exists(self.approved_file):
            df_approved = pd.DataFrame(columns=[
                'name', 'email', 'password_hash', 'role', 'approval_date', 'approved_by'
            ])
            df_approved.to_excel(self.approved_file, index=False)
    
    def hash_password(self, password):
        """Hash a password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def generate_password(self, length=12):
        """Generar una contraseña segura aleatoria"""
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    
    def send_email(self, to_email, subject, html_content):
        """Enviar email usando SMTP"""
        try:
            # Crear mensaje
            msg = MIMEMultipart('alternative')
            msg['From'] = ADMIN_EMAIL
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Agregar contenido HTML
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            
            # Enviar email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(ADMIN_EMAIL, ADMIN_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            return True, "Email enviado exitosamente"
        except Exception as e:
            return False, f"Error enviando email: {str(e)}"
    
    def register_user_request(self, name, email):
        """Registrar una nueva solicitud de usuario"""
        try:
            # Verificar si el email ya existe
            if self.email_exists(email):
                return False, "Este email ya está registrado o tiene una solicitud pendiente"
            
            # Cargar usuarios pendientes
            df_pending = pd.read_excel(self.pending_file)
            
            # Crear nueva solicitud
            new_request = {
                'name': name,
                'email': email,
                'request_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'status': 'pending',
                'admin_notes': ''
            }
            
            # Agregar a DataFrame
            df_pending = pd.concat([df_pending, pd.DataFrame([new_request])], ignore_index=True)
            df_pending.to_excel(self.pending_file, index=False)
            
            # Enviar notificación al admin
            admin_email_content = get_admin_notification_template(new_request)
            email_sent, email_msg = self.send_email(
                ADMIN_EMAIL, 
                EMAIL_SUBJECT_NEW_REQUEST, 
                admin_email_content
            )
            
            if email_sent:
                return True, "Solicitud enviada exitosamente. Recibirás una respuesta por email."
            else:
                return True, f"Solicitud registrada, pero hubo un problema enviando la notificación: {email_msg}"
                
        except Exception as e:
            return False, f"Error registrando solicitud: {str(e)}"
    
    def email_exists(self, email):
        """Verificar si un email ya existe en el sistema"""
        try:
            # Verificar en usuarios pendientes
            df_pending = pd.read_excel(self.pending_file)
            if email in df_pending['email'].values:
                return True
            
            # Verificar en usuarios aprobados
            df_approved = pd.read_excel(self.approved_file)
            if email in df_approved['email'].values:
                return True
            
            return False
        except:
            return False
    
    def get_pending_requests(self):
        """Obtener todas las solicitudes pendientes"""
        try:
            df_pending = pd.read_excel(self.pending_file)
            return df_pending[df_pending['status'] == 'pending']
        except:
            return pd.DataFrame()
    
    def approve_user(self, email, approved_by="admin"):
        """Aprobar un usuario y crear sus credenciales"""
        try:
            # Cargar usuarios pendientes
            df_pending = pd.read_excel(self.pending_file)
            user_row = df_pending[df_pending['email'] == email]
            
            if user_row.empty:
                return False, "Usuario no encontrado en solicitudes pendientes"
            
            user_data = user_row.iloc[0]
            
            # Generar contraseña
            password = self.generate_password()
            password_hash = self.hash_password(password)
            
            # Cargar usuarios aprobados
            df_approved = pd.read_excel(self.approved_file)
            
            # Crear nuevo usuario aprobado
            new_user = {
                'name': user_data['name'],
                'email': user_data['email'],
                'password_hash': password_hash,
                'role': 'user',
                'approval_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'approved_by': approved_by
            }
            
            # Agregar a usuarios aprobados
            df_approved = pd.concat([df_approved, pd.DataFrame([new_user])], ignore_index=True)
            df_approved.to_excel(self.approved_file, index=False)
            
            # Actualizar estado en pendientes
            df_pending.loc[df_pending['email'] == email, 'status'] = 'approved'
            df_pending.to_excel(self.pending_file, index=False)
            
            # Enviar email de aprobación
            approval_data = {
                'name': user_data['name'],
                'email': user_data['email'],
                'password': password
            }
            
            approval_email_content = get_approval_template(approval_data)
            email_sent, email_msg = self.send_email(
                user_data['email'], 
                EMAIL_SUBJECT_APPROVAL, 
                approval_email_content
            )
            
            if email_sent:
                return True, f"Usuario aprobado exitosamente. Credenciales enviadas por email."
            else:
                return True, f"Usuario aprobado, pero hubo un problema enviando el email: {email_msg}"
                
        except Exception as e:
            return False, f"Error aprobando usuario: {str(e)}"
    
    def reject_user(self, email, reason="", rejected_by="admin"):
        """Rechazar una solicitud de usuario"""
        try:
            # Cargar usuarios pendientes
            df_pending = pd.read_excel(self.pending_file)
            user_row = df_pending[df_pending['email'] == email]
            
            if user_row.empty:
                return False, "Usuario no encontrado en solicitudes pendientes"
            
            user_data = user_row.iloc[0]
            
            # Actualizar estado en pendientes
            df_pending.loc[df_pending['email'] == email, 'status'] = 'rejected'
            df_pending.loc[df_pending['email'] == email, 'admin_notes'] = reason
            df_pending.to_excel(self.pending_file, index=False)
            
            # Enviar email de rechazo
            rejection_data = {
                'name': user_data['name'],
                'email': user_data['email']
            }
            
            rejection_email_content = get_rejection_template(rejection_data, reason)
            email_sent, email_msg = self.send_email(
                user_data['email'], 
                EMAIL_SUBJECT_REJECTION, 
                rejection_email_content
            )
            
            if email_sent:
                return True, "Usuario rechazado. Notificación enviada por email."
            else:
                return True, f"Usuario rechazado, pero hubo un problema enviando el email: {email_msg}"
                
        except Exception as e:
            return False, f"Error rechazando usuario: {str(e)}"
    
    def get_all_users(self):
        """Obtener todos los usuarios aprobados"""
        try:
            df_approved = pd.read_excel(self.approved_file)
            return df_approved
        except:
            return pd.DataFrame()
    
    def authenticate_user(self, email, password):
        """Autenticar un usuario"""
        try:
            df_approved = pd.read_excel(self.approved_file)
            user_row = df_approved[df_approved['email'] == email]
            
            if user_row.empty:
                return False, None
            
            user_data = user_row.iloc[0]
            password_hash = self.hash_password(password)
            
            if user_data['password_hash'] == password_hash:
                return True, {
                    'name': user_data['name'],
                    'email': user_data['email'],
                    'role': user_data['role']
                }
            else:
                return False, None
                
        except Exception as e:
            return False, None