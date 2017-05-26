import logging
import paramiko


class Ssh(object):
    """
        SSH utilities
        
        - Execute commands on remote host.
        - Copy files from and to remote host.
    """

    def __init__(self, host, port=None, user=None, password=None, private_key=None):
        """
            :param host: Hostname or ip
            :param port: Connection port
            :param user: Username
            :param password: User or key password
            :param private_key: Full path to the private key
            :type host: string
            :type port: integer (default: 22)
            :type user: string (default: root)
            :type password: string (default: None)
            :type private_key: (default: None)
        """
        ssh_port = 22
        if port is not None:
            try:
                ssh_port = int(port)
            except:
                raise TypeError("ssh port should be an integer")
        self.log = logging.getLogger("niav")
        self.connection = None
        self.host = host
        self.port = ssh_port
        self.user = "root" if user is None else user
        self.password = password
        self.private_key = private_key

    def connect(self):
        """
            Open a connection to a remote host
        """
        if self.connection is None:
            self.log.debug("opening connection to '%s'" % self.host)
            self.connection = paramiko.SSHClient()
            self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.connection.connect(self.host, port=self.port, username=self.user,
                                    password=self.password, key_filename=self.private_key)
        self.log.debug("connected to '%s'" % self.host)

    def execute(self, cmd, encoding="utf-8"):
        """
            Run a command on a remote host

            :param cmd: Command to execute
            :param encoding: Remote encoding (default: utf-8)
            :type cmd: string
            :type encoding: string
            :return: stdout output, stderr output, exit code
            :rtype: tuple (string, string, integer)
        """
        self.connect()
        self.log.debug("executing command '%s'" % cmd.encode(encoding))
        c_stdin, c_stdout, c_stderr = self.connection.exec_command(cmd)
        exit_code = c_stdout.channel.recv_exit_status()
        stdout = c_stdout.read().decode(encoding)
        stderr = c_stderr.read().decode(encoding)
        self.log.debug("exit code: %s" % exit_code)
        self.log.debug("stdout: %s" % stdout)
        self.log.debug("stderr: %s" % stderr)
        return stdout, stderr, exit_code

    def disconnect(self):
        """
            Disconnect from a remote host
        """
        if self.connection:
            self.connection.close()

    def sftp_get(self, remote_path, local_path):
        """
            Copy a file from the remote host locally through SFTP

            :param remote_path: Full path of the remote file
            :param local_path: Local path of the copied file
            :type remote_path: string
            :type local_path: string
        """
        self.connect()
        self.log.debug("copying file '%s:%s' to '%s'" % (self.host, local_path, remote_path))
        sftp = self.connection.open_sftp()
        sftp.get(remote_path, local_path)
        sftp.close()

    def sftp_put(self, local_path, remote_path):
        """
            Copy a local file to a remote host through SFTP

            :param local_path: Local path of the copied file
            :param remote_path: Full path of the remote file
            :type local_path: string
            :type remote_path: string
        """
        self.connect()
        self.log.debug("copying file '%s' to '%s:%s'" % (local_path, self.host, remote_path))
        sftp = self.connection.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()
