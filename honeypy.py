# Libraries
import argparse
import threading
from ssh_honeypot import honeypot
from web_honeypot import run_web_honeypot

# Parse Arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', type=str, required=True, help="Address to bind the honeypots")
    parser.add_argument('-p', '--ssh-port', type=int, required=False, default=2222, help="Port for SSH honeypot")
    parser.add_argument('-hp', '--http-port', type=int, required=False, default=5000, help="Port for HTTP honeypot")
    parser.add_argument('-u', '--username', type=str, default="admin", help="Default username for honeypots")
    parser.add_argument('-pw', '--password', type=str, default="password", help="Default password for honeypots")
    parser.add_argument('-s', '--ssh', action="store_true", help="Enable SSH honeypot")
    parser.add_argument('-w', '--http', action="store_true", help="Enable HTTP honeypot")
    args = parser.parse_args()
    
    try:
        threads = []

        # Start SSH Honeypot
        if args.ssh:
            print(f"[-] Running SSH Honeypot on {args.address}:{args.ssh_port}...")
            ssh_thread = threading.Thread(target=honeypot, args=(args.address, args.ssh_port, args.username, args.password))
            ssh_thread.start()
            threads.append(ssh_thread)

        # Start HTTP Honeypot
        if args.http:
            print(f"[-] Running HTTP Honeypot on port {args.http_port}...")
            http_thread = threading.Thread(target=run_web_honeypot, args=(args.http_port, args.username, args.password))
            http_thread.start()
            threads.append(http_thread)

        if not args.ssh and not args.http:
            print("[!] Choose a honeypot type: SSH (--ssh) or HTTP (--http).")
        else:
            for thread in threads:
                thread.join()

    except Exception as e:
        print(f"\n[!] Error: {e}")
        print("\n[!] Exiting HONEYPY...\n")
