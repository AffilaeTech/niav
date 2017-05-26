===
ssh
===

File
----
    niav/niav/ssh.py

Class
-----
    
SSH utilities

- Execute commands on remote host.

- Copy files from and to remote host.


    |  **Ssh**(host, port=None, user=None, password=None, private_key=None)
    |       host: string. Hostname or ip.
    |       port: integer. Connection port. (default: 22)
    |       user: string. Username. (default: root)
    |       password: string. User or key password. (default: None)
    |       private_key: string. Full path to the private key. (default: None)
    |
    |  **connect**()
    |      Open a connection to a remote host
    |
    |  **disconnect**()
    |      Disconnect from a remote host
    |
    |  **execute**(cmd, encoding='utf-8')
    |      Run a command on a remote host
    |
    |       cmd: string. Command to execute.
    |       encoding: string. Remote encoding. (default: utf-8)
    |       return: tuple (string, string, integer). stdout output, stderr output, exit code.
    |
    |  **sftp_get**(remote_path, local_path)
    |      Copy a file from the remote host locally through SFTP
    |
    |       remote_path: string. Full path of the remote file.
    |       local_path: string. Local path of the copied file.
    |
    |  **sftp_put**(local_path, remote_path)
    |      Copy a local file to a remote host through SFTP
    |
    |       local_path: string. Local path of the copied file.
    |       remote_path: string. Full path of the remote file.
