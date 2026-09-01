select u.name, 
sum(CASE WHEN u.id in (select distinct user_id from rides ) THEN r.distance ELSE 0 END) as travelled_distance 
from users u
left join rides r
on u.id=r.user_id
group by r.user_id, u.name
order by travelled_distance desc, name asc 
;