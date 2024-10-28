#this script users local operators to check the conditions and print the appopriate messages bases on the input numbers

number1=$1
number2=$2

if [ $number1 -gt 10 ] && [ $number2 -gt 10 ]
then 
    echo "both numbers are greater than 10"
if [ $number1 -gt 10 ] || [ $number2 -gt 10 ]
then
    echo "at least one number is greater than 10"
else 
     echo "neither is greater than 10"
fi 