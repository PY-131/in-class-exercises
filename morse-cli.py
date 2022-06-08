import argparse
import morse


def morse_cli():
	parser = argparse.ArgumentParser()
	parser.add_argument("INPUT", type=str, help="input string for encode / decode")
	parser.add_argument("-e","--encode", action="store_true", help="Encodes a string to morse code")
	parser.add_argument("-d","--decode", action="store_true", help="Decodes from morse to ascii")
	args = parser.parse_args()

	if args.encode:
		print(f"Encoded {args.INPUT} as {morse.encode(args.INPUT)}")

	if args.decode:
		print(f"Decoded {args.INPUT} as {morse.decode(args.INPUT)}")

if __name__ == '__main__':
	morse_cli()