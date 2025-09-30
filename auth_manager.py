# Sistema de Autenticación Simplificado
# Credenciales configuradas de forma privada

import streamlit as st
import hashlib

class AuthManager:
    def __init__(self):
        # Credenciales hasheadas para mayor seguridad
        # Contactar al administrador para obtener las credenciales
        self._valid_username_hash = "f6f6900fa783b8c0d0fcaad9a4578fed19a1cfc839f2705f82401c3e4be147c7"
        self._valid_password_hash = "85b1b589385c776bb6198bea809ef15c5bbef8827ea9f8c87a30f0281c5d1ee2"
        
    def _hash_credential(self, credential):
        """Hash de credencial para comparación segura"""
        return hashlib.sha256(credential.encode()).hexdigest()
        
    def authenticate(self, username, password):
        """Autentica usuario con credenciales hasheadas"""
        username_hash = self._hash_credential(username)
        password_hash = self._hash_credential(password)
        
        if username_hash == self._valid_username_hash and password_hash == self._valid_password_hash:
            return True, "Acceso autorizado"
        else:
            return False, "Credenciales incorrectas"
    
    def get_user_role(self, username):
        """Todos los usuarios autenticados tienen acceso completo"""
        return "user"