def is_letter(n):
    if n in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' or n in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z':
        waarheid = True
    else:
        waarheid = False
    return waarheid


def roteer_letter(n, k):
    def is_letter(n):
        if n in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' or n in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z':
            waarheid = True
        else:
            waarheid = False
        return waarheid
    if is_letter(n) == True:
        if n in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z':
            if ord(n) + k >= 122:
                return chr((ord(n) + k) - 26)
            else:
                return chr(ord(n) + k)

        elif n in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z':
            if ord(n) + k >= 90:
                return chr((ord(n) + k) - 26)
            else:
                return chr(ord(n)+k)

    else:
        return n


def versleutel(n, k):
        def roteer_letter(n, k):
            def is_letter(n):
                if n in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' or n in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z':
                    waarheid = True
                else:
                    waarheid = False
                return waarheid

            if is_letter(n) == True:
                if n in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z':
                    if ord(ln) + k >= 122:
                        return chr((ord(n) + k) - 26)
                    else:
                        return chr(ord(n) + k)

                elif n in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z':
                    if ord(n) + k >= 90:
                        return chr((ord(n) + k) - 26)
                    else:
                        return chr(ord(n) + k)
            else:
                return n

        zin = ''
        for letter in n:
            zin += roteer_letter(n, k)
        return zin

print(versleutel('H', 20))
print(versleutel('Het leven bestaat voor 10% uit dingen die gebeuren en voor 90% uit hoe jij daarop reageert.', 20))
print(versleutel('Vertrouw op je kracht en vier het leven!',8))