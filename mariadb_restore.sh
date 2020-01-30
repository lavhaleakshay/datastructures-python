#!/bin/bash⏎
⏎
BKP_FILE=all-databases-2020-01-30_16-26.sql.gz⏎
POD_NAME=mariadb-0⏎
BKP_DIR=var/mariadb/backup⏎
BKP_PATH=${BKP_DIR}/${BKP_FILE}⏎
⏎
# restore all databases from provided backup⏎
kubectl -n default exec -it ${POD_NAME} -c mariadb -- sh -c "mkdir -p ${BKP_DIR}"⏎
kubectl cp ${BKP_FILE} default/${POD_NAME}:${BKP_PATH}⏎                                                                                                                                                            
kubectl -n default exec -it ${POD_NAME} -c mariadb -- bash -c "gunzip < ${BKP_PATH} |⏎
    mysql -uroot -pD0QdPPYtWZZi"⏎
⏎
# cleanup⏎
kubectl -n default exec -it ${POD_NAME} -c mariadb -- sh -c "rm -f ${BKP_PATH}"⏎
