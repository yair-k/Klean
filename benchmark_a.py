from numba import jit, prange 
import numpy as np  
import time  

def compute_sum(n: int) -> int:

    total = 0  
    for i in prange(n):
        total += i  
    return total 
def compute_sum_numpy(n: int) -> int:

    return np.sum(np.arange(n))
def benchmark(func, n: int) -> None:

    start_time = time.time()  
    result = func(n) 
    end_time = time.time()  

    print(f"{func.__name__} result: {result}")
    print(f"{func.__name__} execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    n = 100_000_000  
    benchmark(compute_sum, n)
    benchmark(compute_sum_numpy, n)
