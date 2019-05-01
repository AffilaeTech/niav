import tempfile
import hashlib
import os
import base64


class File(object):
    """
        File utilities
    """

    @classmethod
    def get_tmp_file(cls, size=0):
        """
            Create temporary file of specified size
    
            :param size: Expected size of created file
            :type size: integer (default: 0)
            :return: Created file full path
            :rtype: string
        """
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp_name = tmp.name
        if size > 0:
            tmp.seek(size - 1)
            tmp.write("\0")
        tmp.close()
        return tmp_name

    @classmethod
    def get_tmp_folder(cls):
        """
            Return a temp folder
            
            :return: tmp folder path
            :rtype: string
        """
        return tempfile.gettempdir()

    @classmethod
    def sha1_file(cls, path):
        """
            Calculate sha1 of specified file
    
            :param path: Full path to file
            :type path: string
            :return: File sha1
            :rtype: string
        """
        sha = hashlib.sha1()
        with open(path, "rb") as file_handler:
            chunk = file_handler.read(1024 ** 2)
            sha.update(chunk)
        return sha.hexdigest()

    @classmethod
    def delete_file(cls, path):
        """
            Delete specified file
    
            :param path: Full path to file
            :type path: string
        """
        if os.path.exists(path):
            os.unlink(path)

    @classmethod
    def file_to_base64(cls, path):
        """
            Encode file to base64

            :param path: Full path to file
            :type path: string
            :return: File base64 string
            :rtype: string
        """
        with open(path, "rb") as file_handler:
            file_base64_bytes = base64.b64encode(file_handler.read())
            return file_base64_bytes.decode("utf-8")
