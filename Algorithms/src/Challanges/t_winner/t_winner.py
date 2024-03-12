# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

* 2 Team x time
* each competition , one team -> home team , other -> away team
* 1 winner and 1 loser
* No Ties
* Winner: 3 points
* Loser: 0 points
* Winner = most points


* 1 array teams have competest
* 1 array result of each competition
* Return winner of the tournament

* competition. [home_team, away_team]
* results: result is indexed . 1 = home_team won 0 = away_team won


* 1 Team will win
* all team compete excatly once
* Tournament always have 2 teams


"""
import math
from pprint import pprint


def first_solution(competitions: list, results: list) -> str:
    # Add competitors in the competitors table
    competitor_table = {competitor: 0
                        for competition in competitions
                        for competitor in competition
                        }


    winner = ''
    for round, competition in enumerate(competitions):
        [home_team, away_team] = competition
        score = results[round]
        if score == 1: # Home team wins
            competitor_table[home_team] += 1
            continue
        competitor_table[away_team] += 1

    max_value = 0
    for scores in competitor_table.items():
        score = scores[-1]
        if score > max_value:
            max_value = score
            winner = scores[0]


    return winner

def second_solution(competitions: list, results: list) -> str:
    # Add competitors in the competitors table
    competitor_table = {competitor: 0
                        for competition in competitions
                        for competitor in competition
                        }

    winner = ''
    for round, competition in enumerate(competitions):
        [home_team, away_team] = competition
        score = results[round]
        if score == 1: # Home team wins
            competitor_table[home_team] += 1
            continue
        competitor_table[away_team] += 1
    # now reverse the mapping
    score_mapping = {score: player for player, score in competitor_table.items()}
    max_score = max(score_mapping.keys())
    return score_mapping[max_score]


if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]
    expected = "Python"
    result = first_solution(competitions, results)
    assert result == expected

    result = second_solution(competitions, results)
    assert result == expected