# 🧩 RA5_1_3 - Pipeline con Docker y Docker Compose

## 🎯 Objetivo

Esta tarea tiene como objetivo construir y ejecutar una **pipeline de CI/CD en Jenkins utilizando Docker**. Se trabajará con un archivo `jenkinsfile.docker` para definir una serie de etapas (stages) que ejecutarán las pruebas del proyecto de Python en contenedores Docker. Además, se creará y usará un archivo `docker-compose.yml` como parte de la integración del flujo.

---

## 🐳 Dockerfile

Crea un archivo `Dockerfile` para construir la imagen del entorno Python:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY RA5_1_1/ ./RA5_1_1/

RUN pip install --no-cache-dir --upgrade pip

CMD ["python3", "-m", "unittest", "RA5_1_1/test_calculator.py"]
```

---

## 🐳 docker-compose.yml

Dine el servicio de prueba:

```dockerfile
version: '3.8'

services:
  calculadora:
    build: .
    container_name: calculadora_test
```

---

## ⚙️ jenkinsfile.docker

Archivo de pipeline con todas las etapas:

```dockerfile
pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKER_IMAGE = 'calculadora:test'
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                git url: 'https://github.com/PPS10219544/RA5_1.git'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE RA5_1_3'
            }
        }

        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run --rm $DOCKER_IMAGE'
            }
        }

        stage('Ejecutar tests en Docker') {
            steps {
                sh 'docker run --rm $DOCKER_IMAGE python3 -m unittest RA5_1_1/test_calculator.py'
            }
        }

        stage('Ejecutar docker-compose') {
            steps {
                dir('RA5_1_3') {
                    sh 'docker-compose up --build --abort-on-container-exit'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline Docker ejecutada correctamente.'
        }
        failure {
            echo 'Error en la pipeline Docker.'
        }
    }
}
```

--- 

## ▶️ ¿Cómo ejecutar esta pipeline?
1. Asegúrate de que Jenkins tenga acceso a Docker:
  - Usa una imagen de Jenkins con Docker in Docker.
  - O comparte el socket Docker (-v /var/run/docker.sock:/var/run/docker.sock) como en este ejemplo.

2. Crea un nuevo proyecto en Jenkins:
  - Tipo: Pipeline
  - Pipeline from SCM
    - Repository URL: https://github.com/PPS10219544/RA5_1.git
    - Script Path: RA5_1_3/jenkinsfile.docker

3. Guarda y haz clic en “Build Now”.

--- 

## 📚 Recursos

- [Jenkins con Docker](https://www.jenkins.io/doc/book/pipeline/docker/)
- [Dockerfile](https://docs.docker.com/engine/reference/builder/)
- [docker-compose](https://docs.docker.com/compose/)
