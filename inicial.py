

name=['NES-EIQ-VST-001','NES-EIQ-CCI-001','NES-EIQ-CCI-002','NES-EIQ-VST-002','NES-EIQ-COM-001','NES-EIQ-COM-002','NES-EIQ-CBJ-001','NIP-EIQ-COM-001']
switch=['10.10.1.128/24','10.10.1.130/24','10.10.1.131/24','10.10.1.129/24','10.10.1.132/24','10.10.1.133/24','10.10.1.134/24','10.10.1.22/24']
nombresvlans=["CIRCUITO-CERRADO-TV","TELEFONIA-INTERFONIA","MEGAFONIA","CONTROLESTACION","RADIO-TETRA","CONTRA-INCENDIOS","SISTEMA-INTRUSION","SISTEMA-VENTILACION","ELECTRIFICACION","INFORMACION-VIAJERO"]
vlans=[
    [nombresvlans[0],2410,'10.24.10.254'],
    [nombresvlans[1],2411,'10.24.11.254'],
    [nombresvlans[2], 2412, '10.24.12.254'],
    [nombresvlans[3], 2413, '10.24.13.254'],
    [nombresvlans[4], 1051, '10.51.1.254'],
    [nombresvlans[5], 2414, '10.24.14.254'],
    [nombresvlans[6], 2415, '10.24.15.254'],
    [nombresvlans[7], 1052, '10.52.1.254'],
    [nombresvlans[8], 2416, '10.24.16.254'],
    [nombresvlans[9], 2417, '10.24.17.254']
]

#     "CCTV",
#     "CONTROL",
#     "TELEFONO",
#     "MEGAFON",
#     "RADIOT",
#     "INCENDIO",
#     "INTRUSION",
#     "VENTILA",
#     "ELECTRIFI",
#     "INFVIAJE",
# "GESTION"

puertos=[


    ["CCTV","CCTV","CCTV","CCTV",0,0,0,0,"CONTROL","CONTROL","CONTROL","CONTROL","TELEFONO","TELEFONO","TELEFONO","TELEFONO","TELEFONO","TELEFONO",0,0,0,0,"INFVIAJE","INFVIAJE",0,"GESTION","GESTION","GESTION"],
    ["CCTV","CCTV","CCTV","CCTV","CCTV","CCTV","CCTV","CCTV","INTRUSION","INTRUSION","INTRUSION","INTRUSION","TELEFONO","TELEFONO","TELEFONO","TELEFONO","TELEFONO","TELEFONO","TELEFONO","TELEFONO","INTRUSION","INTRUSION","INFVIAJE",0,"GESTI1ON","GESTION","GESTION",0],
    ["CCTV","CCTV","TELEFONO","TELEFONO","MEGAFON","MEGAFON","RADIOT","RADIOT","INCENDIO","INCENDIO","VENTILA","VENTILA","ELECTRIFI","ELECTRIFI","INFVIAJE","INFVIAJE","INTRUSION","INTRUSION","CONTROL","CONTROL",0,0,0,0,0,"GESTION",0,0]



    ]

def saltodelinea(cadena):
    file.write(cadena+"\n")

def vlanypuerto(texto):
    if texto=="CCTV":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[0][1]))
        saltodelinea("description vlan " + vlans[0][0])
        saltodelinea("exit ")
    if texto=="TELEFONO":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[1][1]))
        saltodelinea("description vlan " + vlans[1][0])
        saltodelinea("exit ")
    if texto=="MEGAFON":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[2][1]))
        saltodelinea("description vlan " + vlans[2][0])
        saltodelinea("exit ")


    if texto=="CONTROL":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[3][1]))
        saltodelinea("description vlan " + vlans[3][0])
        saltodelinea("exit ")

    if texto=="RADIOT":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[4][1]))
        saltodelinea("description vlan " + vlans[4][0])
        saltodelinea("exit ")
    if texto=="INCENDIO":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[5][1]))
        saltodelinea("description vlan " + vlans[5][0])
        saltodelinea("exit ")
    if texto=="INTRUSION":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[6][1]))
        saltodelinea("description vlan " + vlans[6][0])
        saltodelinea("exit ")
    if texto=="VENTILA":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[7][1]))
        saltodelinea("description vlan " + vlans[7][0])
        saltodelinea("exit ")
    if texto=="ELECTRIFI":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[8][1]))
        saltodelinea("description vlan " + vlans[8][0])
        saltodelinea("exit ")

    if texto=="INFVIAJE":
        saltodelinea("switchport mode access")
        saltodelinea("switchport access vlan "+str(vlans[9][1]))
        saltodelinea("description vlan " + vlans[9][0])
        saltodelinea("exit ")
    if texto=="GESTION":
        saltodelinea("switchport mode trunk")
        saltodelinea("description Puerto-Gestion")
        saltodelinea("switchport nonegotiate")
        saltodelinea("exit ")
    if texto=="0":
        saltodelinea("sh")
        saltodelinea("description Puerto-no-asignado")
        saltodelinea("exit ")

contaux=1
for i in range(len(name)):
    xx=i
    file = open('switches/'+str(contaux)+" " +name[i], 'w+')

    file.write("enable"+"\n")
    file.write("config t"+"\n")
    file.write("hostname "+name[i]+"\n")
    contaux=contaux+1
    file.write("line console 0 "+"\n")
    file.write("password ACLMQCCUSUIO"+"\n")
    file.write("login"+"\n")
    file.write("line vty 0 15"+"\n")
    file.write("password ACLMQCCUSUIO"+"\n")
    file.write("login"+"\n")
    file.write("exit"+"\n")
    file.write("int vlan 1"+"\n")
    datos=switch[i]
    datos=datos.split("/")
    if datos[1]=="24":
        file.write("ip add "+datos[0]+" "+"255.255.255.0"+"\n")
        file.write("no shut"+"\n")
    saltodelinea("exit")
    saltodelinea("vtp mode transparent")
    for i in range(len(nombresvlans)):
        saltodelinea("vlan "+str(vlans[i][1]))
        saltodelinea("\t name "+vlans[i][0])
        saltodelinea("exit")
        saltodelinea("int vlan "+str(vlans[i][1]))
        saltodelinea("\t ip add "+str(vlans[i][2])+" 255.255.255.0")
        saltodelinea("exit")
    if xx<=2:
        print "gasf"
        contador=1
        for j in puertos[xx]:
            print str(j)
            saltodelinea("int Gi 0/0/"+str(contador))
            vlanypuerto(str(j))
            contador=contador+1

    file.close()


