# Requerimientos del Sistema

## 1. Descripción general
Sistema web para la gestión de inventario, ventas, usuarios y sucursales de una empresa dedicada a la comercialización de productos para animales.

## 2. Objetivo general
Centralizar y optimizar el control de inventario, las ventas y la administración de sucursales mediante una plataforma web segura y escalable.

## 3. Usuarios del sistema
- Administrador general
- Administrador de sucursal
- Vendedor

## 4. Requerimientos funcionales

### 4.1 Autenticación y usuarios
- El sistema debe permitir iniciar sesión con credenciales.
- El sistema debe permitir cerrar sesión.
- El sistema debe gestionar usuarios con diferentes roles.
- El sistema debe restringir accesos según rol.

### 4.2 Sucursales
- El sistema debe permitir registrar sucursales.
- El sistema debe permitir listar sucursales.
- El sistema debe permitir editar datos de sucursales.
- El sistema debe asociar usuarios a una sucursal.

### 4.3 Productos
- El sistema debe permitir registrar productos.
- El sistema debe permitir editar productos.
- El sistema debe permitir listar productos.
- El sistema debe permitir clasificar productos por categoría.
- El sistema debe permitir definir precio de compra y precio de venta.

### 4.4 Inventario
- El sistema debe controlar stock por sucursal.
- El sistema debe registrar entradas y salidas de inventario.
- El sistema debe permitir ajustes de inventario.
- El sistema debe alertar sobre stock mínimo.
- El sistema debe permitir transferencias entre sucursales.

### 4.5 Ventas
- El sistema debe registrar ventas.
- El sistema debe registrar detalle de cada venta.
- El sistema debe asociar la venta a una sucursal.
- El sistema debe asociar la venta a un vendedor.
- El sistema debe calcular subtotales y total.

### 4.6 Clientes
- El sistema puede registrar clientes.
- El sistema puede consultar historial de compras de clientes.

### 4.7 Reportes
- El sistema debe generar reportes de ventas por fecha.
- El sistema debe generar reportes por sucursal.
- El sistema debe generar reportes de productos más vendidos.
- El sistema debe generar reportes de stock bajo.

## 5. Requerimientos no funcionales
- La aplicación debe ser usable desde navegador web.
- La interfaz debe ser clara y fácil de usar.
- El sistema debe ser escalable para múltiples sucursales.
- El sistema debe proteger información sensible.
- El sistema debe mantener trazabilidad de operaciones importantes.

## 6. Reglas de negocio iniciales
- Cada usuario tendrá un rol definido.
- Un vendedor solo podrá registrar ventas según sus permisos.
- El inventario debe manejarse por sucursal, no de forma global.
- Cada venta debe tener al menos un detalle.
- El stock no debe quedar en negativo.