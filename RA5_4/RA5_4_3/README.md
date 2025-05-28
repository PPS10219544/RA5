# RA5_4_3 - Despliegue de docker-compose convertido + K9s

## Objetivo

Desplegar un servicio con balanceo de carga definido en Docker Compose dentro de un clúster K3s, convirtiéndolo a manifiestos Kubernetes mediante `kompose`, y validarlo con K9s.

---

## Paso 1: Requisitos previos
- Clúster K3s funcional (Single-Node o HA)
- `kubectl` configurado
- K9s instalado
- `kompose` instalado:

```bash
sudo curl -L https://github.com/kubernetes/kompose/releases/download/v1.31.2/kompose-linux-amd64 -o /usr/local/bin/kompose
sudo chmod +x /usr/local/bin/kompose
```

---

## Paso 2: Obtener el docker-compose

```bash
mkdir k3s-docker-compose
cd k3s-docker-compose
wget https://raw.githubusercontent.com/aulasoftwarelibre/taller-de-docker/master/docker-compose/load-balancer/docker-compose.yml
```

---

## Paso 3: Convertir a manifiestos Kubernetes

```bash
kompose convert
```

> Esto generará archivos `.yaml` compatibles con K3s.

---

## Paso 4: Desplegar los manifiestos

```bash
kubectl apply -f .
```

Verificar:
```bash
kubectl get all
```

---

## Paso 5: Validación con K9s

```bash
k9s
```

Desde K9s:
- Verifica que los pods estén corriendo
- Examina los servicios expuestos
- Observa logs y recursos

---

## Capturas recomendadas para entrega
- Archivos generados por `kompose`
- `kubectl get pods` mostrando los servicios en ejecución
- Vista en K9s con pods corriendo
- Prueba del servicio accediendo a la IP:puerto

---

## ✅ Conclusión

