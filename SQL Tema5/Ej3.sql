/*Crea una consulta SQL que proporcione los proveedores (identificador y nombre)
 para los que tenemos algún pedido de compra pendiente de recepción, 
acompañados de la referencia y fecha de los pedidos pendientes de recepción.*/

/*SELECT res.id, res.name FROM res_partner res*/
Select * from stock_move
