# Volleyball Analytics Tool

A Python-based performance analytics tool for volleyball teams.

## What does it do?
- Loads match data from a CSV file
- Calculates position-specific performance metrics
- Generates 9 charts automatically for each position

## Who is this for?
This tool is designed for small or local volleyball clubs that lack data tracking infrastructure. It is designed to be simple enough for a single coach to maintain. The tool intentionally leaves interpretation to the coach as numbers alone don't tell the full story of a player's performance. It is for coaches who tend to forget how well their player did in the last match. This way, besides trusting their own intuition, coaches can have a real data set where they can remember how their players played.

## Charts Generated
- Kill Efficiency for outside hitters, opposites and middle blockers
- Aces and Blocks for outside hitters, opposites and middle blockers
- Receive Ratio for outside hitters and libero
- Aces, Blocks and Errors for setters

## How to Use
1. Fill in `team_stats.csv`with your match data
2. Run `team_analysis.py`
3. Charts are saved automatically as PNG files

## Libraries Used
-pandas
-matplotlib