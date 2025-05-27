# Stack de Monitorización con Prometheus y Grafana

Este repositorio contiene el paso a paso para la implementación de un sistema de monitorización usando **Prometheus**, **Node Exporter** y **Grafana**, validando su instalación y configuración para el seguimiento de un servidor remoto.

## 📌 Requisitos Previos

- Dos máquinas con Ubuntu:
  - **Servidor Ubuntu Server**: Instalar `prometheus` y `node_exporter`
  - **Cliente Ubuntu 24.10**: Instalar `grafana` y configurar el dashboard

- Acceso root o privilegios sudo en ambas máquinas
- Conectividad entre cliente y servidor

---

## 🔧 1. Instalación de Node Exporter y Prometheus en el Servidor

### Paso 1: Crear usuario Prometheus
```bash
sudo useradd --no-create-home --shell /bin/false prometheus
```

### Paso 2: Descargar Prometheus
```bash
wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-*.tar.gz
tar -xvf prometheus-*.tar.gz
cd prometheus-*/
```

### Paso 3: Mover binarios
```bash
sudo mv prometheus promtool /usr/local/bin/
sudo mkdir /etc/prometheus /var/lib/prometheus
sudo mv consoles/ console_libraries/ prometheus.yml /etc/prometheus/
```

### Paso 4: Crear servicio systemd para Prometheus
```ini
# /etc/systemd/system/prometheus.service
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/var/lib/prometheus

[Install]
WantedBy=default.target
```

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable --now prometheus
```

### Paso 5: Instalar Node Exporter
```bash
wget https://github.com/prometheus/node_exporter/releases/latest/download/node_exporter-*.tar.gz
tar -xvzf node_exporter-*.tar.gz
cd node_exporter-*/
sudo mv node_exporter /usr/local/bin/
```

### Paso 5: Instalar Node Exporter
```ini
# /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter

[Service]
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=default.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now node_exporter
```

---

## 🧭 2. Instalación de Grafana en el Cliente

### Paso 1: Añadir repositorio
```bash
sudo apt install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
sudo apt-get install -y grafana
```

### Paso 2: Iniciar y habilitar Grafana
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now grafana-server
```

Accedemos a Grafana: `http://localhost:3000`
Usuario: **admin**
Contraseña: **admin** (se pide cambiarla en el primer inicio)

---

## 📈 3. Configuración del Dashboard

### Paso 1: Añadir Prometheus como fuente de datos

















