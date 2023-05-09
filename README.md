# ClamAV Privilege Escalation Exploit

## ROOT EXPLOIT

This is a Python 3 script designed to exploit the ClamAV privilege escalation vulnerability described at https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudo-clamav-privilege-escalation/. The script performs a brute-force attack to guess the RSA private key of the root user, but it can be easily modified to read any file as root.

### Installation

    Clone this repository to your local machine.

    Open a terminal and navigate to the directory where you cloned the repository.
    
### Usage

To run the exploit, simply execute the script:

``python3 root_exploit.py``

The script will launch ClamAV as the root user and try to guess the RSA private key by brute force. Once the key is found, it will be saved to a file called id_rsa.
### Customization

The script is designed to target the RSA private key of the root user, but you can easily modify it to target any file that can be read by the root user. To do this, you need to modify the guess_char() function to guess the contents of the file you want to read.

You can also modify the user and w variables to target a different user's home directory or a different file, respectively.

### Disclaimer

This script is intended for educational and testing purposes only. Do not use it for illegal or malicious activities. The author is not responsible for any misuse or damage caused by this script. Use at your own risk.

This is a Python script that cleans the output from ClamAV, an open-source antivirus engine, and saves the cleaned data to a file.
Getting Started
Prerequisites

## ROOT THROUGH F PARAMETER

This script requires Python 3 to be installed on your system. You can download and install Python from the official website: https://www.python.org/downloads/

### Installation

    Clone this repository to your local machine.

    Open a terminal and navigate to the directory where you cloned the repository.

### Usage

To use the script, run the following command:

``python3 root_through_f.py /clamav/output/path``

This command reads the output from ClamAV located at /clamav/output/path, cleans the data, and saves the cleaned data to a file named output.txt.

### Note

Before running the script, you must generate the ClamAV output as a root user. To generate the output, run the following command:

  ``sudo /usr/bin/clamav -f /path/to/file/to/read``

    Copy the output to a file and use it as the input for the script.
### License

This project is licensed under the MIT License - see the LICENSE file for details.
