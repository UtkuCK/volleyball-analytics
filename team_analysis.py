# Volleyball Performance Analytics Tool 
# Loads match data from CSV and generates position-specific performance charts
import pandas as pd
import matplotlib.pyplot as plt
# Load match data
df= pd.read_csv('team_stats.csv', sep='\t', encoding='cp1254')
# Calculate performance metrics
df['Kill_Efficiency'] = ((df['Kills'] - df['Errors']) / df['Attempts']).round(2)
df['Receive_Ratio'] = ((df['Perfect_Receives']) / df['Total_Receives']).round(2)
# Position labels
positions = { 'OH': 'Outside Hitter', 'OPP': 'Opposite','MB': 'Middle Blocker', 'S': 'Setter', 'L': 'Libero'}
# Print season summary per position
for pos_code, pos_name in positions.items():
    pos_df = df[df['Position'] == pos_code]
    if pos_df.empty:
         continue
    print (f'\n=== {pos_name} ===')
    print(pos_df[['Name', 'Match', 'Kills', 'Aces', 'Blocks', 'Errors', 'Kill_Efficiency',  'Receive_Ratio']].to_string(index=False))
# Generate kill efficiency trend charts for attacking positions
for pos_code in ['OH', 'OPP', 'MB']:
    pos_df = df[df['Position'] == pos_code]
    if pos_df.empty:
        continue
    plt.figure(figsize=(10, 5))
    for player in pos_df['Name'].unique():
          player_data = pos_df[pos_df['Name'] == player]
          plt.plot(player_data['Match'], player_data['Kill_Efficiency'], marker='o', label=player)
    plt.title(f'{positions[pos_code]} - Kill Efficiency Trend')
    plt.xlabel('Match')
    plt.ylabel('Kill Efficiency')  
    plt.xticks([1, 2, 3])
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{pos_code}_Kill_Efficiency_Trend.png')
    plt.close()

# Generate aces and blocks trend charts for attacking positions
for pos_code in ['OH', 'OPP', 'MB']:
    pos_df = df[df['Position'] == pos_code].copy()
    if pos_df.empty:
             continue
    plt.figure(figsize=(10, 5))
    for player in pos_df['Name'].unique():
        player_data = pos_df[pos_df['Name'] == player]
        plt.plot(player_data['Match'], player_data['Aces'], marker='o', label=f'{player} - Aces')
        plt.plot(player_data['Match'], player_data['Blocks'], marker='s', label=f'{player} - Blocks')
    plt.title(f'{positions[pos_code]} - Aces and Blocks Trend')
    plt.xlabel('Match')
    plt.ylabel('Count')
    plt.xticks([1, 2, 3])
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{pos_code}_Aces_Blocks_Trend.png')
    plt.close()
        
    # Generate receive ratio trend charts for the Outside Hitters and Libero
    for pos_code in ['OH', 'L']:
     pos_df = df[df['Position'] == pos_code].copy()
     if pos_df.empty:
         continue
     plt.figure(figsize=(10, 5))
     for player in pos_df['Name'].unique():
         player_data = pos_df[pos_df['Name'] == player]
         plt.plot(player_data['Match'], player_data['Receive_Ratio'], marker='o', label=player)
     plt.title(f'{positions[pos_code]} - Receive Ratio Trend')
     plt.xlabel('Match')
     plt.ylabel('Receive Ratio')
     plt.xticks([1, 2, 3])
     plt.legend()
     plt.tight_layout()
     plt.savefig(f'{pos_code}_Receive_Ratio_Trend.png')
     plt.close()

    # Generate aces, blocks and errors trend chart for the Setter
    pos_df = df[df['Position'] == 'S'].copy()
    plt.figure(figsize=(10, 5))
    for player in pos_df['Name'].unique():
        player_data = pos_df[pos_df['Name'] == player]
        plt.plot(player_data['Match'], player_data['Aces'], marker='o', label=f'{player} - Aces')
        plt.plot(player_data['Match'], player_data['Blocks'], marker='s', label=f'{player} - Blocks')
        plt.plot(player_data['Match'], player_data['Errors'], marker='x', label=f'{player} - Errors')
    plt.title('Setter - Aces, Blocks and Errors Trend')
    plt.xlabel('Match')
    plt.ylabel('Count')
    plt.xticks([1, 2, 3])
    plt.legend()
    plt.tight_layout()
    plt.savefig('S_Aces_Blocks_Errors.png')
    plt.close()
    
print('All charts saved!')