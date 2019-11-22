# VPN SERVER ON DOCKER

In production this image should be run first (before connecting to tor-proxy-server).

## Testing the image

- To build the image run the following command:
    ```
    docker-compose build
    ```

- Run the image using following command:
    ```
    docker-compose-up
    ```

- Follow the instructions in ```start.sh``` to create client configuration file to connect to VPN Server using OpenVPN Client.

- Download OpenVPN Client.

- Connect to VPN Server using the generated configuration file.