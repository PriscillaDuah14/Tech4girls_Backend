#this script caclculate three numbers ; the sum of first two numbers and the product of the result with the third number

num1=$1
num2=$2
numn3=$3

sum=$(( num1 + num2 ))
product=$(( sum * num3 ))

echo "the sum of $num1 and $num2 is: $sum"

echo "multiplying the sum by $num3 gives: $product"