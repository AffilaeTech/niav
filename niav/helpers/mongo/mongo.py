import logging
import pendulum

from pymongo import MongoClient
from bson.objectid import ObjectId
from niav.ssh_tunnel import SshTunnel


class Mongo(object):
    """
        MongoDB helper
        
        - MongoDB wrapper
        - load configurations
        - open SSH tunnel if needed
    """

    def __init__(self, env, section_mongo=None, section_tunnel_ssh=None):
        """     
            :param env: Env instance
            :param section_mongo: Section name for MongoDB configuration in env.ini file
            :param section_tunnel_ssh: Section name for SSH tunnel configuration in env.ini file.
            :type env: object instance
            :type section_mongo: string
            :type section_tunnel_ssh: string
        """
        self.env = env
        self.section_mongo = section_mongo
        self.section_tunnel_ssh = section_tunnel_ssh

        self.host = None
        self.port = None
        self.client = None
        self.direct_connection = None
        self.replica_set = None

        self.tunnel = None
        self.tunnel_host = None
        self.tunnel_port = None
        self.tunnel_user = None
        self.tunnel_password = None
        self.tunnel_private_key = None
        self.tunnel_private_key_password = None
        self.tunnel_local_port = None
        self.tunnel_remote_port = None

        self.log = logging.getLogger("niav")

        self.configure_mongo()
        self.configure_tunnel_ssh()

    def connect(self):
        """
            Connect to MongoDB and start SSH tunnel if required.
        
            :return: MongoClient instance
            :rtype: object instance
        """
        if self.is_tunnel_ssh_required():
            self.tunnel = SshTunnel(self.tunnel_host, self.tunnel_local_port, self.tunnel_remote_port,
                                    port_ssh=self.tunnel_port, user=self.tunnel_user, password=self.tunnel_password,
                                    private_key=self.tunnel_private_key, private_key_password=self.tunnel_private_key_password)
            self.tunnel.connect()
            self.tunnel.start()

        if self.client is None:
            self.client = MongoClient(self.host, self.port, directConnection=self.direct_connection, replicaSet=self.replica_set)
            self.log.info("Mongo connected to '%s'" % self.host)
        return self.client

    def close(self):
        """
            Close connection to MongoDB.
        """
        self.client.close()

        if self.tunnel is not None:
            self.tunnel.stop()

    def get_client(self):
        """
            Get MongoClient instance.
            
            :return: MongoClient instance
            :rtype: object instance
        """
        return self.client

    def configure_mongo(self):
        """
            Load MongoDB configuration from env.ini
        """
        if self.section_mongo is None:
            self.section_mongo = "mongo"

        self.host = self.env.get("%s.host" % self.section_mongo)
        self.port = self.env.get_int("%s.port" % self.section_mongo)
        self.direct_connection = self.env.get_boolean_unsafe("%s.direct_connection" % self.section_mongo) if self.env.get_boolean_unsafe("%s.direct_connection" % self.section_mongo) is not None else True
        self.replica_set = self.env.get_unsafe("%s.replica_set" % self.section_mongo) if self.env.get_unsafe("%s.replica_set" % self.section_mongo) is not "" else None

    def configure_tunnel_ssh(self):
        """
            Load configuration from env.ini 
        """
        if self.section_tunnel_ssh is None:
            self.section_tunnel_ssh = "tunnel_ssh"

        self.tunnel_host = self.env.get_unsafe("%s.host" % self.section_tunnel_ssh)
        self.tunnel_port = self.env.get_int_unsafe("%s.port" % self.section_tunnel_ssh)
        self.tunnel_user = self.env.get_unsafe("%s.user" % self.section_tunnel_ssh)
        self.tunnel_password = self.env.get_unsafe("%s.password" % self.section_tunnel_ssh)
        self.tunnel_private_key = self.env.get_unsafe("%s.private_key" % self.section_tunnel_ssh)
        self.tunnel_private_key_password = self.env.get_unsafe("%s.private_key_password" % self.section_tunnel_ssh)
        self.tunnel_local_port = self.env.get_int_unsafe("%s.local_port" % self.section_tunnel_ssh)
        self.tunnel_remote_port = self.env.get_int_unsafe("%s.remote_port" % self.section_tunnel_ssh)

    def is_tunnel_ssh_required(self):
        """
            Check if the configuration is sufficient to start the SSH tunnel.
            
            :return: boolean
            :rtype: bool
        """
        if self.tunnel_host not in [None, ""] and self.tunnel_local_port not in [None, ""] and self.tunnel_remote_port not in [None, ""]:
            return True
        return False

    @classmethod
    def object_id(cls, id_to_object_id):
        """
            Get a string Id and return a MongoDB ObjectID.
            
            :param id_to_object_id: id
            :rtype id_to_object_id: string
            :return: MongoDB ObjectID
            :rtype: ObjectID
        """
        return ObjectId(id_to_object_id)

    @classmethod
    def str_id(cls, object_id_to_id):
        """
            Get a MongoDB ObjectID and return a string id.
            
            :param object_id_to_id: id
            :type object_id_to_id: ObjectId
            :return: id
            :rtype: string
        """
        return str(object_id_to_id)

    @classmethod
    def from_datetime(cls, generation_time=None, timezone="UTC"):
        if generation_time is None:
            generation_time = pendulum.now(timezone).start_of("day")
            # print(generation_time.strftime("%Y-%m-%d %H:%M:%S"))

        object_id = ObjectId.from_datetime(generation_time)
        # print(cls.str_id(object_id))
        return object_id

    @classmethod
    def insert_one(cls, db, collection, doc):
        """
            Insert a document.
            
            :param db: Database name
            :param collection: Collection name
            :param doc: Document to insert
            :type db: 'string'
            :type collection: string
            :type doc: dict
            :return: id
            :rtype: ObjectId
        """
        returned_id = db[collection].insert_one(doc).inserted_id
        return returned_id

    def update_one(self, db, collection, q_filter, update):
        """
            Update a document.
            
            :param db: Database name
            :param collection: Collection name
            :param q_filter: Query filter
            :param update: Data to update
            :type db: 'string'
            :type collection: string
            :type q_filter: dict
            :type update: dict
            :return: True if update is ok
            :rtype: bool
        """
        result = db[collection].update_one(q_filter, update)
        if result.matched_count != 1 or result.modified_count != 1:
            self.log.warning("Mongo update_one: filter match: %d, modified: %d" % (result.matched_count, result.modified_count))
            return False
        return True
