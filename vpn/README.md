# VPN SERVER ON DOCKER

This is **OpenVPN** inside a docker container.
The container will also include a browser (Chrome/Chromium/Firefox) using a TOR proxy, running after the VPN connection is established.

## Testing the image

- To build the image run the following command:
    ```
    $ docker-compose build
    ```

- Run the image using following command to connect to VPN Server using the OpenVPN configuration file:
    ```
    $ docker-compose up vpn <open-vpn-config-file>
    ```

- To check if an IP Address is assigned to you by the VPN Server, run the following commands
    ```
    $ docker exec -it <container-id> bash
    root@<container-id>:/# curl https://ipinfo.io/ip
    <ip-address-assigned-by-vpn-server>
    ```