=====
Mongo
=====

File
----
    niav/niav/helpers/mongo/mongo.py

Class
-----

MongoDB utils

- MongoDB wrapper
- load configurations
- open SSH tunnel if needed

.. code-block::

  Mongo(env, section_mongo=None, section_tunnel_ssh=None)

       env:                 object instance. Env instance.
       section_mongo:       string. Section name for MongoDB configuration in env.ini file.
       section_tunnel_ssh:  string. Section name for SSH tunnel configuration in env.ini file.

.. code-block::

  close()
      Close connection to MongoDB.

.. code-block::

  configure_mongo()
      Load MongoDB configuration from env.ini

.. code-block::

  configure_tunnel_ssh()
      Load configuration from env.ini

.. code-block::

  connect()
      Connect to MongoDB and start SSH tunnel if required.

        return: object instance. MongoClient instance.

.. code-block::

  get_client()
      Get MongoClient instance.

        return: object instance. MongoClient instance.

.. code-block::

  insert_one(db, collection, doc)
      Insert a document.

        db:         string. Database name.
        collection: string. Collection name.
        doc:        dict. Document to insert.

        return:     ObjectId. id.

.. code-block::

  is_tunnel_ssh_required()
      Check if the configuration is sufficient to start the SSH tunnel.

        return: boolean

.. code-block::

  object_id(id_to_object_id)
      Get a string Id and return a MongoDB ObjectID.

        id_to_object_id: string. id.

        return: ObjectID. MongoDB ObjectID.

.. code-block::

  str_id(object_id_to_id)
      Get a MongoDB ObjectID and return a string id.

        object_id_to_id: ObjectId. id.

        return: string. id.

.. code-block::

  update_one(db, collection, q_filter, update)
      Update a document.

        db: string. Database name.
        collection: string. Collection name.
        q_filter:   dict. Query filter.
        update:     dict. Data to update.

        return:     bool. True if update is ok
