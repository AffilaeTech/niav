==========
Ssh_tunnel
==========

File
----
    niav/niav/ssh_tunnel.py

Class
-----

SSH tunnel

.. code-block::

  SshTunnel(host, local_port, remote_port, port_ssh=None, user=None, password=None, private_key=None,
                private_key_password=None, remote_address=None)

        host:           string. Hostname or ip.
        local_port:     int. Port on the machine where this script is running.
        remote_port:    int. Port on the remote machine.
        remote_address: string. Address on the remote machine. (default: 127.0.0.1)
        port_ssh:       string. Connection port. (default: 22)
        user:           string. Username. (default: root)
        password:       string. User password. (default: None)
        private_key:    string. Full path to the private key. (default: None)
        private_key_password: Key password. (default: None)

.. code-block::

  connect()
      Initialize the SSH tunnel.

.. code-block::

  get_local_port()
      Get the local port.

        return: int. Local port.

.. code-block::

  start()
      Start the SSH tunnel.

        return: int. Local port

.. code-block::

  stop()
        Stop the SSH tunnel.
