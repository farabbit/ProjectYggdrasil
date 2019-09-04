import threading
import queue
import time

class message: # =action+source+args
    def __init__(self,**kwargs):
        if "sentence" in kwargs:
            self.action,self.source,*self.args=kwargs['sentence'].split(' ') # *args will receive all other parameters
        elif "message" in kwargs:
            self.action,self.source,self.args=kwargs["message"]


class Yggdrasil:
    # message QUEUE
    # message Consumer
    # SOCKET listener
    # SOCKET communicator
    # HTTP listener
    # HTTP communicator
    def __init__(self):
        self.messageQueue = queue.Queue()
        self.Consumer = self.messageConsumer(self.messageQueue)
        self.prod = self.testProducer(self.messageQueue)

    def start(self):
        self.Consumer.start()
        self.prod.start()

        self.Consumer.join()
        self.prod.join()
        print("Exiting")

    # base Thread 
    # external thread will interit this and regist to thread collection
    class YggThread(threading.Thread):
        def __init__(self):
            super().__init__()
        # Attribute initializing
        # Thread registory
        # Thread moniter & control
        pass

    # consume
    class messageConsumer(YggThread): # TODO: use singleton?
        # will need messageQueue for all messageQueue users
        def __init__(self,messageQueue):
            super().__init__()

            self.messageQueue=messageQueue
        # override
        def run(self):
            count=0
            while 1:
                self.consume()
                count+=1
                if count==10:
                    break
            print("exiting consumer")
        # core
        def consume(self):
            message = self.messageQueue.get()

            if(message.action=='PRINT'):
                print(message.args[0], message.args[1])

    # listen all kinds of connection requsts and create communicator&producer
    class Listener(YggThread):
        pass

    # produce message to queue, point to point communicate with client
    class Producer(YggThread):
        def __init__(self,messageQueue):
            super().__init__()

            self.messageQueue=messageQueue
        def produce(self, message):
            self.messageQueue.put(message)
    
    class testProducer(Producer):
        def run(self):
            index=0
            while 1:
                self.produce(message(sentence=("PRINT NONE HelloWorld! "+str(index))))
                index=index+1

                time.sleep(1)
                if(index==10):
                    break
            print("Exiting producer")

    class SOCKETListener(Listener):
        pass

    class SOCKETCommunicator(Producer):
        pass

    class HTTPListener(Listener):
        pass

    class HTTPCommunicator(Producer):
        pass


class consumerService01:
    def __init__(self):
        pass


if __name__=='__main__':
    Yggdrasil = Yggdrasil()
    Yggdrasil.start()
