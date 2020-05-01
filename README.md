# WavesLPoSDistributer
A revenue distribution tool for Waves nodes

## Installation
First of all, you need to install Node.js (https://nodejs.org/en/) and NPM. Afterwards the installation of the dependencies could be done via:
```sh
mkdir node_modules
npm install
```
Once the dependencies are installed, the script that generates the payouts need to be configured. In order to do so, change the settings of the configuration section:
```sh
/*
    Put your settings here:
        - address: the address of your node that you want to distribute from
        - startBlockHeight: the block from which you want to start distribution for
        - endBlock: the block until you want to distribute the earnings
        - filename: file to which the payments for the mass payment tool are written
        - node: address of your node in the form http://<ip>:<port
        - percentageOfFeesToDistribute: the percentage of Waves fees that you want to distribute
 */
var config = {
    address: '',
    startBlockHeight: 462000,
    endBlock: 465000,
    filename: 'test.json',
    node: 'http://<ip>:6869',
    percentageOfFeesToDistribute: 100
}
```
After a successful configuration of the tool, it could be started with:
```sh
node app.js
```
After the script is finished, the payments that should be distributed to the leasers are written to the file configured by the _config.filename_ setting in the configuration section.
## Why two seperate tools?
We decided to use two seperate tools since this allows for additional tests of the payments before the payments are actually executed. On the other hand, it does not provide any drawback since both scripts could also be called directly one after the other with:
```sh
node apps.js && node massPayment.js
```
We strongly recommend to check the payments file before the actual payments are done. In order to foster these checks, we added the _checkPaymentsFile.js_ tool that could need to be configured as follows:
```sh
/**
 * Put your settings here:
 *     - filename: file to check for payments
 *     - node: address of your node in the form http://<ip>:<port
 */
var config = {
    filename: '',
    node: 'http://<ip>:<port>'
};
```
After the configuration the checking tool could be executed with:
```sh
node checkPaymentsFile.js
```
The output of the tool should provide an information about how man tokens of each asset will be paid by the payment script. After checking this information, you should be ready to execute the payments.
## Transfer rewards to an address to transfer from
In order to transfer the rewards from the node to an address you want to distribute from, you can use the collectReward.js file. Configuration is done as follows:
```sh
/**
 * Put your settings here:
 *
 * address: the address you are collecting your rewards from (usually your nodes address)
 * recipient: the address you want to transfer the rewards to and do the distribtion from
 * node: your node address (http://<node url>:6862)
 */
var config = {
    address: '',
    recipient: '',
    node: ''
}
```
After configuring, you can execute the script by:
```sh
node collectRewards.js
```
It will prompt you for both, your API key and the password for accessing your private key. You'll find both in the credentials.txt file generated during node installation.
## Mass transfer payouts
The generated payout files could now also be used as inputs for mass transfer transactions. this provides a faster and cheaper way to distribute funds.
```sh
python massPayment.py
```
Configuration is done via the configuration section:
```sh
'''
    Configuration section:
        privateKey: the private key of the address you want to distribute from
        file: the calculated payout file
        timeout: timeout between requests send to nodes in ms
        nodes: a list of nodes to which the signed transactions should be send to, in the format: http://host:port
'''
config = {
	'privateKey': '',
	'file': '',
	# timeout between requests in ms
	'timeout': 20,
	'nodes': [
	]
}
```
## Disclaimer
Please always test your resulting payment scripts, e.g., with the _checkPaymentsFile.js_ script!