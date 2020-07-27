import struct, sys, random
# Based on disassembly of the function at 0664:4b92, handle_password
ALPHABET='AM2L3C4Z5P6B7HE9'



def generate_code(score, level, paddles, random_shuffle=None):
	if random_shuffle is None:
		random_shuffle = random.randint(0,7)+1
	score_array = [ord(x) for x in struct.pack('<LBB', score, level, paddles)]
	checksum = sum(score_array) & 0xFF
	score_array.append(checksum)
	# expand array out to only having values in the range 0-15
	expanded=[]
	for v in score_array:
		expanded.append(v&0xF)
		expanded.append(v>>4)

	# invert all bytes:
	expanded = [(~x)&0xF for x in expanded]

	# increment first digit by randomization
	expanded[0] = (expanded[0] + random_shuffle) & 0xF

	# iterate every letter based on previous letter
	for i in range(1, 0xE):
		expanded[i] = (expanded[i] + (expanded[i-1]^0xFF))&0xF

	# Add in the random shuffle digit so it can be extracted latter
	expanded.append(random_shuffle)

	# Convert to custom hex alphabet
	alphabetized = ''.join(ALPHABET[x] for x in expanded)

	# add dashes:
	return '-'.join((alphabetized[:5],alphabetized[5:10],alphabetized[10:]))

if __name__=='__main__':
	if len(sys.argv) in (4,5):
		score=int(sys.argv[1])
		level=int(sys.argv[2])-1 # levels are stored 0-based, shown 1-based
		paddles=int(sys.argv[3])
		if len(sys.argv) == 5:
			random_shuffle = int(sys.argv[4])
		else:
			random_shuffle = None 

		code = generate_code(score, level, paddles, random_shuffle)
		print(code)
	if len(sys.argv)==2 and sys.argv[1] == '--level-list':
		for level in range(1,101):
			print ('Level {: 4}: {}'.format(level, generate_code(0, level, 6)))
	else:
		print('Usage: encode.py <score> <level> <paddles> [random]')
		print('or     encode.py --level-list')
		sys.exit(1)