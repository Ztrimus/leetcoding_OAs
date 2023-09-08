import sys
class LogServer:
    def __init__(self, max_logs):
        # Constructor
        self.max_logs = max_logs
        self.log_list = []
        self.latest_timestamp = 0

    def recordLog(self, logId, timestamp):
        self.log_list.append([logId, timestamp])
        self.latest_timestamp = timestamp

    def getLogs(self):
        print_log = []
        allowed_m = self.max_logs
        for i in range(len(self.log_list)-1, -1, -1):
            if self.log_list[i][1] > self.latest_timestamp-3600 and allowed_m > 0:
                print_log.insert(0,self.log_list[i][0])
                allowed_m -=1
        
        result = ''
        for i, j in enumerate(print_log):
            result+=str(j)
            if i != len(print_log)-1:
                result += ","
                
        return result
                
            

    def getLogCount(self):
        count = 0
        for i in range(len(self.log_list)-1, -1, -1):
            if self.log_list[i][1] > self.latest_timestamp-3600:
                count += 1
        return count
                

# This and below go in the tail section of hacker rank
def handleQuery(log_server, query):
    query_type = query[0]
    if query_type == "RECORD":
        log_server.recordLog(int(query[1]), int(query[2]))
    elif query_type == "GET_LOGS":
        print(log_server.getLogs())
    elif query_type == "COUNT":
        print(log_server.getLogCount())

def main():
    max_logs = int(input())
    log_server = LogServer(max_logs)
    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()
        handleQuery(log_server, query)

if __name__ == "__main__":
    main()