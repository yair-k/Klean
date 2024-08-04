import cupy as cp
import numpy as np
import time

def gpu_acceleration_example(n: int):
    a_gpu = cp.arange(n)
    b_gpu = cp.arange(n)
    start_time = time.time()
    c_gpu = a_gpu + b_gpu
    cp.cuda.Stream.null.synchronize()
    end_time = time.time()
    return c_gpu, end_time - start_time

def cpu_acceleration_example(n: int):
    a_cpu = np.arange(n)
    b_cpu = np.arange(n)
    start_time = time.time()
    c_cpu = a_cpu + b_cpu
    end_time = time.time()
    return c_cpu, end_time - start_time

if __name__ == "__main__":
    n = 100_000_000
    gpu_result, gpu_time = gpu_acceleration_example(n)
    print(f"GPU Execution Time: {gpu_time:.6f} seconds")
    cpu_result, cpu_time = cpu_acceleration_example(n)
    print(f"CPU Execution Time: {cpu_time:.6f} seconds")
    speedup = cpu_time / gpu_time
    print(f"GPU Speedup: {speedup:.2f}x")
