docker stop my-apache-spark

docker rm my-apache-spark

docker build -t jeblanchard/personal-website:my-apache-spark .

docker run --name my-apache-spark -it jeblanchard/personal-website:my-apache-spark sh
