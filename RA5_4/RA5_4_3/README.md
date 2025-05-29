# RA5_4_3 - Despliegue de Docker Compose en K3s con balanceo de carga y validación con K9s

## 🎯 Objetivo

Desplegar una aplicación compuesta por un contenedor Flask, Redis y el balanceador de carga **Traefik** usando un manifiesto Kubernetes adaptado desde `docker-compose.yaml`, desplegarlo en un clúster K3s y validar su funcionamiento con K9s.

---

## 📋 Requisitos previos

- K3s o Docker instalado en Ubuntu 22.04
- Acceso con usuario con permisos sudo
- Conexión a Internet
- Navegador Firefox disponible o accesible desde otra máquina

---

## 🛠 Paso 1: Preparar entorno y estructura de archivos

```
~/friendlyhello/
├── app.py
├── Dockerfile
├── requirements.txt
└── docker-compose.yaml
```

Para ello creamos el directorio del proyecto: 

```bash
mkdir -p ~/friendlyhello && cd ~/friendlyhello
```

Y creamos los archivos necesarios: 

### Archivo `app.py`
```python
from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = f"<h3>Hello {os.getenv('NAME', 'world')}!</h3>" \
           f"<b>Hostname:</b> {socket.gethostname()}<br/>" \
           f"<b>Visits:</b> {visits}"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

### Archivo `requirements.txt`
```
Flask
Redis
```

### Archivo `Dockerfile`
```dockerfile
FROM python:3-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "app.py"]
```

### Archivo `docker-compose.yaml`
```yaml
services:
  web:
    build: .
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web.rule=PathPrefix(`/`)"
      - "traefik.http.routers.web.entrypoints=web"
      - "traefik.http.services.web.loadbalancer.server.port=80"

  redis:
    image: redis
    volumes:
      - "./data:/data"
    command: redis-server --appendonly yes
    labels:
      - "traefik.enable=false"

  traefik:
    image: traefik:v2.3
    command:
      - "--log.level=DEBUG"
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedByDefault=false"
      - "--entrypoints.web.address=:4000"
    ports:
      - "4000:4000"
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
```

Actualizamos e instalamos lo necesario para el correcto uso:
```bash
sudo apt update
sudo apt install docker.io
sudo apt install docker
sudo apt install docker-compose
```

---

## 🐳 Paso 2: Construir imagen y probar aplicació

### Construcción manual (opcional):
```bash
sudo docker build -t friendlyhello .
```

### Ejecución directa para pruebas:
```bash
sudo docker run --rm -p 4000:80 friendlyhello
```
> Visita en el navegador: `http://192.168.1.136:4000`

---

## 📦 Paso 3: Despliegue con `docker-compose`

Instalamos `docker-compose` si no está disponible:
```bash
sudo apt update
sudo apt install docker-compose -y
```

### Ejecutamos el despliegue con balanceo:
```bash
sudo docker-compose up -d --scale web=5
```

---

## 🔍 Paso 4: Validar funcionamiento

### Navegador:
- Accedemos a la aplicación: `http://192.168.1.136:4000`
- Dashboard de Traefik: `http://192.168.1.136:8080/dashboard/#/`

> ✅ Si aparece el mensaje de "Hello World!" y el hostname cambia al recargar, ¡el balanceo funciona!

---

## ✅ Conclusión

Se ha desplegado correctamente una aplicación multi-servicio con Flask, Redis y Traefik utilizando `docker-compose`. El balanceo entre instancias funciona correctamente, y Traefik permite monitorizar y enrutar tráfico de forma eficiente. Además, se resolvieron errores comunes relacionados con permisos y configuración del entorno.

---

## 📚 Recursos 

- [Taller Aula Software Libre - Docker y Traefik](https://aulasoftwarelibre.github.io/taller-de-docker/dockerfile/#balanceo-de-carga)
- [Traefik Documentation](https://doc.traefik.io/traefik/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Flask + Redis Example](https://realpython.com/flask-by-example-part-1-project-setup/)

