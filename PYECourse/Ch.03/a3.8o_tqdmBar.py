# Ch.03 Exercise 3.8 Officail Answer
# Progress Bar using tqdm library

from tqdm import tqdm
from time import sleep

for i in tqdm(range(1, 100)):
    sleep(0.01)
