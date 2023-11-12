import csv

def create():
    """
    Create file with adresses
    
    """
    route = "./files/addresses.csv"

    addresses= [
        { "address" :"Cl. 27 d sur # 27 c 51", "latitude" : [0], "longitude": [0] }, 
        { "address" :"Diag 40 # 41 61","latitude" : [0], "longitude": [0] }, 
        { "address" :"carrera 23 num 35 48", "latitude" : [0], "longitude": [0] }, 
        { "address" :"calle 35 num 33 09", "latitude" : [0], "longitude": [0] },
        { "address" :"calle 52 # 52-43" , "latitude" : [0], "longitude": [0]},
        { "address" :"Cr. 53 # 70 86","latitude" : [0], "longitude": [0]}
        ]

    with open(route,"w",encoding= "UTF-8", newline="") as ad:
        writer = csv.DictWriter(ad, fieldnames=["address","latitude","longitude" ])
        writer.writeheader()
        writer.writerows(addresses)
        

def  run():
    create()


if __name__=="__main__":
    run()