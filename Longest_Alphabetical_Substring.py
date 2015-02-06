s = 'zyxwvutsrqponmlkjihgfedcba'
i = 0;
long_str ='';
longest ='';

for a in s:
    print(a, i, len(s))
    if i+1<len(s):
        if s[i]<= s[i+1]:
            if(long_str==''):
                long_str+=s[i]+s[i+1]
            else:
                long_str += s[i+1]
        else:
            long_str ='';
        if(len(long_str)>len(longest)):
            longest = long_str
        print(s[i],long_str, longest)
    if longest=='':
        longest=s[0]
    i+=1;
print("Longest substring in alphabetical order is:"+longest);

#for(i=0; i<=len(s); i++)
#    if(s[i]<s[i+1])
#        long_str +=s[i];