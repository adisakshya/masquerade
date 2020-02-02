# Dockerfile

FROM alpine:latest

RUN apk --no-cache add \
	tor

# expose socks port
EXPOSE 9050

# copy in our torrc file
COPY torrc.default /etc/tor/torrc.default

# make sure files are owned by tor user
RUN chown -R tor /etc/tor

USER tor

ENTRYPOINT [ "tor" ]
CMD [ "-f", "/etc/tor/torrc.default" ]