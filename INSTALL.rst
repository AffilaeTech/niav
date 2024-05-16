Installation
------------

.. code-block:: bash

    # Install python dependencies:
    sudo apt-get install python-setuptools build-essential python3-dev libffi-dev libssl-dev python3-venv

    # Create vitualenv
    mkdir -p /home/${USER}/venv
    cd venv
    python3 -m venv niav

    # Activate virtualenv:
    source /home/${USER}/venv/niav/bin/activate

    # Install mandatory packages:
    pip install requests paramiko sshtunnel pytest pendulum

    # Install optional packages (depending of your project)
    # MongoDB driver
    pip install pymongo

    # Leave virtualenv:
    deactivate


Clone Niav:

.. code-block:: bash

    git clone https://github.com/AffilaeTech/niav.git /home/${USER}/code/niav


Run a test
----------

.. code-block:: bash

    cd /home/${USER}/code/niav/
    NIAV_ENV=tests/functional_tests/env.ini /home/${USER}/venv/niav/bin/pytest /home/${USER}/code/your_project/tests/functional_tests/test_simple.py


To execute from anywhere, use PYTHONPATH:

.. code-block:: bash

    export PYTHONPATH=$PYTHONPATH:/home/${USER}/code/niav/; NIAV_ENV=/home/${USER}/code/niav/tests/functional_tests/env.ini /home/${USER}/envs/niav/bin/pytest /home/${USER}/code/your_project/tests/functional_tests/test_simple.py
