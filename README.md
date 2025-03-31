# HONEYPY

HONEYPY is a modular honeypot designed to capture IP addresses, usernames, passwords, and commands from unauthorized access attempts. It supports SSH and HTTP protocols, providing valuable intelligence for security researchers.

## Requirements
- Python 3.x
- Flask (for HTTP honeypot)
- Paramiko (for SSH honeypot)
- Pandas (for data processing)
- Dash (for visualization dashboard)

## Usage
### Running SSH Honeypot
```sh
python3 honeypy.py -a <IP_ADDRESS> -p <PORT> --ssh
```
Example:
```sh
python3 honeypy.py -a 0.0.0.0 -p 22 --ssh
```
To run with a specified username and password:
```sh
python3 honeypy.py -a 0.0.0.0 -p 22 --ssh -u admin -pw password
```
To connect as a victim:
```sh
ssh admin@0.0.0.0 -p 22
```

### Running HTTP Honeypot
```sh
python3 honeypy.py -a <IP_ADDRESS> -hp <PORT> --http
```
Example:
```sh
python3 honeypy.py -a 0.0.0.0 -hp 5000 --http
```

### Running Both SSH and HTTP Honeypots
```sh
python3 honeypy.py -a 0.0.0.0 -p 2222 -hp 5000 --ssh --http
```

## Logging
HONEYPY stores logs in the `log_files` directory:
- `cmd_audits.log`: Captures IP, username, password, and executed commands.
- `creds_audits.log`: Records IP, username, and password for SSH attempts.
- `http_audit.log`: Logs IP, username, and password for HTTP access.

## Dashboard
To visualize captured data in a web-based dashboard:
```sh
python3 web_app.py
```
Then access `http://127.0.0.1:8050` in a browser.

## Running in Background (Systemd)
To run HONEYPY as a background service:
```sh
sudo cp honeypy.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable honeypy.service
sudo systemctl start honeypy.service
```

HONEYPY is a lightweight, effective tool for security researchers to analyze unauthorized access attempts.

