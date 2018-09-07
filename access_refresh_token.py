# googleToken.py - Parses the json input for an access token, refresh token, and time to expire.
# Usage: ./googleToken.py [a/r/e]
# Returns 1 if insufficient/over-sufficient arguments, 2 if recieved error instead of tokens.
import json
import sys

class tokens:
	def __init__(self):
		self.access_token = str()
		self.refresh_token = str()
		self.expiry = str()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit(1)

	# Load json from standard input
	sysin = str()
	for line in sys.stdin:
		sysin += line

	data = json.loads(sysin)

	# Check for an error
	if "error" in data:
		sys.exit(2)

	# Access fields
	t = tokens()
	t.access_token = data["access_token"] if "access_token" in data else str()
	t.refresh_token = data["refresh_token"] if "refresh_token" in data else str()
	t.expiry = data["expires_in"] if "expires_in" in data else str()

	# Return appropriate field
	if sys.argv[1] == "a":
		print(t.access_token)

	if sys.argv[1] == "r":
		print(t.refresh_token)

	if sys.argv[1] == "e":
		print(t.expiry)		

	sys.exit(0)
