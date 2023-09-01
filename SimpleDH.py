# Simple example of Diffie Hellman principle

def encrypt(m, k):
# XOR encryption
    c = ""
    for char in m:
        c = c + chr(ord(char) ^ k)
    return c

def decrypt(c, k):
    m = ""
    for char in c:
        m = m + chr(ord(char) ^ k)
    return m


# Alice and Bob agree in public using these numbers
# P: Prime
# G: Generator
# The multiplicative group of integers modulo P, where P is prime and where G is a primitve root modulo P
# In the theory of rings, a branch of abstract algebra, it is described as the group of units of the ring of integers modulo n. Here units refers to elements with a multiplicative inverse, which, in this ring, are exactly those coprime to n.
P=23
G=9
print("Alice  --( Let use P=%i and G=%i )--> Bob" % (P,G))


# Alice select a random private key
AlicePriv = 4

# Bob select a random private key
BobPriv = 3

# Alice compute public value
AlicePub = (G^AlicePriv % P)

# Bob compute public value
BobPub = (G^BobPriv % P)

# Alice sends public value
print("Alice  --( Here is my public integer %i )--> Bob" % AlicePub)

# Bob sends public value
print("Alice <--( Her is my public integer %i )--  Bob" % BobPub)

# Alice compute symmetric key
AliceSecretKey = BobPub^AlicePriv % P
print("Alice computed secret key: %i" % AliceSecretKey)

# Bob compute symmetric key
BobSecretKey = AlicePub^BobPriv % P
print("Bob computed secret key: %i" % BobSecretKey)

# Alice encrypt some text and send to Bob
clearText = "Hi Bob!"
print("Alice encrypt message with her secret key: %s" % clearText)
encryptedText = encrypt(clearText, AliceSecretKey)
print("Alice --( %s )--> Bob" % encryptedText)

# Bob receive encryptet text from Alice and decrypt it with his secret key
receivedClearText = decrypt(encryptedText, BobSecretKey)
print("Bob decrypt message from Alice with his secret key: %s" % receivedClearText)


