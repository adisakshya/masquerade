# FIREFOX DOCKER

This is **Firefox** inside a docker container.
The container includes a web browser (Firefox) using a TOR proxy, running after the VPN connection is established.

## Testing the image

- Run the image using following command to start the firefox service:
    ```
    $ docker-compose up
    ```
    
    or, for running in deatched mode

    ```
    $ docker-compose up -d
    ```

- Browse to http://your-host-ip:5800 to access the Firefox GUI.

### Credits

This service is credited to [jlesage](https://hub.docker.com/r/jlesage/firefox).