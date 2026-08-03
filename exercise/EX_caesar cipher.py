from operator import index

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(name,shift):
    word=""
    name=list(name)
    for i in name:
        if i in alphabets:
            n=alphabets.index(i)
            a=(n+shift)%26
            i=alphabets[a]
            word+=i
    print(f"your encrypted word is:{word}")
encryption("hello jenny",3)
def decryption(name,shift):
    word=""
    word1=""
    names= list(name)
    s_alphabets=set(alphabets)
    s_names=set(name)
    if s_names.intersection(s_alphabets)==set():
        for i in names:
            n = alphabets.index(i)
            a = (n - shift)
            if 0>a :
                a+=26
                a%=26
            else:a%=26
            i = alphabets[a]
            word+=i
    if  s_names.intersection(s_alphabets) != alphabets:
        shape=s_names.intersection(s_alphabets)
        # b = name.split(shape)
        # for v in range(len(b)):
        #     for i in b[v]:
        #         n = alphabets.index(i)
        #         a = (n - shift)
        #         if 0 > a:
        #             a += 26
        #             a %= 26
        #         else:a %= 26
        #         i = alphabets[a]
        #         word1 += i
        #     v=word1
        #     print(b)
        #
        #     word+=word1
        print(shape)
    print(f"your decrypted word is:{word}")
decryption("khoor mhqqb",3)