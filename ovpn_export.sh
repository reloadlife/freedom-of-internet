#!/bin/bash

CLIENTNAME=$1
docker-compose exec openvpn get_client $CLIENTNAME > $CLIENTNAME.ovpn