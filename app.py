from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()

	html = """<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/> <b>Ip:</b> {ip}"""
	return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), ip=ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)