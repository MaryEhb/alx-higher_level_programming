#!/bin/bash
#9. Catch me if you can!
curl -s 0.0.0.0:5000/catch_me -o /dev/null -w "You got me!"
