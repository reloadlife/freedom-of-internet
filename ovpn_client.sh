#!/bin/bash

docker-compose exec openvpn easyrsa build-client-full $@
