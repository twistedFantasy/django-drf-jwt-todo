# Docker

**_*install docker & docker-compose if you are not going to use VirtualBox & Vagrant_**

### Docker installation:
* [CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
* [Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
* [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Binaries](https://docs.docker.com/install/linux/docker-ce/binaries/)

#### Useful resources:
[github](https://github.com/docker/docker-ce/releases) 

### Docker-Compose installation:
```
curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

### Useful resources:
[github](https://github.com/docker/compose/releases)

### Development
To start project from docker-compose
```
$ docker-compose -f docker-compose-local.yml up -d 
```
