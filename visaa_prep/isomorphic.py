def are_isomorphic(s,t):
    if len(s)!=len(t):
        return "false"
    s_to_t={}
    t_to_s={}
    for c1,c2 in zip(s,t):
        if c1 in s_to_t:
            if s_to_t[c1]!=c2:
                return "false"
        else:
            if c2 in t_to_s:
                return "false"
            s_to_t[c1]=c2
            t_to_s[c2]=c1
    return "true"
            
n=int(input())
s=input()
t=input()
print(are_isomorphic(s,t))
