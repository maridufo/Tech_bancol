import csv

def create():
    """
    Create file with adresses
    
    """
    route = "./files/addresses.csv"

    addresses= [
        { "address" :"calle 53 # 55 a 67", "latitude" : [0], "longitude": [0] }, 
        { "address" :"calle 44 # 89 b 44","latitude" : [0], "longitude": [0] }, 
        { "address" :"carrera 50 # 38 a 39", "latitude" : [0], "longitude": [0] }, 
        { "address" :"carrera 102 bb num 49 a 30", "latitude" : [0], "longitude": [0] },
        { "address" :"carrera 99 a # 48 b 29" , "latitude" : [0], "longitude": [0]},
        { "address" :"1600 Amphitheatre Parkway","latitude" : [0], "longitude": [0]}
        ]

    with open(route,"w",encoding= "UTF-8", newline="") as ad:
        writer = csv.DictWriter(ad, fieldnames=["address","latitude","longitude" ])
        writer.writeheader()
        writer.writerows(addresses)
        

def  run():
    create()


if __name__=="__main__":
    run()