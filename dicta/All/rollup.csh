#!/bin/csh
foreach file ( `cat manifest1` )
cat g1_$file.txt >> Gratian1.txt
end
#
foreach file ( `cat manifest2` )
cat g2_$file.txt >> Gratian2.txt
end
