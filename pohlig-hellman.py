#A Script for the Pohlig-Hellman algorithm
#Output looks like it has been solved by hand (Gives idea of hand computation)
#Given 3^x = 22 mod 31
# Alpha = 3, beta = 22, modulo = 31, phi = totient function = 30

def Gcd(a,b):
    if a>b:
        a,b=b,a
        print('Next time, let the first argument be > the second argument, dumbass. The answer is still right though') 
    if a<0 or b<0:
        return 'both a and b must be positive'
    if isinstance(a,int)==True and isinstance(b,int)==True:
        while a!=0:
            a,b=b%a,a
        return b 
    else:
        return 'both a and b must be integers'

alpha = int(input('Enter the alpha val: '))
beta = int(input('Enter the beta val: '))
modulo = int(input('Enter the modulo: '))
phi = int(input('Enter the phi val: '))

for i in range(2,21):
    if (phi)%i == 0 and Gcd(i,int(phi/i))==1:
        first_phi = i
        second_phi = int(phi/first_phi)
        break 
second_phi = int(phi/first_phi)
'''first_phi = 2
second_phi = 15'''
parts = [first_phi, second_phi]
print(parts)

multi_rem = []
for i in range(len(parts)): 
    print(f"x = a_0 + {parts[i]}a_1")
    r = phi/parts[i] 
    print(f"{alpha}^{r}*a_0 = {beta}^{r} mod {modulo}")
    for j in range(2,modulo):
        if pow(pow(alpha,r)%modulo,j)%modulo == pow(beta,r)%modulo: 
            fr_remainder = j
            print(f"x = {j} modulo {parts[i]} ----------{i+1}",end='\n\n')
            multi_rem.append(j*parts[(i+1)%2])
            break 

print(f"{second_phi+first_phi}x = {sum(multi_rem)} mod {phi}")
print(f"Using the Chinese Remainder Theorem")
print(f"x = {sum(multi_rem) * pow(second_phi+first_phi,-1,phi)%phi}")
