# BOTC
*How basic can we get?*

### What is it?
BOTC is a decentralized cryptographic currency written in Python 3.5 that's meant to be really basic for people getting into things like digital currency.

### How is it different?
BOTC doesn't run around what most cryptocurrencies use. The platform itself does not need any mining. There will be 100000 BOTC that will be given out to develop a flow in the BOTC economy

### How does the tech work?
BOTC uses Flask to manage the blockchain.
`python3 -m pip install -U flask`

### Addresses?
324-character addresses, baby!
RSA-1024 encryption!

### **NOTE**
This is a W.I.P. project. Do __**NOT**__ expect decent performance until I release better updates. This repository is only for the node code so expect a wallet soon.

### How to setup the node

##### Step 1 - Configure the config.py file
By default, the `launch.sh` file will create a config file with the host being localhost and the port being 51515. However, you can set it to what you want it to be.

##### Step 2 - Configure the knownhosts file
By default, there is no known hosts file. This file will be used to interact with other nodes to share block information. You **MUST** configure this file in order to be apart of the decentralized network.

Always prefix your hosts with the `http://` scheme in order for the core to not crash :)

Example:
```
test@test~/botc$ cat knownhosts
http://testlol.org:51515
http://danktown.xyz:12312
http://wqeqweqwe.services:50050
test@test~/botc$ 
```

##### Step 3 - Run the launch.sh script
This shell script will launch the node software and will check for a `config.py` file. It's a bash script so y'know... have bash installed.

##### Step 4 - ???
I don't know about this yet

##### Step 5 - Profit
Eureka! You got a BOTC core running on the BOTC network! Enjoy!
