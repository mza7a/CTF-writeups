# Integral Communication

## Introduction

> AES CBC Mode encryption.

Advanced Encryption Standard or AES simply, is an algorithm that uses a key to encrypt and decrypt data.

CBC Mode or Cipher Block Chaining uses xor before every block encryption as shown in the following schema

<p align="center"><img src="img/CBC_encryption.png"/></p>

The Plaintext we want to decrypt gets splitted by `block_size` which is often 16 bytes.

The first block gets xored with `IV` before getting encrypted.

Rest of blocks get xored with the previous ciphertext block before getting encrypted.

So as an initial thought, we can change the results of encryption if we can change the `IV`, and that's exactly what we have in this challenge.

## Challenge

Challenge takes an input out of these 3 :
```
1. Create command
2. Run command
3. Exit
```

You can create a command, run it, or exit the program.

By default the payload seted by the system is as the following :
```python
payload = {"from": "guest", "act": "echo", "msg": message}
```

So no matter what we input, the message goes directly to `msg`

In order to get the flag, the payload should look like this :
```python
payload = {"from": "guest", "act": "flag", "msg": message}
```

So instead of `echo` in `act`, we need to change it to `flag`, and it doesn't matter really what's in message.

Note that we can change the `IV` and the `Ciphertext` as we want.

There's a way to do that :
```
Let's say our text is : original_plaintext = "Hello worlds".
But our wanted text is : wanted_plaintext = "Hello AkaSec".
and let's call our iv : IV.

To change the text as we want, we need to apply the following xors :

E(this we create) = ORIGINAL_PLAINTEXT XOR IV
NEW_IV(our new iv) = E XOR WANTED_PLAINTEXT

Thus, if we input the new_iv and the old ciphertext, when it gets decrypted we will get "Hello AkaSec" instead of "Hello worlds"
```

An automated solution for this is the [sol.py](https://github.com/mza7a/CTF-writeups/blob/main/2024/IrisCTF/Crypto/Integral%20Communication/sol.py)

`to add detailed explaination`
