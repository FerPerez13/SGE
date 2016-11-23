Select res.name, empleados.country_id
 From hr_employee empleados
 INNER JOIN res_users res on empleados.id = res.id