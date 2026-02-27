"""Dado el valor de venta de un producto (49.9), hallar el IVA (16 %) y el precio final de venta."""

valor_venta = 49.9
iva = valor_venta * 0.16
precio_final = valor_venta + iva

print(f"Valor original: {valor_venta}")
print(f"Impuesto (16%): {iva}")
print(f"Total a pagar: {precio_final}")
