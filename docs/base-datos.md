# Diseño Inicial de Base de Datos

## 1. Objetivo
Definir las entidades principales del sistema comercial multisucursal.

## 2. Entidades principales

### 2.1 roles
Campos sugeridos:
- id
- nombre
- descripcion
- estado
- created_at
- updated_at

### 2.2 sucursales
Campos sugeridos:
- id
- nombre
- direccion
- telefono
- estado
- created_at
- updated_at

### 2.3 usuarios
Campos sugeridos:
- id
- nombre
- apellido
- email
- password_hash
- rol_id
- sucursal_id
- estado
- created_at
- updated_at

Relaciones:
- muchos usuarios pertenecen a un rol
- muchos usuarios pueden pertenecer a una sucursal

### 2.4 categorias
Campos sugeridos:
- id
- nombre
- descripcion
- estado
- created_at
- updated_at

### 2.5 productos
Campos sugeridos:
- id
- nombre
- descripcion
- codigo_barras
- categoria_id
- precio_compra
- precio_venta
- stock_minimo
- estado
- created_at
- updated_at

### 2.6 inventario_sucursal
Campos sugeridos:
- id
- sucursal_id
- producto_id
- stock_actual
- created_at
- updated_at

Relaciones:
- una sucursal tiene muchos productos en inventario
- un producto puede existir en varias sucursales

### 2.7 movimientos_inventario
Campos sugeridos:
- id
- sucursal_id
- producto_id
- tipo_movimiento
- cantidad
- motivo
- usuario_id
- fecha_movimiento
- created_at
- updated_at

Tipos sugeridos:
- entrada
- salida
- ajuste
- transferencia_entrada
- transferencia_salida

### 2.8 clientes
Campos sugeridos:
- id
- nombre
- apellido
- telefono
- email
- direccion
- estado
- created_at
- updated_at

### 2.9 ventas
Campos sugeridos:
- id
- sucursal_id
- cliente_id
- usuario_id
- fecha_venta
- subtotal
- descuento
- total
- estado
- created_at
- updated_at

### 2.10 detalle_ventas
Campos sugeridos:
- id
- venta_id
- producto_id
- cantidad
- precio_unitario
- subtotal
- created_at
- updated_at

## 3. Relaciones principales
- roles 1 --- n usuarios
- sucursales 1 --- n usuarios
- categorias 1 --- n productos
- sucursales 1 --- n inventario_sucursal
- productos 1 --- n inventario_sucursal
- sucursales 1 --- n ventas
- usuarios 1 --- n ventas
- clientes 1 --- n ventas
- ventas 1 --- n detalle_ventas
- productos 1 --- n detalle_ventas

## 4. Observaciones
- El stock debe manejarse por sucursal.
- La contraseña no debe guardarse en texto plano.
- Los movimientos de inventario deben quedar auditados.
- Las ventas deben descontar stock según sucursal.