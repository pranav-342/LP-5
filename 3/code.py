
# download msmpi from chrom
# pip install mpi
# pip install mpi4py
# python (filename).py

from mpi4py import MPI

def distribute_array(arr, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()
    chunk_size = len(arr) // size
    start = rank * chunk_size
    end = start + chunk_size if rank < size - 1 else len(arr)
    return arr[start:end]

def compute_sum(arr):
    return sum(arr)

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()


    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    local_array = distribute_array(array, comm)


    local_sum = compute_sum(local_array)


    all_sums = comm.gather(local_sum, root=0)

    print("Processor", rank, "computed local sum:", local_sum)

 
    if rank == 0:
        final_sum = sum(all_sums)
        print("Final Sum:", final_sum)

if __name__ == "__main__":
    main()


