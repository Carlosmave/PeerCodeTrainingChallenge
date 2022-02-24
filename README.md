# Peer Code Training Challenge

## Installation

It requires Python v3.7.5+ to run.

Install the dependencies and run the python file.
```sh
cd PeerCodeTrainingChallenge
pip3 -m virtualenv venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```

## Execution

Required env vars:

- BITWARDEN_ENV (*'local'* or *'robocloud'*) Get bitwarden creds from env vars or from Robocloud Vault. Default is 'local'
- BITWARDEN_USERNAME (should be set for local execution if *BITWARDEN_ENV=='local'*)
- BITWARDEN_PASSWORD (should be set for local execution if *BITWARDEN_ENV=='local'*)
- BITWARDEN_CLIENT_ID (should be set for local execution if *BITWARDEN_ENV=='local'*)
- BITWARDEN_CLIENT_SECRET (should be set for local execution if *BITWARDEN_ENV=='local'*)

example:
```sh
# bot execution locally
python task.py local
```

via *rcc*:
```sh
rcc run
```
