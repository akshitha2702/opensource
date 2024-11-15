x=int(input())
flat_discount=100
per_dis=0.1*x
max_discount=max(flat_discount,per_dis)
final_amount=x-max_discount
print(int(final_amount))
