import pyhash

bit_vector = [0] * 20

# Non cryptographic hash function (Murmur and FNV)

fnv = pyhash.fnv1_32()
murmur  = pyhash.murmur3_32()

#Calculate the output of FNV and Murmur hash functions for Pikachu and Charmander

fnv_pika = fnv()"Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

print(fnv_pika)
print(fnv_char)

print(murmur_pika)
print(murmur_char)

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1

bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

print(bit_vector)

# A Wild Bulbasaur appears!

fnv_bulb = fnv("Balbasaur") % 20
murmur_bulb = murmur("Balbasaur") % 20


print(fnv_bulb)
print(murmur_bulb)

print(bit_vector[fnv_bulb])
print(bit_vector[murmur_bulb])