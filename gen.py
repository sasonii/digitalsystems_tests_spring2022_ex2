import random


def main():
    f = open("MultInputVector.txt", "w")
    for i in range(32):
        rnd_32bit_a = random.getrandbits(32)
        rnd_32bit_b = random.getrandbits(32)
        a = (34 - len(bin(rnd_32bit_a))) * "0" + bin(rnd_32bit_a)[2:]
        b = (34 - len(bin(rnd_32bit_b))) * "0" + bin(rnd_32bit_b)[2:]
        mult = bin(rnd_32bit_a * rnd_32bit_b)
        mult64 = (66 - len(mult)) * "0" + mult[2:]
        f.writelines(f"{a}_{b}_{mult64}\n")
    f.close()

    f = open("FastMultInputVector.txt", "w")
    for i in range(32):
        rnd_16bit_a = random.getrandbits(16)
        rnd_16bit_b = random.getrandbits(16)
        a = (34 - len(bin(rnd_16bit_a))) * "0" + bin(rnd_16bit_a)[2:]
        b = (34 - len(bin(rnd_16bit_b))) * "0" + bin(rnd_16bit_b)[2:]
        mult = bin(rnd_16bit_a * rnd_16bit_b)
        mult32 = (66 - len(mult)) * "0" + mult[2:]
        f.writelines(f"{a}_{b}_{mult32}\n")
    f.close()


main()
