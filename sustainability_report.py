import os
from typing import List
import logging
from codecarbon import EmissionsTracker

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_python_files(directory: str) -> List[str]:
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(directory)
        for file in files if file.endswith('.py')
    ]

def execute_file(file_path: str) -> None:
    logging.info(f"Executing {file_path}...")
    try:
        with open(file_path, 'r') as file:
            exec(compile(file.read(), file_path, 'exec'), {'__name__': '__main__'})
    except Exception as e:
        logging.error(f"Error running {file_path}: {e}")

def run_code_files(directory: str) -> None:
    python_files = find_python_files(directory)
    if not python_files:
        logging.warning(f"No Python files found in {directory}.")
        return

    with EmissionsTracker() as tracker:
        for file_path in python_files:
            execute_file(file_path)

    logging.info(f"Total emissions: {tracker.final_emissions} kg CO2eq")

if __name__ == "__main__":
    CODE_DIRECTORY = 'camples'
    run_code_files(CODE_DIRECTORY)
