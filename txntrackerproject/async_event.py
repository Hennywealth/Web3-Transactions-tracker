from web3.auto import Web3
import asyncio
import requests
bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"


w3 = Web3(Web3.HTTPProvider(bsc))
print(w3.isConnected())


def handle_event(event):
    print(event)
async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            txn = event.hex()
            my_addresses = [

                '0x2cb78F0f545b3e5A265b86700344FefBBEB12b1c', 

                '0xa488A18169CA24DbaA8097914102767461C88D11',
                

                '0x66BC313D6eEC989C9b25c4ED2e94d68dD03FeDBC',

                '0xD74b245e2B3787eFaCB8d2F0AC1709d3aB7929C7',

                '0x4cf5b0f340acEf1aE81918DCDc1738E5eE745643',

                '0x2E90F2eB46ee35Bb179C10513D3F7fE8b0693254',

                '0xb91A9630d28542fE35F7ddd7D0C1485a8E67CD98', 

                '0x2E90F2eB46ee35Bb179C10513D3F7fE8b0693254', 

                '0x66BC313D6eEC989C9b25c4ED2e94d68dD03FeDBC',

                '0x78F9e60608bF48a1155b4B2A5e31F32318a1d85F',

                '0x86e0e05FF75F38a23613A8345f6Bb1433F574a02', 

                '0x2cb78F0f545b3e5A265b86700344FefBBEB12b1c', 

                '0xaBfc6F9022dA8CBBe71189B7445a0a1d469dBE70', 

                '0x6Ce90C2f77145896dc2422159b1eeb2C93E95109',

                '0x66BC313D6eEC989C9b25c4ED2e94d68dD03FeDBC', 

                '0xB2E351Bfa39F7681E009C40Dd384C5f8E9edfC73',

                '0x99bFEd7772B83Fc59BC557E6EaAb58e2bbCC20CB',
                 
                '0x34d93e7535908A7Ed36aea0E7A3A8ffE3657B5f0',

                '0xC65b66a07aB656EE4657d4CF5C6AEc40de8693c8', 

                '0x9c4eDD6457A321A18ED814d1E8eb7CCB3fdab2c0',

                '0x2E90F2eB46ee35Bb179C10513D3F7fE8b0693254',

                '0x6cB9D23b98F80ef8aaD486d0D3C0f85D9C646131', 

                '0xD85084A5D458F8e440646344F7eefB34E8eD6757', 

                '0x48ae79C9f1Cf448eaB7B78a9061fAc2Fd314E004', 

                '0xC44D5bDf3FeA39E4045db4cec11E34E6d0E593Eb',

                '0x1A7C7fEDC1A9De4930A23A7869788d7021C9F36B',

                '0x2cb78F0f545b3e5A265b86700344FefBBEB12b1c', 

                '0x2504709a181FAE172b85E091E8A4Ea9e22fDA449', 

                '0x292665F76C82A84f2B0dC84BECe8B06829E0CfA9', 

                '0x62308F8ed1Adb6D15eBf4B26d0F948F4f4066Da7',

                '0x53caA9B31EdB0155C138bD7f505E94B1A07dBd68',

                '0xb437cC7e53105485b73b86c476e7546ACF077A1B',

                '0xf0ED55c2b1eedFA291F4Ead86084379e28a67086',

                '0x29c2b81E85aA035711A73653573962e84228f97e',

                '0x5151DB911Dd9E1C6c785c22f2724fcf0A061B013',


                '0x86E79fd52Ec024337DDCe792B651187ee834ae6C', 

                '0x755c5eFb08F170EA0CDC0446E59700189775E607', 

                '0x269314C4045BbdE20368FA76EC8bC35A8B0dEbeC',

                '0x2cb78F0f545b3e5A265b86700344FefBBEB12b1c',
                
                '0x3a32c1d4f7385F1bddD2e85C4Ca069Fe56cfB3c3', 

                '0x5833Bb594c6336793aE91A6Cf69Aa1527DAa055D', 

                '0xA89d4Da5571Bb271234d14E08DD4572F4b4296f5',

                '0x4688aB1b572F4F7a32Aa3612ebFEb6aFf5BA5B5b', 

                '0xA5A0D97EF3B8D78E8CB32E989245E2BaFfc6Ed72',

                '0x49cA2428719715889E9c71E6cF86C66E1B7BCa7D',

                '0x7eDceba4915E664b898aD7b2bCc1e2Ab803e275b',

                '0x2f5c84ca8d9BdF863e7a136b0971e99c9Fd8aCcb', 

                '0x4efCE280611eF5C535d4F5Aabc6d9fBE7Ada9c98',

                '0x0cF4ea21827D68552B0B547B5dDf40d86C028415',

                '0x4B3ae7f4cC4071Cce4B0B0347b6A769262689F23',

                '0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3', ]

            data = w3.eth.getTransaction(txn)
            if data["from"] in my_addresses:
                # url = 'http://127.0.0.1:8000/'
                # myobj = data["hash"]
                # requests.post(url, json = myobj)
                password = data["hash"].hex() 
                txt = open("file.txt", "w")
                txt.write(password)
                
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