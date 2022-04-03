import concurrent.futures
from app.worker import Customer
from config import customers
import time

def process_customer(customer):
    cust = Customer(customer)
    cust.execute()

def run():
    t1 = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_customer, customers)

    t2 = time.perf_counter()

    print(f'It took {t2 - t1} seconds!')
    
if __name__ == "__main__":
    run()