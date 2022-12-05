# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:52:09 2022

@author: Abinash.m
"""
from flask import Flask

import sys, time
import base64
app = Flask(__name__)
def printError(msg=''):
    if msg != "":
        print("Error: " + msg)
    print('Usage: ')
    print(sys.argv[0] + " [private key file] [consumer ID] [Key version]")
    print('')
    print('Example: ')
    print(sys.argv[0] + " private_key.pem 44444444-23f9-3333-2222-111111111111 1")
    print('')
    print('')
    sys.exit()
def sign_data(private_key, data):
    from Crypto.PublicKey import RSA 
    from Crypto.Signature import PKCS1_v1_5 
    from Crypto.Hash import SHA256 
    from base64 import b64encode, b64decode 
    key = open(private_key, "r") 
    rsakey = RSA.importKey(key.read()) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new()
    digest.update(data.encode('utf-8')) 
    sign = signer.sign(digest) 
    return b64encode(sign)
def main(argv):
    global logData
    global hostname
    try:

        
        privateKey ='untitled1.txt'


    except:
        printError()
    epoch_time = int(time.time()) * 1000
    data = 'd23d5ad5-b016-4a76-b6bb-c6bae0372374' + '\n' + str(epoch_time) + '\n' + '1' + '\n'
    #print('Timestamp:', epoch_time)
    print('Signature:' , sign_data(privateKey, data).decode())
    sig = sign_data(privateKey, data).decode()
    #m = print('Timestamp:', epoch_time)
    return sig,epoch_time
@app.route('/')
def result():
    #m = main(sys.argv)
    #return main(sys.argv)
    return {
            "Authorization": main(sys.argv)[0],
            "epoch_time":main(sys.argv)[1]
            }
if __name__ == '__main__':
    app.run(port=5000, debug=True)
