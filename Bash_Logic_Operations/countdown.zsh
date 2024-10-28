#this script counts down an input number to 1 and then print countdown complete

number=$1

while [ $1 -le 10 ]
do
    echo "$1"
    number=$(( number+1 ))
done
     echo "countdown complete!"