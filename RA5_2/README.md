# RA5.2 - Automatización de Infraestructura con Vagrant y Ansible

Este repositorio demuestra cómo implementar **Infrastructure as Code (IaC)** para desplegar y configurar automáticamente una máquina virtual Ubuntu 24.04 LTS utilizando **Vagrant** y **Ansible**.

---

## 📦 Requisitos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:

- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)
- [Ansible](https://www.ansible.com/)

---

## 🔧 Paso 1: Provisionar Ubuntu 24.04 con Vagrant

El archivo `Vagrantfile` define la creación de una máquina virtual con Ubuntu 24.04.

### ✅ Instrucciones

```bash
vagrant up
```
---

## ⚙️ Paso 2: Configurar la VM con Ansible (playbook.yml)

Este `playbook.yml` realiza:
 - La actualización del sistema (`apt update && apt upgrade`).
 - La instalación del servidor Apache.

### ✅ Instrucciones

```bash
ansible-playbook -i provision/hosts.ini provision/playbook.yml
```
---

## 📝 Paso 3: Añadir index.html y verificar con curl (index.yml)

Este `playbook.yml` realiza:
 - Crea un archivo `index.html` con el texto “Ansible rocks”.
 - Reinicia el servicio Apache.
 - Verifica la respuesta con `curl`.



