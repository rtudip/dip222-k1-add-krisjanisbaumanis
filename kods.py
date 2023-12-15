from gettext import find


sar1=[]
rinda = []
with open("pd_atbildes/treninsh/data.txt", "r") as f:
    next(f)
    for line in f:
        row = line.rstrip().rsplit(",")
        rinda.append(row)
sar = []
sar1=[]
for row in rinda:
    sertific = row[3].rsplit(".")
    country = row[4]
    ieks = []
    if(row[4] == "Latvia"):
        sar.append(sertific)   # PAREIZA ATBLIDE ORG IR 20
print(sar)
#         if(reversed(sertific[0:3]) == "org"):
#             sar.append(sertific)
# print(sertific)

            
            
        
                   

# sar = []
# for row in rinda:
#     if(row[4]== "Oman"):
#         sar1.append(row[6])     sakartots saraksts kura gada ir dibinata vecaka kompanija omana
# print(sorted(sar1))

# sar = []
# sar1=[]
# for row in rinda:
#     ieks = []
#     if(row[4] == "Latvia"):
#         sar.append(int(row[8]))      cik cilv strada lv
# print(sum(sar))


# sar=[]
# for row in rinda:
#     ieks = []
#     if(row[4] == "Latvia"):
#         if(row[7]=="Telecommunications"):   cik cilv strada telecomunication latvija
#           sar.append(int(row[8]))
# print(sum(sar))
    



#     sertific = row[3]
# print(sertific)
# sar = []
# sar1=[]
# for row in rinda:
#     ieks = []
#     if(row[4] == "Latvia"):
#         if(sertific[0:5] == "https"):  ssl sertifikats Latvijas kompanijam 
#             sar.append(row[2])
# print(len(sar))
        

    

    