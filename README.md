# Volleyball Analytics Tool

A Python-based performance analytics tool for volleyball teams.

## What does it do?
- Loads match data from a CSV file
- Calculates position-specific performance metrics
- Generates 9 charts automatically for each position

## Who is this for?
 Most professional clubs have access to advanced analytics platforms. Small and local volleyball clubs don't. Coaches at this level make decisions based on memory and intuition alone. This tool was built by a competitive volleyball player who experienced this gap firsthand, giving grassroots clubs a simple, accessible way to track player performance across a season without any technical expertise required.

## Charts Generated
- Kill Efficiency for outside hitters, opposites and middle blockers
- Aces and Blocks for outside hitters, opposites and middle blockers
- Receive Ratio for outside hitters and libero
- Aces, Blocks and Errors for setters

## How to Use
1. Fill in `team_stats.csv` with your match data
2. Run `team_analysis.py`
3. Charts are saved automatically as PNG files

## Libraries Used
-pandas
-matplotlib