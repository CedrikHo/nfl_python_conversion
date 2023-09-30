import json
import csv
import math

import numpy as np
from tabulate import tabulate
import pandas as pd
import json


def filter_out_unwanted_col(list_of_wanted_col, df):
    ''' Need to drop all col in data frame that are not wanted to not make a mess'''
    all_col = df.columns.values
    for name in all_col:
        if (name not in list_of_wanted_col):
            del df[name]
    return df


if __name__ == '__main__':


    #with open('source_total_1249_week1.json') as a:
    a = '''
    {
      "PlayerID": 4314,
      "Season": 2021,
      "Played": 1,
      "Started": 1,
      "Week": 1,
      "Opponent": "DAL",
      "TeamHasPossession": false,
      "HomeOrAway": null,
      "TeamIsHome": true,
      "Result": "W",
      "HomeScore": 31,
      "AwayScore": 29,
      "Quarter": "F",
      "QuarterDisplay": "F",
      "IsGameOver": true,
      "GameDate": "/Date(1631233200000)/",
      "TimeRemaining": null,
      "ScoreSummary": "F (W) 31 - 29 vs. DAL",
      "PassingCompletions": 32,
      "PassingAttempts": 50,
      "PassingCompletionPercentage": 64,
      "PassingYards": 379,
      "PassingYardsPerAttempt": 7.6,
      "PassingTouchdowns": 4,
      "PassingInterceptions": 2,
      "PassingRating": 97,
      "RushingAttempts": 0,
      "RushingYards": 0,
      "RushingYardsPerAttempt": 0,
      "RushingTouchdowns": 0,
      "Receptions": 0,
      "ReceivingTargets": 0,
      "ReceivingYards": 0,
      "ReceptionPercentage": 0,
      "ReceivingTouchdowns": 0,
      "ReceivingLong": 0,
      "ReceivingYardsPerTarget": 0,
      "ReceivingYardsPerReception": 0,
      "Fumbles": 0,
      "FumblesLost": 0,
      "FieldGoalsMade": 0,
      "FieldGoalsAttempted": 0,
      "FieldGoalPercentage": 0,
      "FieldGoalsLongestMade": 0,
      "ExtraPointsMade": 0,
      "ExtraPointsAttempted": 0,
      "TacklesForLoss": 0,
      "Sacks": 0,
      "QuarterbackHits": 0,
      "Interceptions": 0,
      "FumblesRecovered": 0,
      "Safeties": 0,
      "DefensiveTouchdowns": 0,
      "SpecialTeamsTouchdowns": 0,
      "SoloTackles": 0,
      "AssistedTackles": 0,
      "SackYards": 0,
      "PassesDefended": 0,
      "FumblesForced": 0,
      "FantasyPoints": 27.16,
      "FantasyPointsPPR": 27.16,
      "FantasyPointsFanDuel": 29.16,
      "FantasyPointsYahoo": 29.16,
      "FantasyPointsFantasyDraft": 32.16,
      "FantasyPointsDraftKings": 32.16,
      "FantasyPointsHalfPointPpr": 27.16,
      "FantasyPointsSixPointPassTd": 35.16,
      "FantasyPointsPerGame": 27.2,
      "FantasyPointsPerGamePPR": 27.2,
      "FantasyPointsPerGameFanDuel": 29.2,
      "FantasyPointsPerGameYahoo": 29.2,
      "FantasyPointsPerGameDraftKings": 32.2,
      "FantasyPointsPerGameHalfPointPPR": 27.2,
      "FantasyPointsPerGameSixPointPassTd": 35.2,
      "FantasyPointsPerGameFantasyDraft": 32.2,
      "PlayerUrlString": "/nfl/tom-brady-fantasy/4314",
      "GameStatus": "",
      "GameStatusClass": "",
      "PointsAllowedByDefenseSpecialTeams": null,
      "UsaTodayHeadshotNoBackgroundUrlSlug": "tom-brady-4314-6bb21da3",
      "TotalTackles": 0,
      "StatSummary": [
        {
          "Items": [
            {
              "StatValue": "32/50",
              "StatTitle": ""
            },
            {
              "StatValue": "379",
              "StatTitle": "YDS"
            },
            {
              "StatValue": "4",
              "StatTitle": "TD"
            },
            {
              "StatValue": "2",
              "StatTitle": "INT"
            }
          ]
        },
        {
          "Items": [
            {
              "StatValue": "QB RAT 97",
              "StatTitle": ""
            },
            {
              "StatValue": "64",
              "StatTitle": "%"
            },
            {
              "StatValue": "7.6",
              "StatTitle": "YDS/ATT"
            }
          ]
        }
      ],
      "Name": "Tom Brady",
      "ShortName": "T. Brady",
      "FirstName": "Tom",
      "LastName": "Brady",
      "FantasyPosition": "QB",
      "Position": "QB",
      "TeamUrlString": "/nfl/tampa-bay-buccaneers-depth-chart",
      "Team": "TB",
      "IsScrambled": false,
      "Rank": 8,
      "StaticRank": 0,
      "PositionRank": null,
      "IsFavorite": false
    }
    '''
    RawDict = json.load(a)
    print(type(RawDict))
    # print(RawDict)
    list_of_entries_per_player = RawDict["Data"]
    print(type(list_of_entries_per_player))
    first_player_in_list = list_of_entries_per_player[0]
    print(type(first_player_in_list))
    print("This is the first player in the list total data type : \n")
    print(str(first_player_in_list))
    df = pd.DataFrame(first_player_in_list)

    for player in list_of_entries_per_player:
        print(type(player))
        print("This is dict data : " + str(player))
        # print("Starting dictData Print \n")
        # print(dictData)
        # print(type(dictData))
        # print("Starting Data from json print")
        # print(dictData['Data'])
        # real_Data = dictData['Data']
        # print(type(real_Data)) # type list
        # df = pd.DataFrame(player)
        # df.to_csv(r'C:\Users\cedri\PycharmProjects\pythonProjectNFLDataJsonConversion\nfl_Data_test\my_data.csv', index=False)
        # print(df)
        # print(tabulate(df, headers='keys', tablefmt='psql'))
        df = df.append(player, ignore_index=True)
        print(df)

    white_list = ["FantasyPosition", "Team", "Season", "Name", "Week", "Position", "PassingYards", "RushingYards",
                  "PassingYards", "ReceivingTouchdowns", "RushingTouchdowns", "PassingTouchdowns", "Fumbles",
                  "FumblesLost", "PassingInterceptions", "SoloTackles", "AssistedTackles", "PassesDefended",
                  "Sacks", "Safeties", "SpecialTeamsTouchdowns", "Interceptions", "FumblesForced",
                  "ExtraPointsMade", "FieldGoalsLongestMade", "ReceivingYards"]
    cleaned_up_df = filter_out_unwanted_col(white_list, df)
    print(tabulate(cleaned_up_df, headers='keys', tablefmt='psql'))

    # read in the fixed csv file
    '''
    Each person has a team with weekly drafted players. 
    This needs to be a single file with a very standard format. Any change will cause issues. 
    '''
    "PassingYards", "RushingYards",
    "PassingYards", "ReceivingTouchdowns", "RushingTouchdowns", "PassingTouchdowns", "Fumbles",
    "FumblesLost", "PassingInterceptions", "SoloTackles", "AssistedTackles", "PassesDefended",
    "Sacks", "Safeties", "SpecialTeamsTouchdowns", "Interceptions", "FumblesForced",
    "ExtraPointsMade", "FieldGoalsLongestMade, ReceivingYards"

    ##################Offensive##########################33
    df['PassingYards_PTS'] = ((df['PassingYards'] / 25).apply(np.floor))
    df['RushingYards_PTS'] = ((df['RushingYards']) / 10).apply(np.floor)
    df['ReceivingYards_PTS'] = ((df['ReceivingYards']).apply(np.floor) / 10).apply(np.floor)
    df['ReceivingTouchdowns_PTS'] = ((df['ReceivingTouchdowns']).apply(np.floor) * 6).apply(np.floor)
    df['PassingTouchdowns_PTS'] = ((df['PassingTouchdowns']).apply(np.floor) * 6).apply(np.floor)
    df['RushingTouchdowns_PTS'] = ((df['RushingTouchdowns']).apply(np.floor) * 4).apply(np.floor)
    df['Fumbles_Lost_PTS'] = ((df['Fumbles']).apply(np.floor).apply(np.floor) * -2 + (df['FumblesLost'] * -2)).apply(np.floor)
    df['Interception_Offensive_PTS'] = (df['PassingInterceptions'].apply(np.floor) * -2).apply(np.floor)

    df['Total_Offensive_PTS'] = df['PassingYards_PTS'] + df['RushingYards_PTS'] + df['ReceivingYards_PTS'] + df[
        'ReceivingTouchdowns_PTS'] + df['PassingTouchdowns_PTS'] + df['RushingTouchdowns_PTS'] + df[
                                    'Fumbles_Lost_PTS'] + df['Interception_Offensive_PTS']
    ###########DEFENSIVE########################
    df['AssistedTackles_PTS'] = ((df['AssistedTackles']).apply(np.floor) * 1).apply(np.floor)
    df['SoloTackles_PTS'] = ((df['SoloTackles']).apply(np.floor) * 1).apply(np.floor)
    df['PassesDefended_PTS'] = ((df['PassesDefended']).apply(np.floor) * 1).apply(np.floor)
    df['Sacks_PTS + Assisted Sacks_PTS'] = ((df['Sacks']).apply(np.floor) * 4).apply(np.floor)
    df['Safeties_PTS'] = ((df['Safeties']).apply(np.floor) * 2).apply(np.floor)
    df['SpecialTeamsTouchdowns_PTS'] = ((df['SpecialTeamsTouchdowns']).apply(np.floor) * 6).apply(np.floor)
    df['Interception_Defensive_PTS'] = ((df['Interceptions']).apply(np.floor) * 6).apply(np.floor)
    df['SpecialTeamsTouchdowns_PTS'] = ((df['SpecialTeamsTouchdowns']).apply(np.floor) * 6).apply(np.floor)
    df['FumblesForced_PTS'] = ((df['FumblesForced']).apply(np.floor) * 4).apply(np.floor)

    df['Total_defensive_PTS'] = df['AssistedTackles_PTS'] + df['SoloTackles_PTS'] + df['PassesDefended_PTS'] + df[
        'Sacks_PTS + Assisted Sacks_PTS'] + df['Safeties_PTS'] + df['SpecialTeamsTouchdowns_PTS'] + df[
                                    'Interception_Defensive_PTS'] + df['SpecialTeamsTouchdowns_PTS'] + df[
                                    'FumblesForced_PTS']
    ###################KICKING########################
    df['FieldGoalsLongestMade_PTS'] = (df['FieldGoalsLongestMade'] // 10).apply(np.floor)
    df['ExtraPointsMade_PTS'] = (df['ExtraPointsMade'].apply(np.floor) * 1).apply(np.floor)
    df['Total_Kicking_PTS'] = df['FieldGoalsLongestMade_PTS'].apply(np.floor) + df['ExtraPointsMade_PTS'].apply(np.floor)


    ##################Force the round down###########################
    #################################################################

    ####################OFFENSIVE#########################33
    df['PassingYards'] = df['PassingYards'].apply(np.floor)
    df['RushingYards'] = (df['RushingYards']).apply(np.floor)
    df['ReceivingYards'] = (df['ReceivingYards']).apply(np.floor)
    df['ReceivingTouchdowns'] = (df['ReceivingTouchdowns']).apply(np.floor)
    df['PassingTouchdowns_'] = (df['PassingTouchdowns']).apply(np.floor)
    df['RushingTouchdowns'] = (df['RushingTouchdowns']).apply(np.floor)
    df['Fumbles_Lost'] = ((df['Fumbles']).apply(np.floor) + (df['FumblesLost'])).apply(np.floor)
    df['Interception_Offensive'] = (df['PassingInterceptions']).apply(np.floor)

    ###########DEFENSIVE########################
    df['AssistedTackles'] = (df['AssistedTackles']).apply(np.floor)
    df['SoloTackles'] = (df['SoloTackles']).apply(np.floor)
    df['PassesDefended'] = (df['PassesDefended']).apply(np.floor)
    df['Sacks'] = (df['Sacks']).apply(np.floor)
    df['Safeties'] = (df['Safeties']).apply(np.floor)
    df['SpecialTeamsTouchdowns'] = (df['SpecialTeamsTouchdowns']).apply(np.floor)
    df['Interception_Defensive'] = (df['Interceptions']).apply(np.floor)
    df['SpecialTeamsTouchdowns'] = (df['SpecialTeamsTouchdowns']).apply(np.floor)
    df['FumblesForced'] = (df['FumblesForced']).apply(np.floor)

    ###################KICKING########################
    df['FieldGoalsLongestMade'] = (df['FieldGoalsLongestMade']).apply(np.floor)
    df['ExtraPointsMade'] = (df['ExtraPointsMade']).apply(np.floor)
    df['Total_Kicking'] = df['FieldGoalsLongestMade_PTS'].apply(np.floor) + df['ExtraPointsMade_PTS'].apply(np.floor)


    #####swap to help readability##########


    df.set_index(df.pop('Name'), inplace=True)
    df.reset_index(inplace=True)
    df.set_index(df.pop('FantasyPosition'), inplace=True)
    df.reset_index(inplace=True)

    df.to_csv(r'C:\Users\cedri\PycharmProjects\pythonProjectNFLDataJsonConversion\nfl_Data_test\my_data.csv',
              index=False)

    print(tabulate(cleaned_up_df, headers='keys', tablefmt='psql'))
