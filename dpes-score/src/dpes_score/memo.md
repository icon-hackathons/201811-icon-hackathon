// start
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate venv36

// deploy
tbears deploy project -k keystores/k1.json -c config/tbears_cli_config_testnet.json

// txresult
tbears txresult 0xa33220f089306b42cae89494c5c2647c3ea37dc3421b0f29775c53ebc974300b -u https://bicon.net.solidwallet.io/api/v3

