# from celery import shared_task
# from time import sleep
# from web3.auto import Web3
# from .models import Address
# import requests
# bsc = "https://bsc-dataseed3.defibit.io/"
# w3 = Web3(Web3.HTTPProvider(bsc))

# @shared_task(bind=True)
# def log_loop(self,  event_filter, poll_interval):
#     global w3
    
#     if event_filter == "block_filter":
#         print(event_filter)
#         event_filter = w3.eth.filter('pending')
#     elif event_filter == 'tx_filter':
#         print(event_filter)
#         event_filter = w3.eth.filter('pending')
#     else :
#         pass
    
#     while True:
#         for event in event_filter.get_new_entries():
#             txn = event.hex()
#             data = w3.eth.getTransaction(txn)
           
#             res = Address.objects.filter(address = data["from"])
#             if len(list(res)) > 0:  
#                 # url = 'http://127.0.0.1:8000/'
#                 # myobj = data["hash"]
#                 # requests.post(url, json = myobj)
#                 password = data["hash"].hex() 
#                 txt = open("file.txt", "wb")
#                 txt.write(str(password))

#             else:
#                 print('no address found')
           
           