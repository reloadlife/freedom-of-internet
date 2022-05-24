#!/bin/bash

docker-compose run --rm openvpn easyrsa build-client-full $@
