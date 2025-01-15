import os

def setup_server():
    print("Updating Termux...")
    os.system("apt update && apt upgrade -y")
    
    print("Installing Apache2 and PHP...")
    os.system("pkg install apache2 php -y")
    
    print("Starting Apache2 server...")
    os.system("apachectl start")
    
    print("Installing SQLite...")
    os.system("pkg install sqlite -y")
    
    print("Server setup complete. Place your files in `/data/data/com.termux/files/usr/share/apache2/default-site/htdocs/`.")

if __name__ == "__main__":
    setup_server()
