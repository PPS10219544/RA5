# RA5.3 — Sistema de Monitorización con Prometheus y Grafana

Este repositorio contiene la evidencia completa del resultado de aprendizaje **RA5.3** correspondiente al módulo de **Ciberseguridad en entornos de las tecnologías de la información**. En esta práctica se implementa un sistema de monitorización basado en **Prometheus**, **Node Exporter** y **Grafana**, aplicando técnicas de detección y visualización de métricas en infraestructuras reales o simuladas.

## 🎯 Objetivos Generales

- Instalar y configurar Prometheus y Node Exporter en un servidor Linux.
- Instalar y configurar Grafana en un cliente Linux con visualización remota de métricas.
- Validar el stack completo a través de dashboards funcionales y capturas de pantalla.
- Demostrar la capacidad de detectar anomalías o monitorizar el estado de una infraestructura mediante herramientas libres.

---

## 📂 Estructura del Proyecto

El proyecto se divide en dos subactividades, cada una contenida en su carpeta respectiva:

### 🔸 [RA5_3_1](./RA5_3_1)

**Descripción**:  
Configuración básica y validación del stack de monitorización utilizando el repositorio y guía de Dinesh Murali.  
Incluye la instalación de Prometheus, Node Exporter y Grafana en una misma máquina o red local.

---

### 🔸 [RA5_3_2](./RA5_3_2)

**Descripción**:  
Despliegue del sistema de monitorización distribuido:
- **Servidor Ubuntu** con Prometheus y Node Exporter.
- **Cliente Ubuntu 24.10** con Grafana que consume remotamente las métricas del servidor.

---

## 🧩 Máquinas y Herramientas Utilizadas

- **Ubuntu Server y Ubuntu Desktop 22.04**
- **Prometheus** — Recolección y almacenamiento de métricas.
- **Node Exporter** — Exportador de métricas del sistema.
- **Grafana** — Plataforma de visualización de datos.

---

## 📚 Recursos

- [Repositorio Prometheus + Grafana](https://github.com/dinesh24murali/example_repo/tree/main/prometheus_grafana_example)
- [Guía paso a paso en Medium](https://medium.com/@dineshmurali/introduction-to-monitoring-with-prometheus-grafana-ea338d93b2d9)
- [Prometheus Documentation](https://prometheus.io/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Ubuntu Server 24.04 LTS](https://ubuntu.com/download/server/thank-you?version=24.04.2&architecture=amd64&lts=true)
