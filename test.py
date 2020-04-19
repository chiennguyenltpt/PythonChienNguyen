"""viết chương trình in các số từ 2 đến 100 (số chia hết cho môt và chính nó)
"""
i=2
flag=False# giả định nó không là số nguyên tố
for x in range(2,100):
    if i<=x/2:
        x%i==0
        flag=True
        break
if flag==False:
    print(x)
        
    
