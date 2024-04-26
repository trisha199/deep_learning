#!/bin/bash
set -x
cd /Users/abhishekshah/Desktop/rag1/deep_learning
git pull
git add --all
now=$(date)
git commit -m "Auto-Commit at : $now"
git push -u origin main