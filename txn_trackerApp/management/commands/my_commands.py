# from django.core.management.base import BaseCommand
# from web3.auto import Web3

# import time
# # from . import tasks
# bsc = "https://bsc-dataseed.binance.org/"
# w3 = Web3(Web3.HTTPProvider(bsc))
# print(w3.isConnected())

# class Command(BaseCommand):
#     def handle(self, event_filter, poll_interval):
#        while True:
#         for event in event_filter.get_new_entries():
#             txn = event.hex()
#             my_addresses = ['0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea', '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea', '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea', '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea', '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea', '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea']
#             data = w3.eth.getTransaction(txn)
#             if data["from"] in my_addresses:
#                 print(data)
#             else:
#                 print('no address found')            
#             print(data)
#         time.sleep(poll_interval)


# block_filter = w3.eth.filter('pending')
# com = Command()
# com.handle(block_filter, 2)