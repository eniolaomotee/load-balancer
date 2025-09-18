FROM debian:stable-slim
COPY load_balancer /bin/load_balancer
ENV PORT=8991
CMD ["/bin/load_balancer"]
