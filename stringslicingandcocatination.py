st = "Hello yashhigh"
print(st)
print(type(st))
print(st[0])
print(st[4])
print(len(st))
for i in range(len(st)):
    print(st[i])

#slice
print(st[:6])
print(st[4:])
print(st[6:10])
print(st[::2])
print(st[::-1])
print(st[:5:-1])
print(st[4::-1])
print(st[::-1])
print(st[:4:-1])
print(st[3::-1])


# string reversing
cnt=len(st)
lst=""
for i in range(cnt-1,-1,-3):
    lst=lst +st[i]
print(lst)



# Find the duplicate character from the string

lst=""
for i in range(cnt):
    for j in range (i+1,cnt):
        if st[i]==st[j]:
            lst=lst+st[i]
            st=st.replace(str(st[i])," ")
            print(st)
print("duplicate character from string is:-",lst)



# string concatination
st="hello"
st1="Shrikant"
print(st+st1)
print(st,st1)
