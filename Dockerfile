FROM debian:stable-slim
COPY goserver /bin/goserver
ENV PORT=8991
CMD ["/bin/goserver"]



# GOOS=linux GOARCH=amd64 go build -o load-balancer main.go