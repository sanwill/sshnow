# sshnow
Simple python script to SSH and run shell commands to remote server.
The ```paramiko``` module need to be installed on the client before running this script.


**Usage:**
```
# python sshnow.py <ip/hostname> <username> <password> <commands in quote>
```

**Example:**
```
# python sshnow.py 1.2.3.4 user password "hostname"
myhostname
```


**Security Concern**

Since the password will be visible, do not run this script in front of unauthorized audience.

The credential will remain in ```history```. clean up history if you want to keep the credential safe.
