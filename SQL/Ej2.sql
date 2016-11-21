SELECT DISTINCT recursos.name, puestos.name FROM hr_employee empleados
INNER JOIN resource_resource recursos ON empleados.resource_id = recursos.id
LEFT JOIN hr_job puestos ON empleados.job_id = puestos.id