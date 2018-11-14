=========
Changelog
=========


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
