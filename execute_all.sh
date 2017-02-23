#!/bin/bash

zip submission.zip *.py &
cat kittens.in | python3 cache.py > outputs/kittens.out &
cat trending_today.in | python3 cache.py > outputs/trending_today.out &
cat me_at_the_zoo.in | python3 cache.py > outputs/me_at_the_zoo.out &
cat videos_worth_spreading.in | python3 cache.py > outputs/videos_worth_spreading.out &

wait
echo "Done!"
