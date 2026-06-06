--DATA CLEANING AND SEASON WISE ANALYSIS--

import pandas as pd
import numpy as np
df = pd.read_csv("deliveries.csv")
dismissal_cols = [
    "player_dismissed",
    "dismissal_kind",
    "fielder"
]

for col in dismissal_cols:
    if col in df.columns:
        df[col] = df[col].fillna("Not Out")
extra_cols = [
    "wide_runs",
    "bye_runs",
    "legbye_runs",
    "noball_runs",
    "penalty_runs",
    "extra_runs"
]

for col in extra_cols:
    if col in df.columns:
        df[col] = df[col].fillna(0)
season_map = {
    range(1, 59): 2008,
    range(59, 118): 2009,
    range(118, 178): 2010,
    range(178, 252): 2011,
    range(252, 327): 2012,
    range(327, 403): 2013,
    range(403, 463): 2014,
    range(463, 523): 2015,
    range(523, 583): 2016,
    range(583, 643): 2017,
    range(643, 703): 2018,
    range(703, 763): 2019,
    range(763, 823): 2020,
    range(823, 884): 2021,
    range(884, 945): 2022,
    range(945, 1005): 2023
}

def get_season(match_id):
    for r, season in season_map.items():
        if match_id in r:
            return season
    return np.nan

df["season"] = df["match_id"].apply(get_season)
df = df.dropna(subset=["season"])
kohli = df[df["batter"] == "V Kohli"].copy()
kohli["legal_ball"] = np.where(kohli["wide_runs"] == 0, 1, 0)
season_runs = kohli.groupby("season")["batsman_runs"].sum()

season_balls = (
    kohli.groupby("season")["legal_ball"]
    .sum()
)

season_matches = (
    kohli.groupby("season")["match_id"]
    .nunique()
)

season_outs = (
    kohli[kohli["player_dismissed"] == "V Kohli"]
    .groupby("season")
    .size()
)

season_fours = (
    kohli[kohli["batsman_runs"] == 4]
    .groupby("season")
    .size()
)

season_sixes = (
    kohli[kohli["batsman_runs"] == 6]
    .groupby("season")
    .size()
)

summary = pd.DataFrame({
    "Matches": season_matches,
    "Runs": season_runs,
    "Outs": season_outs,
    "Balls": season_balls,
    "4s": season_fours,
    "6s": season_sixes
}).fillna(0)

summary["Average"] = (
    summary["Runs"] / summary["Outs"]
).round(2)

summary["Strike Rate"] = (
    summary["Runs"] * 100 / summary["Balls"]
).round(2)

summary = summary.reset_index()

print(summary)

summary.to_csv(
    "virat_kohli_ipl_season_summary.csv",
    index=False
)

summary.to_excel(
    "virat_kohli_ipl_season_summary.xlsx",
    index=False
)

--Opponent Analysis--

  kohli["legal_ball"] = np.where(
    kohli["wide_runs"] == 0,
    1,
    0
)

opp_runs = kohli.groupby("bowling_team")["batsman_runs"].sum()
opp_balls = kohli.groupby("bowling_team")["legal_ball"].sum()
opp_innings = kohli.groupby("bowling_team")["match_id"].nunique()

opp_outs = (
    kohli[kohli["player_dismissed"] == "V Kohli"]
    .groupby("bowling_team")
    .size()
)

opp_fours = (
    kohli[kohli["batsman_runs"] == 4]
    .groupby("bowling_team")
    .size()
)

opp_sixes = (
    kohli[kohli["batsman_runs"] == 6]
    .groupby("bowling_team")
    .size()
)

opponent_summary = pd.DataFrame({
    "Innings": opp_innings,
    "Runs": opp_runs,
    "Outs": opp_outs,
    "Balls": opp_balls,
    "4s": opp_fours,
    "6s": opp_sixes
}).fillna(0)

opponent_summary["Average"] = (
    opponent_summary["Runs"] /
    opponent_summary["Outs"]
).round(2)

opponent_summary["Strike Rate"] = (
    opponent_summary["Runs"] * 100 /
    opponent_summary["Balls"]
).round(2)

opponent_summary = (
    opponent_summary
    .sort_values("Runs", ascending=False)
)

opponent_summary.to_csv(
    "virat_kohli_by_opponent.csv"
)
---Powerplay / Middle / Death Overs Analysis---

def get_phase(over):
    if over <= 6:
        return "Powerplay"
    elif over <= 15:
        return "Middle Overs"
    else:
        return "Death Overs"

kohli["phase"] = kohli["over"].apply(get_phase)

phase_runs = kohli.groupby("phase")["batsman_runs"].sum()
phase_balls = kohli.groupby("phase")["legal_ball"].sum()

phase_outs = (
    kohli[kohli["player_dismissed"] == "V Kohli"]
    .groupby("phase")
    .size()
)

phase_fours = (
    kohli[kohli["batsman_runs"] == 4]
    .groupby("phase")
    .size()
)

phase_sixes = (
    kohli[kohli["batsman_runs"] == 6]
    .groupby("phase")
    .size()
)

phase_summary = pd.DataFrame({
    "Runs": phase_runs,
    "Balls": phase_balls,
    "Outs": phase_outs,
    "4s": phase_fours,
    "6s": phase_sixes
}).fillna(0)

phase_summary["Average"] = (
    phase_summary["Runs"] /
    phase_summary["Outs"]
).round(2)

phase_summary["Strike Rate"] = (
    phase_summary["Runs"] * 100 /
    phase_summary["Balls"]
).round(2)

phase_summary.to_csv(
    "virat_kohli_by_phase.csv"
)
---Dismissal Analysis---
  dismissals = (
    kohli[kohli["player_dismissed"] == "V Kohli"]
    ["dismissal_kind"]
    .value_counts()
    .reset_index()
)

dismissals.columns = [
    "Dismissal Type",
    "Times"
]

dismissals.to_csv(
    "virat_kohli_dismissals.csv",
    index=False
)

print(dismissals)
