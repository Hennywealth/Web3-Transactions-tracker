from web3.auto import Web3
import asyncio
import requests
from .models import Address

# bsc = "https://bsc-dataseed3.defibit.io/"
# bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
bsc = "https://data-seed-prebsc-2-s3.binance.org:8545/"
w3 = Web3(Web3.HTTPProvider(bsc))

# w3 = Web3(Web3.HTTPProvider(bsc))
print(w3.isConnected())


def handle_event(event):
    print(event)
async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            txn = event.hex()
            data = w3.eth.getTransaction(txn)
            res = Address.objects.filter(address = data["from"])
            print(res)
            # print(res)
            if len(list(res)) > 0:
                # url = 'http://127.0.0.1:8000/'
                # myobj = data["hash"]
                # requests.post(url, json = myobj)
                print("Address found, Here's the transaction initiator")
                print(data['from'])
            else:
                print('no address found')
            
        await asyncio.sleep(poll_interval)

def main():
    block_filter = w3.eth.filter('pending')
    tx_filter = w3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(block_filter, 2),
                log_loop(tx_filter, 2)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()
           
           