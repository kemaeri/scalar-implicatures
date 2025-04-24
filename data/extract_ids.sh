#!/bin/bash
cd "$(dirname "$0")/json"
ls |  grep 'participant_.*_scalar' | sed -n  's/.*participant_\(.*\)_scalar.*/\1/p' > ../output.txt
