#!/bin/bash

docker-compose run --rm openvpn config_gen $@
docker-compose run --rm openvpn pki nopass