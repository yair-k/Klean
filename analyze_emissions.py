import pandas as pd

def save_emissions_data(data, filename='emissions_data.csv'):
    df = pd.DataFrame(data)
    
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    emissions_data = [
        {'timestamp': '2024-07-13 12:00:00', 'energy_consumed': 12.5, 'carbon_emitted': 0.011},
        {'timestamp': '2024-07-13 12:10:00', 'energy_consumed': 8.2, 'carbon_emitted': 0.0024},
        {'timestamp': '2024-07-13 12:20:00', 'energy_consumed': 4.3, 'carbon_emitted': 0.0018},
    ]
    save_emissions_data(emissions_data)
