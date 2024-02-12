import socket

class IPSearch:
    list = []

    def create_list():
        ins = IPSearch("cse.du.ac.bd.", "ns1.cse.du.ac.bd.", "NS", "86400")
        IPSearch.list.append(ins)
        ins3 = IPSearch("ns2.cse.du.ac.bd.", "192.0.2.2", "A", "86400")
        IPSearch.list.append(ins3)
        ins4 = IPSearch("ns1.cse.du.ac.bd.", "2001:db8::1", "AAAA", "86400")
        IPSearch.list.append(ins4)
        ins5 = IPSearch("ns2.cse.du.ac.bd.", "2001:db8::2", "AAAA", "86400")
        IPSearch.list.append(ins5)
        ins6 = IPSearch("cse.du.ac.bd.", "192.0.2.3", "A", "86400")
        IPSearch.list.append(ins6)
        ins7 = IPSearch("cse1.du.ac.bd.", "2001:db8::3", "AAAA", "86400")
        IPSearch.list.append(ins7)
        ins8 = IPSearch("www.cse.du.ac.bd.", "cse.du.ac.bd.", "CNAME", "86400")
        IPSearch.list.append(ins8)
        ins9 = IPSearch("cse2.du.ac.bd.", "10 mail.cse.du.ac.bd.", "MX", "86400")
        IPSearch.list.append(ins9)
        ins10 = IPSearch("mail.cse.du.ac.bd.", "192.0.2.4", "A", "86400")
        IPSearch.list.append(ins10)
        

    def __init__(self, Name, Value, Type, TTL):
        self.Name = Name
        self.Value = Value
        self.Type = Type
        self.TTL = TTL

class Server:
    def search(s):
        ret = 0
        rs = "nf"
        for item in IPSearch.list:
            if item.Name == s:
                rs = item.Type
                break

        if rs.strip() == "NS":
            return 1
        elif rs.strip() == "MX":
            return 5
        elif rs.strip() == "nf":
            return 0
        elif rs.strip() == "CNAME":
            return 2
        elif rs.strip() == "AAAA":
            return 3
        elif rs.strip() == "A":
            return 4
        return ret
    

    # def search1(s):
    #     ret = 0
    #     rs = "nf"
    #     for item in IPSearch.list:
    #         if item.Name == s:
    #             rs = item.Type
    #             break

    #     if rs.strip() == "NS":
    #         return 1
    #     elif rs.strip() == "MX":
    #         return 5
    #     elif rs.strip() == "nf":
    #         return 0
    #     elif rs.strip() == "CNAME":
    #         return 2
    #     elif rs.strip() == "AAAA":
    #         return 3
    #     elif rs.strip() == "A":
    #         return 4
    #     return ret

    def main():
        IPSearch.create_list()
        response = "Welcome to CSE 3111!"
        port = 1500
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((socket.gethostname(), port))
        print("Domain server Started")
        buffer_size = 1024

        while True:
            buffer, client_address = server_socket.recvfrom(buffer_size)
            message = buffer.decode().strip()
            print("Client message:", message)
            flag = Server.search(message)
            print(flag)

            if flag == 0:
                response = "Not Found"
            elif flag == 1:
                response = "NS type domain found"
            elif flag == 2:
                response = "Cname type domain found"
            elif flag == 3:
                response = "AAAA type domain found"
            elif flag == 4:
                response = "A type domain found"
                # response = IPSearch.list[IPSearch.index].Value
            elif flag == 5:
                response = "MX type domain found"

            server_socket.sendto(response.encode(), client_address)

        server_socket.close()

if __name__ == "__main__":
    Server.main()
