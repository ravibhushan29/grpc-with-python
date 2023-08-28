# gRPC

create a python virtual environment

``pip install -r requirements.txt``

```bash gen-key```

```protoc --python_out=. rides.proto```


```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. rides.proto```

```python server.py```

```python client.py```


gRPC, which stands for "gRPC Remote Procedure Call," is an open-source framework developed by Google that facilitates communication between applications or services in a distributed system. It is designed to enable efficient and robust communication between different parts of an application, even if they are running on different machines or platforms. gRPC is widely used for building high-performance and scalable microservices architectures.

Here's an overview of key concepts and features of gRPC:

1.Remote Procedure Call (RPC): RPC is a programming concept that allows a program to call a function or method on a remote server as if it were a local function call. gRPC builds on this concept, allowing developers to define service methods that can be remotely invoked by client applications.

2.Protocol Buffers (Protobuf): gRPC uses Protocol Buffers, also known as Protobuf, as its interface definition language (IDL). Protobuf is a language-agnostic binary serialization format that defines the structure of messages and services. It offers a more compact and efficient way to encode data compared to traditional text-based formats like JSON or XML.

3.Service Definitions: With Protobuf, you define your service methods and message structures in a .proto file. This file acts as a contract between the client and server, outlining the available methods, their input and output types, and any custom options.

4.Bi-directional Streaming: gRPC supports various types of communication patterns, including Unary, Server Streaming, Client Streaming, and Bidirectional Streaming. This allows you to create versatile and responsive interactions between clients and servers.

5.HTTP/2: gRPC uses HTTP/2 as its underlying communication protocol. HTTP/2 offers several benefits, such as multiplexing multiple requests over a single connection, header compression, and support for asynchronous communication.

6.Strongly Typed Contracts: The use of Protobufs ensures that the communication between client and server is strongly typed. This helps prevent data-related errors and simplifies debugging.

7.Interceptors and Middleware: gRPC provides features like interceptors and middleware that allow you to add custom logic to both client and server sides, such as logging, authentication, and error handling.

8.Language Support: gRPC supports a wide range of programming languages, including but not limited to Python, Java, C++, Go, JavaScript, C#, and Ruby. This makes it possible to build distributed systems with diverse technology stacks.

9.Security: gRPC supports transport security by default, using SSL/TLS for encrypted communication. This ensures that data exchanged between client and server remains confidential and secure.

In summary, gRPC simplifies and accelerates the development of distributed systems by providing a well-defined and efficient way for services to communicate with each other. Its use of Protobufs, support for various communication patterns, and cross-language compatibility make it a powerful tool for building modern, scalable applications and microservices

