import struct, sys
# Based on disassembly of the function at 0339:1978, handle_password
ALPHABET='AM2L3C4Z5P6B7HE9'
if len(sys.argv)>1:
	code = sys.argv[1]
else:
	code = '53999-999EA-7279B'

# uppercase and remove dashges
code = code.upper().replace('-','')

# Decode letters to numbers
numbers=[ALPHABET.index(c) for c in code]

# Subtract inverted numbers
for i in range(0xD)[::-1]:
	iv=numbers[i] ^ 0xFFFF
	numbers[i+1] = (numbers[i+1] - iv) & 0xF

# Invert the first number by the last number
numbers[0] = (numbers[0] - numbers[14]) & 0xF

# invert every digit
for i in range(0, 0xE):
	numbers[i] = (numbers[i] ^ 0xFFFF) & 0x0F

# Extract out the score-numbers, which are combinations of the first 14 digits, but only 8 of them are used
score_numbers=[]
for i in range(7):
	score_numbers.append(numbers[i*2+0] + numbers[i*2+1]*16)

paddles = numbers[10]
level = numbers[8] + 1

# calculate checksum. Just add all the score bytes together
checksum = 0
for i in range(6):
	checksum = (checksum + score_numbers[i])&0xFF

checksum_from_score = score_numbers[-1]

# reinterpret the first 4 numbers in score_numbers as a 32bit integer
# TODO: verify this is correct over 16bits? we copy 4 bytes, so 32bit makes more sense
score = struct.unpack('<L',struct.pack('4B', *score_numbers[:4]))[0]
print 'paddles  = ', paddles
print 'level    = ', level
print 'score    = ', score
if checksum_from_score == checksum:
	is_valid='VALID'
else:
	is_valid = 'INVALID, should be {:02X}'.format(checksum)
print 'checksum =  {:02X} ({})'.format(checksum_from_score, is_valid)

