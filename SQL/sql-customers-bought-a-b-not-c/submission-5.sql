with cte as  (
    select customer_id
    from orders 
    group by customer_id
    having count(case when product_name = 'A' then 1 end) > 0  and 
           count(case when product_name = 'B' then 1 end) > 0 and
           count(case when product_name = 'C' then 1 end) = 0
)

select *
from customers 
where customer_id in (select customer_id 
                      from cte)
order by customer_name;