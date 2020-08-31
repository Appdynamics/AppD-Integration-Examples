#!/bin/bash
#
#
HOST=127.0.0.1
PORT=9797
TS=$(date +%s)
RN=$(( $RANDOM % 10 ))

# Test GET
curl -G $HOST:$PORT --data-urlencode "ts=$TS" --data-urlencode "rn=$RN"

# Test POST
curl -X POST $HOST:$PORT --data-urlencode "ts=$TS" --data-urlencode "rn=$RN"
