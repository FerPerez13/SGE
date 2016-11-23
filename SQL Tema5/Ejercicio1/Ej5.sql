SELECT producto.name AS "Nombre", producto.purchase_ok AS "Proveedor" 
FROM product_supplierinfo info
INNER JOIN res_partner proveedor ON info.id = proveedor.id
RIGHT JOIN product_template producto ON producto.id = info.id
WHERE producto.purchase_ok = TRUE