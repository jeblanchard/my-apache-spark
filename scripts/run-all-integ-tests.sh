printf "\n"

for f in ./test/integration/*
do
  echo $f
  $f
  printf "\n\n"
done

printf "All integration tests have passed."
