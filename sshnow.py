import paramiko
import sys

if __name__ == '__main__':
    args_len = (len(sys.argv))
    if args_len != 5:
        print("Missing arguments.\n"
              + "Commands: python3 " + sys.argv[0] + " <ip/hostname> <username> <password> <commands in quote>\n"
              + "Example: python3 " + sys.argv[0] + " 1.2.3.4 username password 'hostname\n"
              + "Exit."
              )
        exit
    elif args_len == 5:
        target_host = sys.argv[1]
        user_name = sys.argv[2]
        user_pwd = sys.argv[3]
        cmds = sys.argv[4]

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=target_host, username=user_name, password=user_pwd)

        stdin, stdout, stderr = ssh_client.exec_command(cmds)
        cmds_out = stdout.read().decode().strip()
        cmd_err = stderr.read().decode().strip()
        print(cmds_out)
        print(cmd_err)

        del ssh_client, stdin, stdout, stderr
