import logging

from sshtunnel import SSHTunnelForwarder


class SshTunnel(object):
    """
        SSH tunnel
    """

    def __init__(self, host, local_port, remote_port, port_ssh=None, user=None, password=None,
                 private_key=None, private_key_password=None, remote_address=None):
        """
            :param host: Hostname or ip
            :param local_port: Port on the machine where this script is running
            :param remote_port: Port on the remote machine
            :param remote_address: Address on the remote machine
            :param port_ssh: Connection port
            :param user: Username
            :param password: User password
            :param private_key: Full path to the private key
            :param private_key_password: Key password
            :type host: string
            :type local_port: integer
            :type remote_port: integer
            :type remote_address: string (default: 127.0.0.1)
            :type port_ssh: integer (default: 22)
            :type user: string (default: root)
            :type password: string (default: None)
            :type private_key: string (default: None)
            :type private_key_password: string (default: None)
        """
        ssh_port = 22
        if port_ssh is not None:
            try:
                ssh_port = int(port_ssh)
            except:
                raise TypeError("ssh port should be an integer")

        self.remote_address = "127.0.0.1" if remote_address is None else remote_address
        self.local_port = local_port
        self.remote_port = remote_port

        self.log = logging.getLogger("niav")
        logging.getLogger("paramiko").setLevel(logging.WARNING)
        self.tunnel = None
        self.host = host
        self.port = ssh_port
        self.user = "root" if user is None else user
        self.password = password
        self.private_key = private_key
        self.private_key_password = private_key_password

    def connect(self):
        """
            Initialize the SSH tunnel.
        """
        if self.tunnel is None:
            self.log.info("opening tunnel to '%s'" % self.host)

            self.tunnel = SSHTunnelForwarder(
                self.host,
                ssh_username=self.user,
                ssh_password=self.password,
                local_bind_address=("127.0.0.1", self.local_port),
                remote_bind_address=(self.remote_address, self.remote_port),
                ssh_pkey=self.private_key,
                ssh_private_key_password=self.private_key_password,
            )
            self.log.info("tunnel to '%s' is initialized" % self.host)

    def start(self):
        """
            Start the SSH tunnel.
            
            :return: Local port
            :rtype: integer
        """
        self.tunnel.start()
        self.local_port = self.tunnel.local_bind_port
        self.log.info("tunnel to '%s' is started (local bind port: %s)" % (self.host, self.tunnel.local_bind_port))
        return self.local_port

    def stop(self):
        """
            Stop the SSH tunnel.
        """
        self.tunnel.stop()
        self.log.info("tunnel to '%s' is stopped" % self.host)

    def get_local_port(self):
        """
            Get the local port.
            
            :return: Local port.
            :rtype: integer
        """
        return self.local_port
