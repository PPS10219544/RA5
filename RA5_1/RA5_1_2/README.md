# 🧩 RA5_1_2 - Creación de una Pipeline de CI para la Calculadora en Python

## 🎯 Objetivo

En esta tarea se define y ejecuta una **pipeline de integración continua** en Jenkins para el proyecto de la calculadora en Python desarrollado en la Tarea 1. Se utilizará un archivo `Jenkinsfile` que describe todas las etapas necesarias del proceso, permitiendo que la ejecución se dispare automáticamente al detectar nuevos commits en el repositorio Git.

El objetivo es implementar el enfoque **"Pipeline as Code"**, asegurando que todo el flujo CI esté versionado, automatizado y sea reproducible.

---

## ⚙️ Jenkinsfile

A continuación se muestra un ejemplo de pipeline declarativa para Jenkins que:

- Realiza `checkout` del código desde GitHub.
- Ejecuta las pruebas unitarias.
- Permite detectar errores automáticamente en las etapas.

```groovy
pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Entorno listo para las pruebas.'
            }
        }

        stage('Pruebas Unitarias') {
            steps {
                sh 'PYTHONPATH=RA5_1/RA5_1_1/ python3 -m unittest test_calculator.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutada correctamente.'
        }
        failure {
            echo 'La pipeline ha fallado. Debes revisar los errores encontrados.'
        }
    }
}
```

---

### ▶️ Ejecución de las pruebas


```bash
python calculadora.py 14 5
python -m unittest test_calculator.py
```
![Prueba_Jenkinsfile](assets/Prueba_Jenkinsfile.png) 

---
 
### 📚 Recursos

- [Guía oficial](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)
- [Jenkins](https://www.jenkins.io)
- [Ejemplos Jenkinsfile)](https://github.com/jenkinsci/pipeline-examples)
