'''
This script connects to a specific server on a specific port and records its response in a file written to our host system.
'''
import socket

server = input("Enter server domain: ")
port = int(input("Enter networking port number: "))
output_file = 'socket_response.txt'

def connect_to_server(server, port, output_file):
  # create socket object
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    # connect to server
    client_socket.connect((server, port))
    print(f"Connected to {server} on port {port}")
    # open output file in write mode
    with open(output_file, 'wb') as file:
      while True:
        # receive data from server
        data = client_socket.recv(1024)
        # break the loop if no more data is received
        if not data:
          break
        # write the received data to the file
        file.write(data)
        # print recevied data to the console
        print(data.decode('utf-8'))
    print(f"Data successfully recorded in {output_file}")

  except Exception as e:
    print(f"An error occurred: {e}")

  finally:
    client_socket.close()

connect_to_server(server, port, output_file)
