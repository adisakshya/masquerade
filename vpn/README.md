# VPN SERVER ON DOCKER

In production this image should be run first (before connecting to tor-proxy-server).

## Testing the image

- To build the image run the following command:
    ```
    docker-compose build
    ```

- Run the image using following command to connect to VPN Server using the OpenVPN configuration file.:
    ```
    docker-compose up vpn <open-vpn-config-file>
    ```