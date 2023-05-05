printf "\n"

docker stop my-apache-spark

docker rm my-apache-spark

docker build -t jeblanchard/personal-website:my-apache-spark .

docker run --name my-apache-spark -it jeblanchard/personal-website:my-apache-spark sh

for f in ./test/integration/*
do
  echo $f
  $f
  printf "\n\n"
done

printf "All integration tests have passed."
