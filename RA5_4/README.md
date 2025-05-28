# RA5_4 - K3s & K9s.

Este repositorio contiene la resolución paso a paso de las actividades propuestas en la unidad RA5.4, relacionadas con la instalación, configuración y validación de entornos Kubernetes ligeros usando K3s y la herramienta de visualización K9s.

## Contenido del repositorio

Cada actividad está documentada en un README.md individual, incluyendo comandos, capturas y verificaciones:

- [RA5_4_1](./RA5_4_1): Instalación de K3s en modo Single-Node + despliegue de nginx + validación con K9s.
- [RA5_4_2](./RA5_4_2): Instalación de K3s en modo HA (Alta Disponibilidad) + despliegue de nginx + validación con K9s.
- [RA5_4_3](./RA5_4_3): Conversión y despliegue de docker-compose en K3s + validación con K9s.

## Herramientas utilizadas
- **K3s**: Kubernetes ligero para entornos con pocos recursos.
- **kubectl**: Herramienta CLI para gestionar recursos Kubernetes.
- **K9s**: Interfaz de terminal para gestionar clústeres Kubernetes.
- **Docker Compose** / `kompose`: Para convertir composiciones Docker en manifiestos de Kubernetes.

## Requisitos previos
- Linux (Ubuntu Server o Desktop recomendado)
- Acceso root o sudo
- Conexión a internet
