# ---
# Setup OpenVPN Server
# Create configuration file to connect to this server using OpenVPN Client
# ---


# Get docker machine ip

# Initialize configuration files
# docker-compose run --rm vpn ovpn_genconfig -u udp://$DOCKER_MACHINE_IP:$PORT

# Initialize certificates
# docker-compose run --rm vpn ovpn_initpki

# Fix ownership
# chown -R $(whoami): ./vpn-data

# Start OpenVPN Server
# docker-compose up -d vpn

# Generate Client Certificates
# export CLIENTNAME="your_client_name"

# # without a passphrase (not recommended)
# docker-compose run --rm vpn easyrsa build-client-full $CLIENTNAME nopass

# Create OpenVPN Configuration files
# docker-compose run --rm vpn ovpn_getclient $CLIENTNAME > $CLIENTNAME.ovpn

# Debugging
# docker-compose run -e DEBUG=1 vpn