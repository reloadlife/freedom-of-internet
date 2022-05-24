# freedom-of-internet

:)

## OpenVPN

it's mostly [https://github.com/kylemanna/docker-openvpn](https://github.com/kylemanna/docker-openvpn) :)

### how to use ?

- openvpn

```bash
docker-compose build
```

to build the container

```bash
bash ovpn_init.sh -u udp://server_public_ip
```

then to generate and export clients:

```bash
export CLIENT_NAME="client-1"
bash ovpn_client.sh $CLIENT_NAME
# bash ovpn_client.sh $CLIENT_NAME nopass
bash ovpn_export.sh $CLIENT_NAME
```

you will have a `$CLIENT_NAME.ovpn` file in the current directory


## Shadowsocks

it's basically V2ShadowRay from [https://github.com/Unleash-the-internet/V2ShadowRay](https://github.com/Unleash-the-internet/V2ShadowRay)

edit `config.json` to change server's password
don't change ip or ports, those will be handled via Docker


## DOH / PiHole

pihole and  DNS Over HTTPS

## MTProto

Telegram's MTProto Proxy from [https://github.com/alexbers/mtprotoproxy](https://github.com/alexbers/mtprotoproxy), but edited a little to match what we want.


## how to run it all ?

copy `.env.example` to `.env`

```bash
cp .env.example .env
```

edit .env file as you wish

```
hostname='localhost'
BOOTP_PORT=67
DNS_PORT=53
DHCP_PORT=68
OPENVPN_PORT=1194
SHADOWSOCKS_PORT=1080
OPENVPN_SERVER_URL=udp://0.0.0.0
SERVER_IP=0.0.0.0
PI_HOLE_PASSWORD=THIS_IS_A_SECURE_PASSWORD
PI_HOLE_HTTP_PORT=180
DOH_SERVER_HTTPS_PORT=443
TELEGRAM_PROXY_PORT=1285
```

then use docker to run it all

```bash
docker-compose up -d
```

or if you want to build images locally and not use pre-built images

```bash
docker-compose up -f docker-compose.build.yml -d
```
