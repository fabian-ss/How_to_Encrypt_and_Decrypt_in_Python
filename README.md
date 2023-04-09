# How_to_Encrypt_and_Decrypt_in_Python

Steps to create a .pem file

Run the following command to create a private key with password

    $ openssl genrsa -des3 -out private.pem 2048

Run the following command to create a public key using a private key, it requires the password 

    $ openssl rsa -in private.pem -outform PEM -pubout -out public.pem