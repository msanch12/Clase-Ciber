# Port Scanner + Banner Grabber

## Descripción General

Este proyecto es una herramienta desarrollada en Python que funciona como Escáner de Puertos y Capturador de Banners con fines educativos en el área de ciberseguridad.

La herramienta analiza un rango de puertos TCP en un sistema objetivo e intenta identificar los servicios que se encuentran ejecutándose en los puertos abiertos.

---

## Funcionalidades

### Escáner de Puertos
- Escanea los puertos del 1 al 200.
- Detecta qué puertos se encuentran abiertos utilizando conexiones TCP mediante sockets.

### Capturador de Banners
- Captura información del servicio que se ejecuta en los puertos abiertos.
- Permite identificar:
  - Servicios en ejecución.
  - Versiones de software.
  - Posibles servicios vulnerables.

### Herramienta Combinada
Al combinar el escaneo de puertos con la captura de banners, el script permite identificar servicios expuestos y versiones de software que podrían requerir una revisión de seguridad.

---

## Cómo Funciona el Código

### 1. Configuración Inicial
- Define:
  - Dirección IP objetivo (ejemplo: `127.0.0.1`)
  - Rango de puertos (1–200)

### 2. Proceso de Escaneo
- Itera a través de cada puerto dentro del rango especificado.
- Crea un socket TCP utilizando:
  - `AF_INET`
  - `SOCK_STREAM`
- Intenta establecer conexión mediante `connect_ex()`.

### 3. Detección de Puertos
- `connect_ex()` devuelve:
  - `0` → El puerto está abierto.
  - Un valor distinto de cero → El puerto está cerrado o filtrado.

### 4. Captura del Banner
- Si un puerto está abierto:
  - El script intenta obtener información del servicio.
  - Utiliza `recv(1024)` para capturar hasta 1 KB de datos enviados por el servicio.
- Se establece un tiempo de espera de 2 segundos para evitar bloqueos en servicios que no responden.

---

## Cómo Ejecutar

```bash
python scanner.py
