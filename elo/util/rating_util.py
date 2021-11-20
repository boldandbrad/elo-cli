import math
from typing import Tuple

from elo.model.player import Player

PRECISION = 1
K_FACTOR = 20
WIN = 1
LOSE = 0
DRAW = 0.5


def _win_probability(home_elo: float, away_elo: float) -> Tuple[float, float]:
    """Calculate probability that either side would win the match.

    Args:
        home_elo (float): current elo rating of the home side
        away_elo (float): current elo rating of the away side

    Returns:
        Tuple[float, float]: home and away win probabilities
    """
    home_prob = 1.0 / (1 + math.pow(10, (away_elo - home_elo) / 400))
    return home_prob, 1.0 - home_prob


def _score_weight(home_score: int, away_score: int) -> float:
    """Calculate score difference weight to be applied to new elo ratings.

    Args:
        home_score (int): score of the home side in the match
        away_score (int): score of the away side in the match

    Returns:
        float: weighted value to be applied to elo calculation
    """
    score_diff = abs(home_score - away_score)

    if score_diff == 0 or score_diff == 1:
        return 1
    elif score_diff == 2:
        return 1.25
    else:
        return (11 + score_diff) / 10


def _calculate_elo(
    current_elo: float, win_prob: float, weight: float, match_outcome: float
) -> float:
    """Calculate a side's new elo rating.

    Args:
        elo (float): current elo rating of side
        prob (float): win probability of side
        weight (float): weighted value to be applied to rating based on score difference of match
        outcome (float): match outcome of side (1 - win, 0 - lose, 0.5 - draw)

    Returns:
        float: new elo rating of side
    """
    net_change = (K_FACTOR * weight) * (match_outcome - win_prob)
    new_elo = current_elo + net_change
    return round(new_elo, PRECISION)


def update_elos(
    home_elo: float, away_elo: float, home_score: int, away_score: int
) -> Tuple[float, float, float]:
    """Update both side's elo ratings based on match outcome.

    Args:
        home_elo (float): current elo rating of the home side
        away_elo (float): current elo rating of the away side
        home_score (int): score of the home side in the match
        away_score (int): score of the away side in the match

    Returns:
        Tuple[float, float, float]: new home elo, new away elo, net change
    """
    orig_home_elo = home_elo

    home_prob, away_prob = _win_probability(home_elo, away_elo)
    weight = _score_weight(home_score, away_score)

    if home_score > away_score:
        # home won
        home_outcome = WIN
        away_outcome = LOSE
    elif home_score < away_score:
        # away won
        home_outcome = LOSE
        away_outcome = WIN
    else:
        # draw
        home_outcome = DRAW
        away_outcome = DRAW

    home_elo = _calculate_elo(home_elo, home_prob, weight, home_outcome)
    away_elo = _calculate_elo(away_elo, away_prob, weight, away_outcome)

    net_change = abs(orig_home_elo - home_elo)

    return home_elo, away_elo, net_change


def update_stats(
    home_player: Player, away_player: Player, home_score: int, away_score: int
) -> None:
    """Update both player's statistics from match outcome."""
    home_player.points_for += home_score
    home_player.points_against += away_score
    away_player.points_for += away_score
    away_player.points_against += home_score

    # home won
    if home_score > away_score:
        home_player.wins += 1
        away_player.losses += 1
    # away won
    elif home_score < away_score:
        home_player.losses += 1
        away_player.wins += 1
    # draw
    else:
        home_player.draws += 1
        away_player.draws += 1
