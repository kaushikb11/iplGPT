from typing import List, Optional

from sqlmodel import Column, Field, SQLModel

from .utils import pydantic_column_type


class Matches(SQLModel, table=True):

    id: int = Field(primary_key=True)
    city: str
    date: str  # change it to datetime
    season: str
    match_number: str
    team1: str
    team2: str
    venue: str
    toss_winner: str
    toss_decision: str
    # super_over: bool
    team_winner: str
    won_by: str
    won_by_runs: Optional[int]
    win_by_wickets: Optional[int]
    player_of_match: Optional[str]
    team1_players: List[str] = Field(
        ..., sa_column=Column(pydantic_column_type(List[str]))
    )
    team2_players: List[str] = Field(
        ..., sa_column=Column(pydantic_column_type(List[str]))
    )
    umpire1: str
    umpire2: str
