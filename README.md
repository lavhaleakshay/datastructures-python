# datastructures-python


kubectl apply -f "https://raw.githubusercontent.com/GoogleCloudPlatform/marketplace-k8s-app-tools/master/crd/app-crd.yaml"

export APP_INSTANCE_NAME=mariadb-galera-1
export NAMESPACE=default

export REPLICAS=1

export MARIADB_ROOT_PASSWORD="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 12 | head -n 1 | tr -d '\n' | base64)"
export EXPORTER_DB_PASSWORD="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 12 | head -n 1 | tr -d '\n' | base64)"



openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /tmp/tls.key -out /tmp/tls.crt -subj "/CN=mariadb/O=mariadb"


export TLS_CERTIFICATE_KEY="$(cat /tmp/tls.key | base64)"
export TLS_CERTIFICATE_CRT="$(cat /tmp/tls.crt | base64)"

helm template chart/mariadb-galera mariadb --namespace "$NAMESPACE" --set "mariadb.image.repo=$IMAGE_REPO" --set "mariadb.image.tag=$TAG" --set "mariadb.volumeSize=8" --set "db.rootPassword=$MARIADB_ROOT_PASSWORD" --set "db.exporter.image=$IMAGE_MYSQL_EXPORTER" --set "db.exporter.password=$EXPORTER_DB_PASSWORD" --set "prometheusToSd.image=$IMAGE_METRICS_EXPORTER" --set "prometheusToSd.enabled=$METRICS_EXPORTER_ENABLED" --set "peerFinder.image=$IMAGE_PEER_FINDER" --set "tls.base64EncodedPrivateKey=$TLS_CERTIFICATE_KEY" --set "tls.base64EncodedCertificate=$TLS_CERTIFICATE_CRT" --set "db.replicas=$REPLICAS" > "${APP_INSTANCE_NAME}_manifest.yaml"


helm template chart/mariadb-galera mariadb --namespace "$NAMESPACE" --set "db.rootPassword=$MARIADB_ROOT_PASSWORD" --set "db.exporter.password=$EXPORTER_DB_PASSWORD" --set "db.exporter.image=$IMAGE_MYSQL_EXPORTER" --set "tls.base64EncodedPrivateKey=$TLS_CERTIFICATE_KEY" --set "tls.base64EncodedCertificate=$TLS_CERTIFICATE_CRT" --set "db.replicas=$REPLICAS" > "mariadb_manifest.yaml"
