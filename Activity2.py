def match_words(word):
    count=0
    list1=[]
    for i in word:
        if len(i)>2 and i[0]==i[-1]:
            count=count+1
            list1.append(i)
    print(list1)
    return count
count1=match_words(["abc","attma","hsh","lal","kak","rrrrrrrrrryr"])
print(count1)