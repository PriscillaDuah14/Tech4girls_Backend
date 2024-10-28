# this script takes a number and sum it to n

echo "please enter a number n;"
read n

sum=0
for (( i=1; i<=n; i++ ))
do
   sum=$(( sum + i ))
   echo "the sum of numbers from 1 to $n is: $sum"
done