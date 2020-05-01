var request = require('request');
var readline = require('readline');

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


var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter your API key: ', (apiKey) => {
    rl.question('Please enter your password: ', (password) => {
        request.get(config.node + '/addresses/balance/' + config.address, (err, response, body) => {
            var amount = JSON.parse(body).balance - 10000000;
            var transfer = {
                "type": 4,
                "amount": amount,
                "fee": 10000000,
                "sender": config.address,
                "password": password,
                "recipient": config.recipient,
                "version": 2
            }

            request.post({ url: config.node + '/transactions/signAndBroadcast', json: transfer, headers: { "Accept": "application/json", "Content-Type": "application/json", "api_key": apiKey } }, function(err, response, body) {
                if (err) {
                    console.log(err);
                } else {
                    if (body.error) {
                        console.log('error during transfer: ' + body.message);
                    } else {
                        console.log('Successfully transferred ' + (amount / 100000000) + ' West to ' + config.recipient + '!');
                    }
                }
                rl.close();
            });
        });
    });
});

