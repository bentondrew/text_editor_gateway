# text_editor_gateway
Reverse proxy for external access to text editor service APIs.

## Docker Image Build Instructions
From directory containing the Dockerfile
```Bash
docker build -t text_editor_gateway:0.1.0 .
```

## Docker Run Instructions
```Bash
docker run --rm -p 80:80 text_editor_gateway:0.1.0
