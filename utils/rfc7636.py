# RFC 7636 - Proof Key for Code Exchange by OAuth Public Clients implementation
# Usage: ./rfc7636 [cv/cc] [if cc, place the code verifier token here]
# Returns 1 if lack of arguments, 0 otherwise
# Not intended for direct interfacing.
import base64
import hashlib
import secrets
import string
import sys

def genCodeVerifier():
	alpha = string.ascii_letters # includes both lower and uppercase
	digits = string.digits
	special_charas = "-._~"

	unreserved = alpha + digits + special_charas
	codeverifier = str()

	for i in range(secrets.choice(range(43, 128))): # choose between 43 to 128 characters
		codeverifier += secrets.choice(unreserved)

	return codeverifier

def createCodeChallenge(codeverifier):
	if isinstance(codeverifier, str):
		return base64.urlsafe_b64encode(hashlib.sha256(codeverifier.encode()).digest())
	else: raise RuntimeError("codeverifier must be a str() object")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		sys.exit(1)

	if sys.argv[1] == "cv":
		print(genCodeVerifier())

	if sys.argv[1] == "cc":
		if len(sys.argv) == 3:
			print(createCodeChallenge(sys.argv[2]).decode()[:-1])
		else: sys.exit(1)

	sys.exit(0)
