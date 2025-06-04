from statsbombpy import sb
import os
from dotenv import load_dotenv
import pandas as pd

def get_competitions():
    """
    Fetches all competitions from StatsBomb.
    """
    competitions = sb.competitions()
    return competitions

def get_matches(competition_id):
    """
    Fetches all matches for a given competition ID.
    
    Args:
        competition_id (int): The ID of the competition.
    
    Returns:
        DataFrame: A DataFrame containing match details.
    """
    matches = sb.matches(competition_id=competition_id)
    return pd.DataFrame(matches)

def get_events(match_id):
    """
    Fetches all events for a given match ID.
    
    Args:
        match_id (int): The ID of the match.
    
    Returns:
        DataFrame: A DataFrame containing event details.
    """
    events = sb.events(match_id=match_id)
    return pd.DataFrame(events)

def get_lineups(match_id):
    """
    Fetches lineups for a given match ID.
    
    Args:
        match_id (int): The ID of the match.
    
    Returns:
        DataFrame: A DataFrame containing lineup details.
    """
    lineups = sb.lineups(match_id=match_id)
    return pd.DataFrame(lineups)

def main():
    #fetches all the compitition data and saves it to a CSV file
    compititions = get_competitions()
    compititions_df = pd.DataFrame(compititions)
    compititions_df.to_csv('SampleData/competitions.csv', index=True)
    print("Competitions saved to SampleData/competitions.csv")
    

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()