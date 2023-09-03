# Simple example of Diffie Hellman algorithm

# Encryption with XOR
def encrypt(m, k):
    c = ""
    for char in m:
        c = c + chr(ord(char) ^ k)
    return c

# Decryption with XOR
def decrypt(c, k):
    m = ""
    for char in c:
        m = m + chr(ord(char) ^ k)
    return m


# In clear text, Alice and Bob agree a multiplicative group of integers with
# P: Prime, and
# G: Generator
# where P is prime and where G is a primitve root modulo P
# In the theory of rings, it is described as the group of units of the ring of integers modulo n. 
# Here units refers to elements with a multiplicative inverse, which, in this ring, are exactly those coprime to n.
P=23
G=9
print("Alice  --( Msg in clear: 'Let use P=%i and G=%i' )--> Bob" % (P,G))

# Alice select a random private key
AlicePriv = 4

# Bob select a random private key
BobPriv = 3

# Alice compute public integer
AlicePub = (G^AlicePriv % P)

# Bob compute public integer
BobPub = (G^BobPriv % P)

# Alice sends public integer
print("Alice  --( Msg in clear: 'Here is my public integer %i' )--> Bob" % AlicePub)

# Bob sends public integer
print("Alice <--( Msg in clear: 'Her is my public integer %i' )--  Bob" % BobPub)

# Alice compute symmetric secret key
AliceSecretKey = BobPub^AlicePriv % P
print("Alice computed secret key: %i" % AliceSecretKey)

# Bob compute symmetric secret key
BobSecretKey = AlicePub^BobPriv % P
print("Bob computed secret key: %i" % BobSecretKey)

# Alice encrypt some text and send to Bob
clearText = "Hi Bob!"
print("Alice encrypt message with her secret key: '%s'" % clearText)
encryptedText = encrypt(clearText, AliceSecretKey)
print("Alice --( Encrypted msg: '%s' )--> Bob" % encryptedText)

# Bob receive encryptet text from Alice and decrypt it with his secret key
receivedClearText = decrypt(encryptedText, BobSecretKey)
print("Bob decrypt message from Alice with his secret key: '%s'" % receivedClearText)


