# this scipt checks if a number is odd or even

number=$1
if [ $(( $1 % 2 )) = 0 ]
then
    echo "the number $1 is even"
else
    echo "the number $1 is odd"
    
fi
    