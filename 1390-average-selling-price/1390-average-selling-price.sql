# Write your MySQL query statement below
select p.product_id,IFNULL(round(SUM(p.price*units)/sum(u.units),2),0) as average_price
From prices p
left join unitsSold u
on p.product_id = u.product_id AND
u.purchase_date between p.start_date and p.end_date
group by p.product_id;