SELECT reunion.name, reunion.description, reunion.date, partner.name
FROM crm_meeting reunion
LEFT JOIN crm_case_categ categ ON reunion.id = categ.id
INNER JOIN res_partner partner ON reunion.partner_id = partner.id
WHERE categ.id = 1