from tech_test import b_uploadaws
from tech_test import c_readcsvaws
from tech_test import d_homoadd
from tech_test import e_comparate
from tech_test import f_apimaps
from tech_test import g_locate

def main():
    b_uploadaws.upload_to_s3("addresses.csv")
    c_readcsvaws.download_s3()
    c_readcsvaws.read_adrcsv("addresses.csv")
    d_homoadd.homo_address("addresses.csv")
    e_comparate.results_hom("addreses_h", "addresses.csv")
    f_apimaps.generate_coordinates("results_homo.csv")
    g_locate.generate_map("location.csv")

if __name__=="__main__":
   main()