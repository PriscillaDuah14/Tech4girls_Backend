#this script check for ages

#read

echo " what is your age?;"
read age

if [ "$age" -lt 18 ]
then
    echo " you are a minor"
elif [ "$age" -ge 18 ] && [ "$age" -le 64 ]
 then
     echo " you are an adult"
else 
      echo "you are senior"
fi 