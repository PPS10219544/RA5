# RA5_4_1 - Instalación de K3s en Single-Node + nginx + K9s

## Objetivo

Instalar y configurar un clúster K3s en un solo nodo, desplegar un servicio NGINX con 2 réplicas y validar su funcionamiento utilizando la herramienta K9s.

---

## Paso 1: Preparar el entorno

### Requisitos:
- Sistema operativo: Ubuntu Server/Desktop 20.04 o superior
- Acceso con usuario con permisos sudo
- Conexión a internet activa

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Paso 2: Instalar K3s (modo Single-Node)

```bash
curl -sfL https://get.k3s.io | sh -
```

> Esto instalará K3s y creará el archivo de configuración en `/etc/rancher/k3s/k3s.yaml`

### Verificar estado del servicio:
```bash
sudo systemctl status k3s
```

---

## Paso 3: Configurar kubectl

```bash
mkdir -p $HOME/.kube
sudo cp /etc/rancher/k3s/k3s.yaml $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### Verificar conexión:
```bash
kubectl get nodes
```

---

## Paso 4: Desplegar servicio NGINX con 2 réplicas

```bash
kubectl create deployment nginx --image=nginx
kubectl scale deployment nginx --replicas=2
```

### Exponer servicio (opcional):
```bash
kubectl expose deployment nginx --port=80 --type=NodePort
```

### Verificar:
```bash
kubectl get pods
kubectl get svc
```

---

## Paso 5: Instalar K9s

```bash
curl -sS https://webinstall.dev/k9s | bash
```

> O descarga manualmente desde https://github.com/derailed/k9s/releases

### Ejecutar:
```bash
k9s
```

### En K9s puedes:
- Navegar por los pods
- Ver logs
- Monitorizar el estado del clúster

---

## Paso 6: Validación final

1. Verifica que los 2 pods de nginx estén en estado `Running`.
2. Accede al servicio NGINX desde el navegador si está expuesto.
3. Observa los recursos desde K9s.

---

## Capturas recomendadas para entrega
- Salida de `kubectl get nodes`
- Salida de `kubectl get pods`
- Vista de K9s mostrando los pods en ejecución
- Servicio NGINX accesible (captura del navegador o `curl`)

---

## ✅ Conclusión

