import requests
import multiprocessing.pool

url = 'https://www.example.com'
count = 100000

def make_request(i):
    with requests.Session() as session:
        response = session.get(url)
    if response.status_code == 200:
        return f'Response {i + 1}: Site up'
    else:
        return f'Response {i + 1}: Site down'

if __name__ == '__main__':
    with multiprocessing.pool.ThreadPool(processes=multiprocessing.cpu_count()) as pool:
        for result in pool.imap(make_request, range(count), chunksize=20): # Chunksize1 = 4 req / sec
            print(result)