# RA5_4_2 - Instalación de K3s en HA + nginx + K9s

## Objetivo

Instalar un clúster K3s en alta disponibilidad (HA) usando `etcd` embebido, desplegar NGINX con 2 réplicas y verificar el estado con K9s.

---

## 🧩 Escenario recomendado
- 3 nodos (máquinas virtuales o físicas) con Ubuntu 20.04 o superior.
- Red común entre ellos
- Acceso SSH o físico con permisos sudo

---

## Paso 1: Preparar todos los nodos

### En todos los nodos:
```bash
sudo apt update && sudo apt upgrade -y
```

---

## Paso 2: Instalar el nodo inicial (Ubuntu Desktop 22.04)

### En el primer nodo:
```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--cluster-init" sh -
```

> Este nodo inicia el clúster con etcd embebido.

Obtenemos el token:
```bash
sudo cat /var/lib/rancher/k3s/server/node-token
```
 
![NodeToken](./assets/NodeToken.png)

Obtenemos su IP para conectarlo desde otros nodos:
```bash
ip a | grep inet
```

---

## Paso 3: Añadir más nodos al plano de control (Ubuntu Server 2 y 3)

### En los demás nodos:
```bash
curl -sfL https://get.k3s.io | K3S_URL="https://<IP-PRIMER-NODO>:6443" K3S_TOKEN="<TOKEN>" sh -
```

> Reemplaza `<IP-PRIMER-NODO>` y `<TOKEN>` por los valores obtenidos.

---

## Paso 4: Verificar estado del clúster

En cualquiera de los nodos:
```bash
sudo kubectl get nodes
```

---

## Paso 5: Desplegar servicio NGINX

```bash
kubectl create deployment nginx --image=nginx
kubectl scale deployment nginx --replicas=2
kubectl expose deployment nginx --port=80 --type=NodePort
```

### Verificar:
```bash
kubectl get pods
kubectl get svc
```

---

## Paso 6: Instalar y usar K9s

```bash
curl -sS https://webinstall.dev/k9s | bash
k9s
```

### Verifica:
- El estado de los 3 nodos
- Los pods de nginx corriendo en diferentes nodos

---

## Validación final

- K3s corriendo en HA (3 nodos `Ready`)
- NGINX funcionando con 2 réplicas
- Visualización y navegación de recursos con K9s

---

## Capturas recomendadas para entrega
- Salida de `kubectl get nodes` (3 nodos en Ready)
- Salida de `kubectl get pods`
- K9s mostrando los pods distribuidos
- Servicio NGINX expuesto funcionando

---

## ✅ Conclusión
