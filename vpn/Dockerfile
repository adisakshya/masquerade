FROM alpine:latest
RUN apk --no-cache add \
	openvpn

RUN apk add --no-cache --upgrade bash
RUN apk add --no-cache --upgrade curl

RUN mkdir /usr/share/openvpn
RUN cp /etc/openvpn/* /usr/share/openvpn/

WORKDIR /etc/openvpn
ENTRYPOINT ["openvpn"]