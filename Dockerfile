FROM debian:stable-slim
COPY load_balancer /bin/load_balancer
ENV PORT=8991
CMD ["/bin/load_balancer"]



# first build (build the server)  to an image
# GOOS=linux GOARCH=amd64 go build -o load_balancer main.go

# second build (build the docker image)
# docker build -t load_balancer_image .

# run the docker image
# docker run -d -p 8991:8991 load_balancer

# check if the container is running
# docker ps