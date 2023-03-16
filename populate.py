import ast

import pandas as pd
from sqlmodel import Session, SQLModel, create_engine

from ipl_gpt.models import Matches

sqlite_file_name = "ipl.sqlite"

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def create_matches(csv_file: str) -> None:
    matches = pd.read_csv(csv_file)

    with Session(engine) as session:
        for _, match in matches.iterrows():
            match_object = Matches(
                id=match.ID,
                city=match.City,
                date=str(match.Date),
                season=int(match.Season),
                match_number=match.MatchNumber,
                team1=match.Team1,
                team2=match.Team2,
                venue=match.Venue,
                toss_winner=match.TossWinner,
                toss_decision=match.TossDecision,
                team_winner=match.WinningTeam,
                won_by=match.WonBy,
                won_by_runs=match.WonByRuns,
                won_by_wickets=match.WonByWickets,
                player_of_match=match.Player_of_Match,
                team1_players=ast.literal_eval(match.Team1Players),
                team2_players=ast.literal_eval(match.Team2Players),
                umpire1=match.Umpire1,
                umpire2=match.Umpire2,
            )
            session.add(match_object)

        session.commit()


if __name__ == "__main__":
    create_db_and_tables()

    matches_csv_file = "./data/matches.csv"
    create_matches(matches_csv_file)
