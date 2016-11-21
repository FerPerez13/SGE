select DISTINCT cas.name from crm_lead crm
inner join crm_case_categ cas on crm.categ_id=cas.id

