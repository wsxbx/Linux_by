import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(1)
print('waiting for connnecting...')
filename='C:/python_server.txt'
print('I want to get the file %s!' % filename)
(c,addr)=s.accept()
c.send(filename.encode('utf-8'))
str1=c.recv(1024)
str2=str1.decode('utf-8')
if str2=='no':
	print('The file %s is failed!' % filename)
else:
	c.send(b'I am ready!')
	temp=filename.split('/')
	myname='my_'+temp[len(temp)-1]
	size=1024
	with open(myname,'wb') as f:
		while True:
			data = c.recv(size)
			f.write(data)
			if len(data)<size:
				break
	print('The download file is %s!' % myname)
c.close()