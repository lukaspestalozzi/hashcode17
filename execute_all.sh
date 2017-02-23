#!/bin/bash

zip submission.zip *.py &
cat kittens.in | python3 cache.py &
cat trending_today.in | python3 cache.py &
cat me_at_the_zoo.in | python3 cache.py &
cat videos_worth_spreading.in | python3 cache.py &

wait
echo "Done!"
