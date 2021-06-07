```
#!/bin/bash
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
echo "Hello World $(hostname)" > /var/www/html/index.html
```

The COPY instruction copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
// Same as 'ADD' but without the tar and remote url handling.
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

 while ADD has some features (like local-only tar extraction and remote URL support)

The ADD instruction copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.
ADD https://example.com/big.tar.xz /usr/src/things/
RUN tar -xJf /usr/src/things/big.tar.xz -C /usr/src/things
RUN make -C /usr/src/things all