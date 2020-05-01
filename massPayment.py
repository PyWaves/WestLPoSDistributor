import json
import time
import pywaves as pw
import time

config = {
	'privateKey': '',
	'file': '',
	# timeout between requests in ms
	'timeout': 100,
	'nodes': [
		''
	]
}

startTime = time.time()
totalPayments = 0
paid = 0
counter = 0

pw.setNode(config['nodes'][0], 'mainnet')
pw.setChain('Vostok', 'V')
print(config['nodes'][0])
address = pw.Address(privateKey = config['privateKey'])

def pay(batch):
    global paid
    global address
    global counter

    node = config['nodes'][counter % len(config['nodes'])]
    counter += 1
    pw.setNode(node, 'mainnet')
    pw.setChain('Vostok', 'V')

    print('number of payouts in batch: ' + str(len(batch)))
    print('batch: ' + str(batch))
    print('paid from address: ' + address.address)
    print('paid via node: ' + node)
    paid += len(batch)
    print('paying in West!')
    tx = address.massTransferWaves(batch, baseFee=10000000)
    print('tx: ' + str(tx))

with open(config['file']) as json_data:
        payments = json.load(json_data)
        currentBatch = []

        totalPayments = len(payments)
        for payment in payments:
                if (len(currentBatch) < 100):
                    currentBatch.append({ 'recipient': payment['recipient'], 'amount': payment['amount'] })
                    if (len(currentBatch) == 100):
                        pay(currentBatch)
                        currentBatch = []
                        time.sleep(config['timeout'] / 1000)
        if (len(currentBatch) > 0):
            pay(currentBatch)
        print('planned payouts: ' + str(totalPayments) + ', paid: ' + str(paid))
        usedTime = time.time() - startTime
        print('time: ' + str(usedTime) + ' (' + str(totalPayments / usedTime) + 'tx/s)')
