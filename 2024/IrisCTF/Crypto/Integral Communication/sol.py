from pwn import *

context.log_level = 'DEBUG'
io = process(["python3", "chal.py"])

orig_plaintext = b'{"from": "guest", "act": "echo", "msg": "flag"}\x00'
wanted_pt_1 = b'{"from": "admin"'
wanted_pt_2 = b', "act": "flag",'

def recv_data_pt1():

    io.recvuntil("3. Exit\n---------------------------------------------------------------------------")
    io.sendline("1")
    io.recvuntil("Please enter your message:")
    io.sendline("flag")
    results = io.recvuntil("3. Exit\n---------------------------------------------------------------------------").decode()
    iv = results.split('\n')[0][4:]
    cipher = results.split('\n')[1][9:]
    return(iv, cipher)

def recv_data_pt2(iv, cipher):
    io.sendline("2")
    io.recvuntil("IV: ")
    io.sendline(iv)
    io.recvuntil("Command: ")
    io.sendline(cipher)
    results = io.recvuntil("3. Exit\n---------------------------------------------------------------------------").decode()
    return bytes.fromhex(results.split('\n')[0][len("Failed to decode UTF-8: "):])[:16]

def recv_flag(iv, cipher):
    io.sendline("2")
    io.recvuntil("IV: ")
    io.sendline(iv)
    io.recvuntil("Command: ")
    io.sendline(cipher)
    results = io.recvuntil("Congratulations! The flag is: ").decode()
    return results.split('\n')[0][len("Congratulations! The flag is: "):]


def do_xoring(orig_iv, orig_cipher):
    pts = [orig_plaintext[i:i+16] for i in range(0, len(orig_plaintext), 16)]
    cts = [orig_cipher[i:i+16] for i in range(0, len(orig_cipher), 16)]

    """
    e = original_plaintext XOR iv
    new_iv = e XOR wanted_plaintext
    """
    e1 = xor(pts[1], cts[0])
    new_iv1 = xor(e1, wanted_pt_2)
    e2 = xor(pts[0], orig_iv)
    new_iv2 = xor(e2, wanted_pt_1)

    return(new_iv2, new_iv1+orig_cipher[16:])

def main():
    original_iv, original_cipher = recv_data_pt1()
    new_iv, new_ciphertext = do_xoring(bytes.fromhex(original_iv), bytes.fromhex(original_cipher))
    print(" data : ", new_iv.hex(), new_ciphertext.hex())
    unwanted_ct = recv_data_pt2(new_iv.hex(), new_ciphertext.hex())
    e3 = xor(unwanted_ct, new_iv)
    final_iv = xor(e3, wanted_pt_1)
    flag = recv_flag(final_iv.hex(), new_ciphertext.hex())
    print("huiknnjnj: ", flag)
    io.interactive()

if __name__ == "__main__":
    main()