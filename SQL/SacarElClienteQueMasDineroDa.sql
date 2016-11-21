Select cml.name, cml.planned_revenue, cml.user_id, cml.probability
from crm_lead cml
left join res_partner resp on cml.partner_id = resp.id
left join res_users resu on cml.user_id = resu.id
where cml.priority like '3' and cml.planned_revenue is not null

