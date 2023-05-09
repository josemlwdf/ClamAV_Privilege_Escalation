### ClamAV Privilege Escalation Exploit

## ROOT EXPLOIT

This is a Python 3 script designed to exploit the ClamAV privilege escalation vulnerability described at https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudo-clamav-privilege-escalation/. The script performs a brute-force attack to guess the RSA private key of the root user, but it can be easily modified to read any file as root.
# Usage

To run the exploit, simply execute the script:

``python3 root_exploit.py``

The script will launch ClamAV as the root user and try to guess the RSA private key by brute force. Once the key is found, it will be saved to a file called id_rsa.
# Customization

The script is designed to target the RSA private key of the root user, but you can easily modify it to target any file that can be read by the root user. To do this, you need to modify the guess_char() function to guess the contents of the file you want to read.

You can also modify the user and w variables to target a different user's home directory or a different file, respectively.

# Disclaimer

This script is intended for educational and testing purposes only. Do not use it for illegal or malicious activities. The author is not responsible for any misuse or damage caused by this script. Use at your own risk.
