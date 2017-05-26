from niav.testcase import TestCase
from niav.env import Env
from niav.utils import Utils
from niav.file import File
from niav.ssh import Ssh


class TestSsh(TestCase):

    def setUp(self):
        self.env = Env(__file__)
        self.host = self.env.get("niav_server_ssh.host")
        self.port = self.env.get("niav_server_ssh.port")
        self.user = self.env.get("niav_server_ssh.user")
        self.password = self.env.get("niav_server_ssh.password")
        self.private_key = self.env.get("niav_server_ssh.private_key")

    def tearDown(self):
        pass

    def test_ssh_login_with_key_success(self):
        ssh = Ssh(self.host, port=self.port, user=self.user, private_key=self.private_key)
        ssh.connect()
        ssh.disconnect()

    def test_ssh_execute_command(self):
        ssh = Ssh(self.host, port=self.port, user=self.user, private_key=self.private_key)
        stdout, stderr, exit_code = ssh.execute("echo 'Niav'")
        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout, "Niav\n")
        ssh.disconnect()

    def test_ssh_transfer_files(self):
        ssh = Ssh(self.host, port=self.port, user=self.user, private_key=self.private_key)
        local_file = "/bin/echo"
        remote_file = "/tmp/echo_%s" % Utils.get_random_string()

        # send the file to remote
        ssh.sftp_put(local_file, remote_file)

        # compare if the two files are the same
        sha1_local_file = File.sha1_file(local_file)
        stdout, stderr, exit_code = ssh.execute("sha1sum '%s'" % remote_file)
        self.assertEqual(exit_code, 0)
        sha1_remote_file = stdout.split(" ")[0]
        self.assertEqual(sha1_local_file, sha1_remote_file)

        # get the file from remote
        new_local_file = "%s/echo_%s" % (File.get_tmp_folder(), Utils.get_random_string())
        ssh.sftp_get(remote_file, new_local_file)
        self.assertEqual(sha1_remote_file, File.sha1_file(new_local_file))

        # remove test files
        stdout, stderr, exit_code = ssh.execute("rm -f '%s'" % remote_file)
        self.assertEqual(exit_code, 0)
        File.delete_file(new_local_file)

        ssh.disconnect()

