from riotwatcher import ValWatcher, TftWatcher, ApiError
from collections import OrderedDict
import pandas as pd
import json

# golbal variables
api_key = 'enter-your-api-key'
my_val_region = 'NA'
my_tft_server = 'na1'
my_val_localized = 'en-US'
my_match_history_count = 10

# Assume valid Summoner Name
user_input_summonerName = input("Enter Summoner Name: ")
my_val_name = user_input_summonerName

# Output file
user_input_summonerName_server_filename = my_val_name + '_' + my_val_region + '_val_file.txt'

#Val global variables
val_watcher = ValWatcher(api_key)
tft_watcher = TftWatcher(api_key)

# my_val = val_watcher.match.matchlist_by_puuid(my_val_region, my_val_name)

my_tft = tft_watcher.summoner.by_name(my_tft_server, user_input_summonerName)
my_puuid = my_tft["puuid"]
my_val = val_watcher.match.matchlist_by_puuid(my_val_region, my_puuid)

print('\n\n\n this is my puuid' + my_puuid + '\n')
# my_val = val_watcher.summoner.by_name(my_val_server, user_input_summonerName)
# my_val_rank = val_watcher.league.by_summoner(my_val_server, my_val['id'])
# my_tft_matches = val_watcher.match.by_puuid(my_tft_region, my_tft["puuid"], my_match_history_count)


# with open(user_input_summonerName_server_filename, 'w') as val_file:
#     val_file.write("Summoner Name: " + my_val_name + "\n")
    # tft_file.write("Rank: " + my_val_rank + "\n\n\n\n")