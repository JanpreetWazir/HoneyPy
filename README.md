# HONEYPY

HONEYPY is a modular honeypot designed to capture IP addresses, usernames, passwords, and commands from various protocols, currently supporting SSH and HTTP. It provides a simple yet effective way to gather intelligence on unauthorized access attempts.

## Requirements
- Python 3.x
- Flask (for HTTP honeypot)
- Paramiko (for SSH honeypot)
- Pandas (for data processing)
- Dash (for visualization dashboard)


## Usage
To start the honeypot, use:
```sh
python3 honeypy.py -a <IP_ADDRESS> -p <PORT> --ssh  # For SSH honeypot
python3 honeypy.py -a <IP_ADDRESS> -p <PORT> --http # For HTTP honeypot
```
Example:
```sh
python3 honeypy.py -a 0.0.0.0 -p 22 --ssh
```

To run with a specified username and password:
```sh
python3 honeypy.py -a 0.0.0.0 -p 22 --ssh -u admin -pw password
```
To connect with username and password(from victim's side):
```sh
ssh admin@0.0.0.0 -p 22 
```

## Logging
HONEYPY stores logs in the `log_files` directory:
- `cmd_audits.log`: Logs IP, username, password, and commands.
- `creds_audits.log`: Logs IP, username, and password for SSH.
- `http_audit.log`: Logs IP, username, and password for HTTP.

## Dashboard
To view captured data in a web-based dashboard, run:
```sh
python3 web_app.py
```
Then access `http://127.0.0.1:8050` in a browser.

## Running in Background (Systemd)
To run HONEYPY as a background service, copy the `honeypy.service` file to `/etc/systemd/system/`, then execute:
```sh
systemctl daemon-reload
systemctl enable honeypy.service
systemctl start honeypy.service
```

HONEYPY is a lightweight, effective tool for security researchers and enthusiasts to analyze unauthorized access attempts.
