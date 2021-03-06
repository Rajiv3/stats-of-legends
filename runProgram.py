from PlayerInfo import PlayerInfo
from MatchHistory import MatchHistory
from ChampionInfo import ChampionInfo
from GameInfo import GameInfo
from MatchStats import MatchStats

def main():

    gameInfo = GameInfo()
    gameInfo.storeQueueIds()
    gameInfo.storeSeasoninfo()
    gameInfo.storeMapInfo()
    gameInfo.storeGameModeInfo()
    gameInfo.storeGameTypeInfo()


    champions = ChampionInfo()
    champions.storeChampionJson()
    champions.storeChampionPairs("IdKey")
    champions.storeChampionPairs("KeyId")
    print(champions.getChampionKeyOrId("IdKey", "Anivia"))


    summonerName = input("Summoner Name: ")
    summoner = PlayerInfo(summonerName, "na1")
    summoner.storePlayerInfo()

    summonerMatchHistory = MatchHistory(summonerName, server="na1", queue="solo", champion="")
    summonerMatchHistory.storeMatchHistory()
    summonerMatchHistory.storeMasterMatchHistory()
    summonerMatchHistory.storeGameIds()
    print(summonerMatchHistory.getChampionsPlayed())
    print(summonerMatchHistory.countChampionsPlayed())
    summonerMatchHistory.displayPlots()
    summonerMatchHistory.storeDetailedMatchData()
    summonerMatchHistory.deleteMatchHistoryFile()

    summonerMatchStats = MatchStats(summonerName, server = "na1", queue = "solo",  champion = "")
    print(summonerMatchStats.getCsValues())
    summonerMatchStats.displayPlots()


if __name__ == "__main__":
    main()
