## HTTPS redirect from example.com to www.example.com

In my service container docker-compose.yml:

```yaml
version: '3.5'
# ...
services:
  nginx-proxy:
    container_name: nginx-proxy
    image: jwilder/nginx-proxy
    # ...
  servicename:
    container_name: servicename
    image: bryand1/servicename
    environment:
        VIRTUAL_HOST: www.example.com
        LETSENCRYPT_HOST: example.com,www.example.com
# ...
```

Note, I intentionally removed example.com from `VIRTUAL_HOST` because I don't want to generate the server example.com block from the template. We still need the example.com TLS certificate though in the `LETSENCRYPT_HOST`.

Put an extra.conf in /etc/nginx/conf.d on the nginx container so it can redirect:

```
server {
    listen 80;
    server_name example.com;
    return 308 https://www.example.com$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;
    ssl_certificate /etc/nginx/certs/example.com.crt;
    ssl_certificate_key /etc/nginx/certs/example.com.key;
    ssl_dhparam /etc/nginx/certs/example.com.dhparam.pem;
    return 308 https://www.example.com$request_uri;
}
```

Map this extra.conf to the nginx-proxy container in the docker-compose.yml:

```yaml
# ...
    volumes:
      - ./nginx/docker/extra.conf:/etc/nginx/conf.d/extra.conf
# ...
```

It is working, however, this is still a workaround as I have domain hardcoding in the extra.conf.

With this workaround, all the 3 requests below end up on https://www.example.com:

+ http://www.example.com
+ http://example.com
+ https://example.com
