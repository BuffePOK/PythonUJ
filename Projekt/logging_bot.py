from time import ctime

def logging_bot(log_message):
    f1 = open('logging.log','a')
    f1.write("[" + str(ctime()) + "]. Message: " + log_message + "\n")
    f1.close()

if __name__ == "__main__":
    f1 = open('logging.log', 'r')
    for i in f1:
        print(i)