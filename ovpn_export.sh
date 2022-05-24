#!/bin/bash

CLIENTNAME=$1
docker-compose run --rm openvpn get_client $CLIENTNAME > $CLIENTNAME.ovpn