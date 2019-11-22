# TOR PROXY SERVER ON DOCKER

In production this image should be run after establishing connection with the VPN server.

## Testing the image

- To build the image run the following command:
    ```
    docker build -t tor
    ```

- Run the image using following command:
    ```
    docker run -d --rm tor -p 9150:9150 tor
    ```

- Open Google Chrome or any browser you are using and download [SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=en) or any other tool to manage proxy for your browser.

- Create a new proxy server with:
    - Protocol: SOCKS5
    - Server Address: 192.168.99.100
    - Port: 9150

- Check if the tor proxy server is functioning good by visiting this [check.torproject](https://check.torproject.org/)
    - Look for the congratulations message and the IP assigned.