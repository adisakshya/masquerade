<p align="center">
  <a href="https://github.com/adisakshya/masquerade">
    <img src="https://images-na.ssl-images-amazon.com/images/I/61MjBdX3-DL._SX355_.jpg" height="300" alt="Masquerade">
  </a>
</p>

[![release](https://img.shields.io/badge/release-1.0-green.svg)](https://github.com/adisakshya/masquerade/releases)
[![maintenance](https://img.shields.io/badge/maintained%3F-yes-green.svg)]()
[![dockerized](https://img.shields.io/badge/dockerized-yes-green.svg)](https://github.com/adisakshya/masquerade/blob/master/docker-compose.yml)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/adisakshya/masquerade/blob/master/LICENSE)
[![Website](https://img.shields.io/badge/website-down-red.svg)](https://adisakshya.github.io/masquerade)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/adisakshya/masquerade/pulls)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)]()

---

The TOR browser has revolutionized the way we browse in this age of privacy breaches, mass surveillance, and data monetization. It provided the much needed peace of mind to many browsing the internet 😃.
Over the years though, TOR has been exposed quite a couple of times. The browser is still as secure — but not as leak-proof as some would want it to be 🤔. TOR has a habit of storing the IP address at the entry node which can cause security issues of its own. The browser is notorious for being slow 😕.

I needed something that doesn't expose my IP address at the entry node & all the information exchange I do on the web is secure enough to provide me my peace of mind.

So, I built Masquerade 🎭!

## What is Masquerade

A configurable setup that encrypts all the information that you are sending over TOR & hides the fact from your Internet Service Provider (ISP) that you are using TOR and also doesn't exposes your IP address to TOR entry node. Combine that with the fact that you now get to use TOR in regions of the world where it is not supported.

## How Masquerade work?

A VPN will hide your IP address ever before you connect to the TOR. That means the entry node on TOR still records an IP address, but that won’t be your real location, it would be of the VPN Server.

The VPN encrypt all the Internet traffic within the VPN layer. Then, this encrypted traffic would be sent to the wide TOR network through a few TOR hops before it ends up at the final destination (the Internet).

Because you would firstly connect to VPN, this hides from your Internet Service Provider (ISP) that you are using TOR.

When you make TOR the last gateway before connecting to the Internet, you are still able to access TOR’s hidden services and websites (hidden websites with the .onion suffix) which would normally can only be accessed within the TOR network.

You'll be assigned an IP address by the VPN Server that will be seen by the TOR entry node, and the web-browser sees the IP address of the TOR exit node. This means, Google might locate you in Russia and your system IP address says you are in South Korea.

**Caution:** No one knows your real IP address except the VPN provider. Your TOR traffic can be exposed to your ISP in the event if your VPN connection unexpectedly drops.
For now you can use custom configuration files to connect your VPN Provider using OpenVPN, but later releases of this project are aimed to provide an Open-VPN-Server to all clients.

## Getting Started

Follow below steps for setup:

### Prerequisites

Docker - Set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

- For Windows/MacOS
	- Download & Install **Docker Toolbox**
		- for macOS instructions are [here](https://docs.docker.com/toolbox/toolbox_install_mac/).
		- for Windows instructions are [here](https://docs.docker.com/toolbox/toolbox_install_windows/).
- For Ubuntu
	- Install **Docker**, instructions are [here](https://www.youtube.com/watch?v=V9AKvZZCWLc).

### Operating Instructions

- Fork this repository
	- "Forking" adds a copy of [adisakshya/masquerade](https://github.com/adisakshya/masquerade) repository to your GitHub account as `https://github.com/YourGitHubUserName/masquerade`
- Download or clone your forked repository
	- You can clone the repository executing below command in a location of your choice of your system.
	```$ git clone https://github.com/YourGitHubUserName/masquerade.git```
- Connect to VPN Provider using any of your VPN Client Applications (eg. OpenVPN)
- Activate TOR Proxy by following the README instructions in ```/tor/README.md```.
- Check if the TOR proxy server is functioning good by visiting this [check.torproject](https://check.torproject.org/)
    - Look for the congratulations message and the IP assigned.
- That's it you've done configuring the setup.

#### Developer Guide

- TOR Proxy Service: ```/tor```
	- Dockerfile: ```/tor/Dockerfile``` setup TOR Proxy in docker container
- VPN Service: ```/vpn```
	- Dockerfile: ```/vpn/Dockerfile``` connect to VPN Provider using OpenVPN client in docker container

## What is in the next release ?

Issues to work on next, possibly before the next release are covered in [milestones](https://github.com/adisakshya/masquerade/milestones).

## Suggest Features

Is a feature you care about currently missing? Make sure to browse the [issue tracker](https://github.com/adisakshya/masquerade/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc) and add your ":+1:" reaction to the issues you care most about, as we also use those reactions to prioritize issues.

## Contributing

There are multiple ways to contribute to this project, read about them [here](https://github.com/adisakshya/masquerade/blob/master/.github/CONTRIBUTING.md).

## License

All versions of the app are open-sourced, read more about this [LICENSE](https://github.com/adisakshya/masquerade/blob/master/LICENSE).
