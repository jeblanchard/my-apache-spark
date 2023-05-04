printf "\n"

for f in ./test/unit/*
do
  echo $f
  py $f
  printf "\n\n"
done

printf "All unit tests have passed."
