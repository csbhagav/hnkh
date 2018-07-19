HNKH
=====



Setup
-----
This repository is primarily developed in python and uses standard
python tooling ([`pip`][pip] and
[`requirements` files][requirements]). Additionally,
[`direnv`][direnv], [`pyenv`][pyenv], and
[`pyenv-virtualenv`][pyenv-virtualenv] are helpful tools for managing
your project dependent environment variables and python environments.

  1. (Optional) with [`pyenv`][pyenv] and
     [`pyenv-virtualenv`][pyenv-virtualenv] installed, create a virtual
     environment for the repo:

         pyenv virtualenv 3.6 hnkh
         echo 'hnkh' > .python-version

  2. Install the repo in edit mode (from the repo root):

         pip install -r requirements.txt
         pip install -e .


Download Data
-----

`./get-data.sh` will put the BBC dataset in the `data/` directory.