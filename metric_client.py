import socket
import time
from typing import DefaultDict

class ClientError(Exception):
    pass

class Client():
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    def put(self, metric, value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
        else:
            timestamp = str(timestamp)
        with socket.create_connection((self.ip, self.port), timeout=self.timeout) as sock:
            query = f'put {metric} {value} {timestamp}\n'
            sock.send(query.encode())
            response = sock.recv(1024).decode()

            if response != 'ok\n\n':
                raise ClientError

    def get(self, query):
        with socket.create_connection((self.ip, self.port), timeout=self.timeout) as sock:
            query = f'get {query}\n'
            sock.send(query.encode())
            data = sock.recv(1024).decode()

        if data == 'ok\n\n':
            return {}
        try:
            if data.split('\n')[0] == 'ok':
                metrics = [i.split(' ') for i in data.split('\n')[1:-2]]
                metrics = sorted(metrics, key=lambda x: int(x[2]))
                result = DefaultDict(list)
                for key, value, ts in metrics:
                    result[key].append((int(ts), float(value)))
                return dict(result)
            else:
                raise ClientError
        except:
            raise ClientError

if __name__=='__main__':
    client = Client("127.0.0.1", 8888, timeout=15)
    print(client.get("palm.cpu"))