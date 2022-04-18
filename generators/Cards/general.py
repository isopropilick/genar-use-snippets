import random
def ran(num):
	res=""
	for n in range(num):
		res=res+str(random.randint(1, 9))
	return str(res)
def checksum(string):
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10
def verify(string):
    return (checksum(string) == 0)
def generate(string):
    cksum = checksum(string + '0')
    return (10 - cksum) % 10
def append(string):
    return string + str(generate(string))
file = open("tarjetas.txt","w") 
BINvismaster = [520694,547075,554629,542010,522174,506270,405306,467473,455503,455510,491280,421316]
BINamex = [370376]
Mes = ["01","02","03","04","05","06","07","08","09","10","11","12"]
for val in BINvismaster:
    for no in range(100):
            account = (str(val) + ran(8) )
            luhn =append(account)
            no += 1
            file.write(str(no) + "," + luhn + ",")
            file.write(random.choice(Mes) + "/")
            file.write(str(random.randint(2020, 2032)) + ",")
            file.write(str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + "\n")
for vale in BINamex:
    for no in range(100):
            accounte = (str(vale) + ran(9))
            luhne =append(accounte)
            no += 1
            file.write(str(no) + "," + luhne + "\n")
file.close()
