-- Write your query below
select c.name 
from customers c left join orders o 
on c.id = o.customer_id
where o.customer_id is null
