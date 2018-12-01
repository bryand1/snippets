#!/bin/bash

for i in `seq 1 5`;
do
  date -d "2018-12-01 $i days" +%Y-%m-%d;
done;
