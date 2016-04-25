#!/bin/sh

curl -H "Content-Type: application/json" -X POST -d '{"foo":"xyz", "secret":"xyz"}' http://localhost:9090/
