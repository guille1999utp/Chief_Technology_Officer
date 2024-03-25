#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until mysqladmin ping -h "$host" --silent; do
  >&2 echo "MySQL no esta disponible - esperando"
  sleep 1
done

>&2 echo "MySQL esta montado - Ejecutando comando de inicio de aplicacion"
exec $cmd
