import time

start = time.perf_counter()

def do_sth():
    print("Sleeping in 1 second")
    time.sleep(1)
    print("Sleeping done")

do_sth()

finish = time.perf_counter()    

print(f"Time taken: {finish - start}")
