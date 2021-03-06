with open('nonces.log') as f:
    nonces = f.readlines()

max_len = 163 # very rare

lengths = {}
total = 0

for nonce in nonces:
    total += 1
    bin_nonce = bin(int(nonce))[2:]
    nonce_len = len(bin_nonce)
    if nonce_len in lengths:
        lengths[nonce_len] += 1
    else:
        lengths[nonce_len] = 1

keylist = lengths.keys()
keylist.sort()

print "%s\t/%s\t%s" % ("length", total, "percentage")

for length in keylist:
    amount = lengths[length]
    percentage = int(amount * 100 / total)
    print "%s\t%s\t%i" % (length, amount, percentage)
