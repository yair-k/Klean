import concurrent.futures
import time
from typing import List, Callable, Any

def process_task(task_id: int) -> str:
    print(f"Processing task {task_id}")
    time.sleep(1)
    return f"Task {task_id} completed"

def parallel_processing(tasks: List[int], worker_function: Callable[[int], Any], max_workers: int = None) -> List[Any]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(worker_function, tasks))
    return results

def main():
    tasks = list(range(1, 11))
    start_time = time.time()
    results = parallel_processing(tasks, process_task)
    end_time = time.time()
    
    for result in results:
        print(result)
    
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
