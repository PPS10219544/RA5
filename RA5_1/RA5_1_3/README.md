# 🧩 RA5_1_3 - Jenkinsfile con Docker y Docker Compose

## 🎯 Objetivo

En esta tarea se construye una pipeline de Integración Continua (CI) más avanzada que integra:

* Contenedores Docker
* Imágenes personalizadas
* Docker Compose

El objetivo es automatizar el ciclo completo de pruebas del proyecto Python (la calculadora) **dentro de contenedores Docker**, permitiendo mayor portabilidad y aislamiento. Todo el flujo está definido mediante un `jenkinsfile.docker`.

---

## 📁 Estructura del repositorio esperada

```
RA5_1/
├── RA5_1_1/
│   ├── calculadora.py
│   └── test_calculator.py
├── RA5_1_2/
│   └── Jenkinsfile
├── RA5_1_3/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── jenkinsfile.docker
```

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
    agent any

    stages {

        stage('Clonar Repositorio') {
            steps {
                echo 'Repositorio clonado correctamente.'
            }
        }

        stage('Construir Imagen Docker') {
            steps {
                dir('RA5_1_3') {
                    sh 'docker build -t calculadora_test .'
                }
            }
        }

        stage('Ejecutar Contenedor') {
            steps {
                sh 'docker run --rm --name contenedor_calculadora calculadora_test'
            }
        }

        stage('Ejecutar Docker Compose') {
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
            echo 'Fallo en alguna etapa de Docker Pipeline.'
        }
    }
}
```

---

## 🚀 Crear Pipeline en Jenkins

1. En la interfaz Jenkins, haz clic en **Nuevo Item**.
2. Nombre: `calculadora-docker-ci`
3. Tipo: **Pipeline**
4. En configuración:

   * **Pipeline script from SCM**
   * **SCM**: Git
   * **URL**: `https://github.com/PPS10219544/RA5.git`
   * **Branch**: `*/main`
   * **Script Path**: `RA5_1/RA5_1_3/jenkinsfile.docker`

---

## 🧪 Validación y Resultados

* La pipeline debe ejecutar sin errores.
* Se observará la construcción de la imagen, ejecución del contenedor y validación de los test unitarios.

---

## ✅ Conclusión

Con esta tarea se automatiza todo el proceso CI usando Docker y Jenkins. Esta práctica refuerza los conocimientos en:

* Contenedores y pruebas aisladas
* Automatización completa con Jenkins y pipelines declarativas
* Uso de Dockerfile y docker-compose en entornos de CI
 
--- 
 
## 📚 Recursos

- [Jenkins con Docker](https://www.jenkins.io/doc/book/pipeline/docker/)
- [Dockerfile](https://docs.docker.com/engine/reference/builder/)
- [docker-compose](https://docs.docker.com/compose/)
