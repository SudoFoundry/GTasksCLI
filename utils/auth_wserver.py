# auth_wserver.py - Recieves stuff from the Google Authentication Server after authenticating with Google. Please pass in the port to this needy script (intentional).
# Returns to the caller a code to be interpreted by some other script.
# Please contact the Google Authentication Server first before launching this script.
# Also, listens to 127.0.0.1 only because that suffices.
# Exits with error code 1 if caller makes python script sad :(

import http.server
import socketserver
import sys
import urllib

class auth_wserver (http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		query = urllib.parse.urlparse(self.path).query
		if "code" in urllib.parse.parse_qs(query):
			print(urllib.parse.parse_qs(query)["code"][0])
			self.send_header("Content-Type", "text/plain")
			self.wfile.write("Authentication OK. Please close this window.\n".encode())
			self.send_response(200) # everything is fine
			self.end_headers()

		if "error" in urllib.parse.parse_qs(query):
			print("error")
			self.send_header("Content-Type", "text/plain")
			self.wfile.write("Authentication rejected. Please close this window.\n".encode())
			self.send_response(503) # everything is the opposite of fine
			self.end_headers()
		return

	def log_request(code, size):
		pass # do not implement

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit(1) # pass in a port damn it

	port = sys.argv[1]
	with socketserver.TCPServer(("", int(port)), auth_wserver) as httpd:
		httpd.handle_request()

	sys.exit(0)
