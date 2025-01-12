
#!/bin/bash

# Configuración inicial
set -euo pipefail # Salir ante cualquier error

# Variables de entorno (puedes definirlas en un archivo .env y cargarlas aquí)
BACKEND_DIR="./src/backend"
FRONTEND_DIR="./src/frontend"
MOBILE_DIR="./src/mobile"
DEPLOYMENT_ENV="${1:-development}" # Entorno de despliegue (development, production, staging, etc.)
CONFIG_DIR="./config"

echo "Desplegando Alphapp en el entorno: ${DEPLOYMENT_ENV}"

# Cargar configuración específica del entorno
if [ -f "${CONFIG_DIR}/${DEPLOYMENT_ENV}.ini" ]; then
  echo "Cargando configuración desde ${CONFIG_DIR}/${DEPLOYMENT_ENV}.ini"
  # Aquí puedes usar source o una herramienta como envsubst para cargar las variables
  # Ejemplo con source (requiere que el .ini tenga formato de variables de entorno):
  # source "${CONFIG_DIR}/${DEPLOYMENT_ENV}.ini"
  # Ejemplo con envsubst (más robusto):
  export $(grep -v '^#' "${CONFIG_DIR}/${DEPLOYMENT_ENV}.ini" | xargs)
else
  echo "Archivo de configuración ${CONFIG_DIR}/${DEPLOYMENT_ENV}.ini no encontrado. Usando configuración por defecto."
fi


# Despliegue del Backend
echo "Desplegando Backend..."
cd "${BACKEND_DIR}" || exit 1 # Cambiar al directorio del backend o salir si falla

# Instalar dependencias
echo "Instalando dependencias del backend..."
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
elif [ -f "package.json" ]; then # Para backends con Node.js
  npm install
fi

# Migraciones de la base de datos (si aplica)
if [ -f "manage.py" ]; then # Para backends con Django
  python manage.py migrate
elif [ -f "alembic.ini" ]; then # Para backends con Alembic (SQLAlchemy)
    alembic upgrade head
fi

# Ejecutar el backend (en un proceso separado o con un gestor de procesos como Gunicorn/PM2)
echo "Iniciando el backend..."
# Ejemplo simple (NO para producción): python app.py &
# Ejemplo con Gunicorn: gunicorn app:app --bind 0.0.0.0:8000 &

cd .. # Volver al directorio raíz

# Despliegue del Frontend
echo "Desplegando Frontend..."
cd "${FRONTEND_DIR}" || exit 1

# Instalar dependencias
echo "Instalando dependencias del frontend..."
if [ -f "package.json" ]; then
  npm install
fi

# Construir el frontend para producción (si es necesario)
if [[ "${DEPLOYMENT_ENV}" == "production" ]]; then
  echo "Construyendo el frontend para producción..."
  npm run build # O el comando de build que uses (ej. yarn build, ng build)
fi

# Copiar archivos estáticos al servidor (si aplica)
# Ejemplo con rsync:
# rsync -avz dist/ usuario@servidor:/ruta/del/servidor/

cd .. # Volver al directorio raíz

# Despliegue de la Aplicación Móvil (si aplica)
if [ -d "${MOBILE_DIR}" ]; then
  echo "Desplegando Aplicación Móvil..."
  cd "${MOBILE_DIR}" || exit 1

  # Dependiendo de la plataforma (Android/iOS) y el método de despliegue,
  # aquí se ejecutarán los comandos correspondientes.
  # Ejemplos:
  # Para Android: ./gradlew assembleRelease
  # Para iOS: xcodebuild ...

  cd .. # Volver al directorio raíz
fi

echo "Despliegue completado."