-- Write your query below
select p.first_name , p.last_name ,a.city , a.state 
from person p  left join address a 
on p.person_id = a.person_id 
