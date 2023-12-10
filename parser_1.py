import pandas as pd

def preprocess_data(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # List of unnecessary fields to remove
    unnecessary_fields = [
        'PCT_PTS_2PT_MR', 'PCT_PF',
        'PCT_PTS_PAINT', 'PCT_PTS_FT', 'PCT_PFD', 'OPP_EFG_PCT', 'CFG_PCT',
        'TM_TOV_PCT', 'PCT_UAST_FGM', 'OREB_PCT', 'PCT_PTS_FB', 'PCT_AST_FGM',
        'UFG_PCT', 'PCT_FG3A', 'PCT_STL', 'DFG_PCT', 'OREB', 'AST', 'REB',
        'DFGA', 'SAST', 'OPP_PTS_2ND_CHANCE', 'PFD', 'TO', 'FG3A', 'STL',
        'POSS', 'PASS', 'UFGM', 'FG3M', 'PTS', 'UFGA', 'DRBC', 'OPP_PTS_PAINT',
        'FTM', 'ORBC', 'BLKA', 'PTS_FB', 'CFGA', 'PTS_PAINT', 'TCHS', 'CFGM',
        'PLUS_MINUS', 'DFGM', 'OPP_PTS_OFF_TOV', 'PTS_OFF_TOV', 'FGA', 'FTA',
        'PTS_2ND_CHANCE', 'FGM', 'PF', 'DREB', 'BLK', 'RBC', 'OPP_PTS_FB',
        'FTAST', 'E_OFF_RATING', 'OFF_RATING', 'E_NET_RATING', 'E_DEF_RATING',
        'NET_RATING', 'DEF_RATING', 'E_PACE', 'AST_RATIO', 'DIST', 'AST_TOV',
        'FTA_RATE', 'OPP_FTA_RATE', 'MIN', 'PACE_PER40', 'PACE', 'PIE'
    ]

    # Drop unnecessary fields from the DataFrame
    df = df.drop(columns=unnecessary_fields, errors='ignore')

    # Parse and format the GAME_DATE column to day-month-year
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE']).dt.strftime('%d-%m-%Y')

    # Save the preprocessed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "player_data.csv"
    output_file = "preprocessed_player_data.csv"
    preprocess_data(input_file, output_file)
