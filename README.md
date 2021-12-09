# Gnosis Chain validator's data generator

- [Introduction](#introduction)
- [Tutorial for users](#tutorial-for-users)
  - [Requirements](#requirements)
  - [File Permission](#file-permissions)
  - [Commands](#commands)
    - [`new-mnemonic` Arguments](#new-mnemonic-arguments)
    - [`existing-mnemonic` Arguments](#existing-mnemonic-arguments)
    - [Successful message](#successful-message)
  - [Generate validator's data](#generate-validators-data)
    - [Step 1. Pull the docker image](#step-1-pull-the-docker-image)
    - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-1)
      - [Commands](#commands-1)
      - [Arguments](#arguments-1)
      - [Successful message](#successful-message-1)
- [Development](#development)
  - [Install basic requirements](#install-basic-requirements)
  - [Install testing requirements](#install-testing-requirements)
  - [Run tests](#run-tests)

## Introduction

`validator-data-generator` is a tool for creating [EIP-2335 format](https://eips.ethereum.org/EIPS/eip-2335) BLS12-381 keystores and a corresponding `deposit_data*.json` file for the Gnosis Chain.

It is based on the [Eth2.0 `deposit-cli` tool](https://github.com/ethereum/eth2.0-deposit-cli) with minor adoptation for the Gnosis Chain specific.

- **Warning: Please generate your keystores on your own safe, completely offline device.**
- **Warning: Please backup your mnemonic, keystores, and password securely.**

## Tutorial for users

### Requirements

- Docker

### File Permissions

On Unix-based systems, keystores and the `deposit_data*.json` have `440`/`-r--r-----` file permissions (user & group read only). This improves security by limiting which users and processes that have access to these files. If you are getting `permission denied` errors when handling your keystores, consider changing which user/group owns the file (with `chown`) or, if need be, change the file permissions with `chmod`.

### Commands

The tool offers different commands depending on what you want to do with the tool.

| Command | Description |
| ------- | ----------- |
| `new-mnemonic` | (Recommended) This command is used to generate keystores with a new mnemonic. |
| `existing-mnemonic` | This command is used to re-generate or derive new keys from your existing mnemonic. Use this command, if (i) you have already generated keys with this CLI before, (ii) you want to reuse your mnemonic that you know is secure that you generated elsewhere (reusing your eth1 mnemonic .etc), or (iii) you lost your keystores and need to recover your keys. |

#### `new-mnemonic` Arguments

You can use `new-mnemonic --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--num_validators`  | Non-negative integer | The number of signing keys you want to generate. Note that the child key(s) are generated via the same master key. |
| `--mnemonic_language` | String. Options: `chinese_simplified`, `chinese_traditional`, `czech`, `english`, `italian`, `korean`, `portuguese`, `spanish`. Default to `english` | The mnemonic language |
| `--folder` | String. Pointing to `./validator_keys` by default | The folder path for the keystore(s) and deposit(s) |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. Use `gnosis` for the Gnosis Chain. |
| `--eth1_withdrawal_address` | String. xDai address in hexadecimal encoded form | If this field is set and valid, the given xDai address will be used to create the withdrawal credentials. Otherwise, it will generate withdrawal credentials with the mnemonic-derived withdrawal public key in [EIP-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |

#### `existing-mnemonic` Arguments

You can use `existing-mnemonic --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--validator_start_index` | Non-negative integer | The index of the first validator's keys you wish to generate. If this is your first time generating keys with this mnemonic, use 0. If you have generated keys using this mnemonic before, use the next index from which you want to start generating keys from (eg, if you've generated 4 keys before (keys #0, #1, #2, #3), then enter 4 here.|
| `--num_validators`  | Non-negative integer | The number of signing keys you want to generate. Note that the child key(s) are generated via the same master key. |
| `--folder` | String. Pointing to `./validator_keys` by default | The folder path for the keystore(s) and deposit(s) |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. Use `gnosis` for the Gnosis Chain. |
| `--eth1_withdrawal_address` | String. xDai address in hexadecimal encoded form | If this field is set and valid, the given xDai address will be used to create the withdrawal credentials. Otherwise, it will generate withdrawal credentials with the mnemonic-derived withdrawal public key in [EIP-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |

#### Successful message

You will see the following messages after successfully generated the keystore(s) and the deposit(s):

```text
Creating your keys:               [####################################]  <N>/<N>
Creating your keystores:          [####################################]  <N>/<N>
Creating your depositdata:        [####################################]  <N>/<N>
Verifying your keystores:         [####################################]  <N>/<N>
Verifying your deposits:          [####################################]  <N>/<N>

Success!
Your keys can be found at: <YOUR_FOLDER_PATH>
```

### Generate validator's data

#### Step 1. Pull the docker image

Run the following command to locally build the docker image:

```sh
docker pull ghcr.io/gnosischain/validator-data-generator:latest
```

#### Step 2. Create keys and `deposit_data-*.json`

Run the following command to enter the interactive CLI:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys ghcr.io/gnosischain/validator-data-generator:latest
```

You can also run the tool with optional arguments:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys ghcr.io/gnosischain/validator-data-generator:latest new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english --folder=<YOUR_FOLDER_PATH>
```

Example for 1 validator on the Gnosis Chain using english:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys ghcr.io/gnosischain/validator-data-generator:latest new-mnemonic --num_validators=1 --mnemonic_language=english --chain=gnosis
```

##### Commands

See [here](#commands)

##### Arguments

  - See [here](#new-mnemonic-arguments) for `new-mnemonic` arguments
  - See [here](#existing-mnemonic-arguments) for `existing-mnemonic` arguments

##### Successful message
See [here](#successful-message)

## Development

### Install basic requirements

```sh
python3 -m pip install -r requirements.txt
python3 setup.py install
```

### Install testing requirements

```sh
python3 -m pip install -r requirements_test.txt
```

### Run tests

```sh
python3 -m pytest .
```
