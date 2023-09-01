# Simple example of Diffie Hellman principle

# Alice and Bob agree in public using these numbers
P=23
G=9
print("Alice  --(Let use P=%i and G=%i)--> Bob" % (P,G))


# Alice select a random private key
AlicePriv = 4

# Bob select a random private key
BobPriv = 3

# Alice compute public value
AlicePub = (G^AlicePriv % P)

# Bob compute public value
BobPub = (G^BobPriv % P)

# Alice sends public value
print("Alice  --(%i)--> Bob" % AlicePub)

# Bob sends public value
print("Alice <--(%i)--  Bob" % BobPub)

# Alice compute symmetric key
AliceSecretKey = BobPub^AlicePriv % P
print("Alice computed secret key: %i" % AliceSecretKey)

# Bob compute symmetric key
BobSecretKey = AlicePub^BobPriv % P
print("Bob computed secret key: %i" % BobSecretKey)

