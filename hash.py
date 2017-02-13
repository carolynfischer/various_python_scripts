"""
If memory serves, this locking mechanism relies on a horribly bad cryptographic hash, and you should be able to break it with some rudimentary calculations.
To open these doors, you will need to reverse engineer the hash function it is using. You already managed to steal the details of the algorithm used, and with 
some quiet observation of the guards you find out the results of the hash (the digest). Now to break it.
The function takes a 16 byte input and gives a 16 byte output. It uses multiplication (*), bit-wise exclusive OR (XOR) and modulo (%) to calculate an element of 
the digest based on elements of the input message: 

digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256

For the first element, the value of message[-1] is 0.

For example, if message[0] - 1 and message[1] = 129, then:
For digest[0]:
129*message[0] = 129
129 XOR message[-1] = 129
129 % 256 = 129
Thus digest[0] = 129.

For digest[1]:
129*message[1] = 16641
16641 XOR  message[0] = 16640
16640 % 256 = 0
Thus digest[1] = 0.

Write a function answer(digest) that takes an array of 16 integers and returns another array of 16 that correspond to the unique message that created this digest.
Since each value is a single byte, the values are 0 to 255 for both message and digest.
"""

def answer(digest):
    message = {}
    result = []
    for i, el in enumerate(digest):
        # a ^ b = c
        # c ^ b = a
        # digest[i] ^ (129 * message[i])
        #(message[i-1] XOR x)/129 = message[i]
        if i == 0:
            message[0] = 0
            digest[i] = ( (129 * message[i]) ^ 0) % 256
        else:
            message[i] = digest[i-1]            
            print ("129 * message[i]", 129 * message[i])
            digest[i] = ( (129 * message[i]) ^ message[i-1]) % 256
        result.append(digest[i])

        print "digest {} is {}".format(i, digest[i])
    print message
    return 

if __name__ == "__main__":
    digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
    #digest = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
    print answer(digest)