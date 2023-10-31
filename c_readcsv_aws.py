import boto3 
import csv

def download_s3():
     """
     Crear un cliente para acceder al servicio de s3.
     Especificar la Url del archivo en s3 y descargar el archivo  de s3.
     """
     try:
         s3 = boto3.client(
          service_name = "s3",
          region_name = "sa-east-1"
          )
     
         adr_url ='s3://techtestsbancol/addresses.csv'
         s3.download_file ("techtestsbancol", "addresses.csv","addresses.csv" )

     except Exception as e:
         print(f"Error en la descarga desde s3: {str(e)}")
          

def read_adrcsv():
     try:
         addresses_list = []
         with open("addresses.csv", 'r', encoding='UTF-8') as adrfile:
             addrreader = csv.reader(adrfile)
             for line in addrreader:
                 addresses_list.append(line)
         return addresses_list
 
     except Exception as e:
         print(f"Error en la descarga desde s3: {str(e)}")



def run():
     download_s3()
     addresses_list = read_adrcsv()
     for line in addresses_list:
         print(line)
                
    

if __name__ =="__main__":
    run() 