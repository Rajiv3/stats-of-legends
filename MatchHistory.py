import requests
import json
import os
from APIKey import api_key
from PlayerInfo import PlayerInfo
from ServerSettings import ServerSettings
from ChampionInfo import ChampionInfo
from FileStorage import FileStorage
from GameInfo import GameInfo
class MatchHistory:
    """Class to get and maintain the match history of a user"""
    # Note that there is a limit to how far back the data can be fetched
    # don't want to delete old data (how to solve? add to dictionary?)

    def __init__(self, summonerName, server = "na1", champion = "", queue = ""):
        self.summonerName = summonerName
        self.champion = champion
        self.queue = queue
        self.server = server
        self.serverSettings = ServerSettings(self.server)
        self.championInfo = ChampionInfo(self.server)
        self.fileStorage = FileStorage()
        self.playerInfo = PlayerInfo(self.summonerName, self.server)
        self.gameInfo = GameInfo(self.server)
    
    def checkPlayerData(self):
        """check if data for the user already exists, if not, build it"""
        pass

    def getMatchHistory(self):
        """get the match history with an API call"""
        if self.champion != "":
            champKey = self.championInfo.getChampionKeyOrId("IdKey", self.champion)
        else: 
            champKey = ""
        queueId = self.gameInfo.relevantQueueIds(self.queue)
        accountId = self.playerInfo.getAccountId()
        url = f"{self.serverSettings.api_prefix}{self.serverSettings.apiMatchlistAccountId}{accountId}?champion={champKey}&queue={queueId}&{self.serverSettings.api_suffix}"
        r = requests.get(url)
        print(f"Status code: {r.status_code}")

        matchHistory = r.json()

        return matchHistory
    
    def storeMatchHistory(self):
        """store the match history in a file"""
        self.fileStorage.makePath(f"{self.fileStorage.dataStoragePath}/{self.summonerName}")
        championFile = self.champion.replace(" ", "")
        queueFile = self.queue.title()
        filename = (f"{self.fileStorage.dataStoragePath}/{self.summonerName}/{self.summonerName}{championFile}{queueFile}MatchHistory.json").strip()

        matchHistory = self.getMatchHistory()   

        with open(filename, 'w') as f:
            json.dump(matchHistory, f, indent=4)
    
    def championsPlayed(self):
        """return a list of the champions played in the provided matchHistory"""
        # check the file, get a list, return it.
        pass
