# 🧪 RA5_1_2 - Jenkins CI Pipeline para Calculadora Python

## 🎯 Objetivo

El objetivo de esta tarea es poner en práctica el enfoque de Integración Continua (CI) mediante la automatización del proceso de pruebas de un proyecto en Python utilizando Jenkins. Para ello, se implementará una pipeline declarativa descrita en un archivo Jenkinsfile, que será gestionada desde el propio repositorio Git del proyecto. 
 
La canalización debe ejecutarse de forma automática cada vez que se realicen cambios (commits) en el código, permitiendo:
- Detectar errores de manera temprana.
- Asegurar que las pruebas unitarias se ejecuten correctamente.
- Verificar la estabilidad del proyecto tras cada actualización.
 
De este modo, se afianza el principio de "Pipeline as Code", donde toda la lógica de construcción y prueba del software es mantenida de forma versionada, transparente y reproducible. 
 
--- 
 
## 🛠️ Preparativos

### 📁 Estructura esperada del repositorio

```
RA5/
├── RA5_1_1/
│   ├── calculadora.py
│   └── test_calculator.py
├── RA5_1_2/
│   └── Jenkinsfile
```

### 📌 Código de [`calculadora.py`](../RA5_1_1/calculadora.py)

### 📌 Código de [`test_calculator.py`](../RA5_1_1/test_calculator.py)

---

## 📜 [Jenkinsfile](./Jenkinsfile)

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
                sh 'PYTHONPATH=RA5_1/RA5_1_1/ python3 -m unittest test_calculator'
            }
        }
    }

    post {
        success {
            echo 'La pipeline se ha ejecutado correctamente.'
        }
        failure {
            echo 'La pipeline ha fallado. Debes revisar los errores encontrados.'
        }
    }
}
```

---

## 🚀 Cómo crear la pipeline en Jenkins

### 1. Crea una nueva tarea (New Item)

* Nombre: `calculadora-ci`
* Tipo: **Pipeline**

### 2. Configura la pipeline con Git

* **Definition**: `Pipeline script from SCM`
* **SCM**: Git
* **Repository URL**: `https://github.com/PPS10219544/RA5.git`
* **Branch Specifier**: `*/main`
* **Script Path**: `RA5_1_2/Jenkinsfile`

### 3. Guarda y haz clic en **“Build Now”** para ejecutarla

---

## 🐍 Instalar Python en Jenkins (si es necesario)

Si el contenedor Jenkins no tiene `python3`, entra como root:

```bash
sudo docker exec -u 0 -it jenkins bash
apt update
apt install -y python3 python3-pip
exit
```

---

## 🧪 Resultado esperado

* Al ejecutar correctamente, los tests se mostrarán como pasados en la consola.
* Si algo falla (como un test incorrecto), Jenkins marcará el pipeline como fallido.

### 📸 Ejemplo visual:

✅ Ejecución correcta:

```
Ran 3 tests in 0.001s

OK
```

❌ Ejecución fallida:

```
AttributeError: module 'test_calculator' has no attribute 'py'
```

(Solucionado eliminando `.py` del comando en Jenkinsfile).

---

## ✅ Conclusión

Esta tarea demuestra cómo integrar un proyecto en Python con Jenkins usando pipelines declarativas y pruebas automatizadas, controladas por cambios en Git. Además, se aprendió a corregir errores comunes relacionados con entornos, rutas y ejecución de scripts de test.

--- 
 
## 📚 Recursos

- [Guía oficial](https://psegarrac.github.io/Ciberseguridad-PePS/tema5/cd/ci/2022/01/13/jenkins.html#tareas)
- [Jenkins](https://www.jenkins.io)
- [Ejemplos Jenkinsfile](https://github.com/jenkinsci/pipeline-examples)
