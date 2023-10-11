!#/bin/bash

for i in $(ls *.py);
do
    echo $i
    echo "---"
    cat $i
    echo "---"

    echo " "
    echo " "
    echo " "
done
