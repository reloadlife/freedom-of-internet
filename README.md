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
