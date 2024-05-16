=========
Changelog
=========


2024/05/16
~~~~~~~~~~

- update MongoDB helper for MongoDB > 4.0
- add replicaSet support to MongoDB helper
- add directConnection option to MongoDB helper

- Python 3.5 is now the minimal requirement


2024/04/25
~~~~~~~~~~

- add async possibility


2019/01/14
~~~~~~~~~~

- add execute_command in utils helper. This command is a wrapper of subprocess.run()

- Python 3.5 is now the minimal requirement


2018/11/14
~~~~~~~~~~

- remove no more need dependency (pytest-catchlog now included in Pytest)

- add an utility method (utils.plog) to write a message no captured
  new conf in pytest.ini must be added:
  log_cli = True
  log_cli_level = INFO


2017/08/03
~~~~~~~~~~

- Add Niav component

- Add SSL configs (http component must be instantiated by Niav component or Env must be set in http (http.set_env())


2017/05/26
~~~~~~~~~~

- Initial version
