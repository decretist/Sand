#!/bin/csh
foreach word ( `cat sorted.txt`)
echo "'"$word"'," >> quotified.txt
end
