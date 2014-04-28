#!/bin/csh
foreach word ( `cat unsorted.txt`)
echo "'"$word"'," >> quotified.txt
end
