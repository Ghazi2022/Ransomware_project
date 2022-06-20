import socket
import threading
import sys
import subprocess, sys, io
import time
from win10toast import ToastNotifier

#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            
            print("You have been disconnected from the server")
            signal = False
            break

#Get host and port
host = input("Host: ")
port = int(input("Port: "))

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

pf_old=" "
allprot_old = ""
allprot = ""
x=0
etatmyl_old=["True","True","True","True","True"]
etatmy2_old=["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False"]
etatmyem_old=["","","","","","","","",""]
etatmyajout_old=["","","",""]
etatmyperm_old=["MicrosoftUpdateServer|MMPC"]
etatmy0l_old=["1","1","1","1"]
etatmyl0_old=["0"]
etatmyl8_old=["1","1"]
etatmyl35_old=["1","1","1","1"]
etatmyl69_old=["1"]
etatmyl1_old=["1"]
etatmyl01_old=["1","1"]
while True:
    toaster = ToastNotifier()
    p = subprocess.Popen(["powershell.exe", 
                "get-MpPreference"], 
                stdout=subprocess.PIPE)

    output = str(p.stdout.read())
    mylist = output.split('\\r\\n')

    """for pf in mylist:
      if "ControlledFolderAccessProtectedFolders" in pf:
        
        if pf_old != pf:
            pfs=pf.replace('{','')
            pfs=pf.replace('}','')
            pfs_old=pf_old.replace('{','')
            pfs_old=pf_old.replace('}','')
            if len(pfs_old) > len (pfs):
                print("na9est")
                pflist = pfs.split(',')
                pflist_old = pfs_old.split(',')            
                for i in range (0,len(pflist)):            
                    if x==0 and pflist_old[i] != pflist[i]:
                        allprot = pflist_old[i]
                        x=1
                    elif x==0:
                        allprot = pflist_old[len(pflist_old)-1]
                notif = "Attention ! le fichier suivant a été supprimé" + allprot
            elif len(pfs_old) < len (pfs):
                print("zedt")
                pflist = pfs.split(',')
                pflist_old = pfs_old.split(',')
                for i in range (0,len(pflist_old)):            
                    if x==0 and pflist_old[i] != pflist[i]:
                        allprot = pflist[i]
                        x=1
                    elif x==0:
                        allprot= pflist[len(pflist)-1]
                notif = "Le fichier suivant est devenu protéger" + allprot     
            print(allprot)
            toaster.show_toast(notif)
            message=allprot
            print("message!! : "+message)
            sock.sendall(str.encode(message))
            pf_old = pf
            x=0
    for pf in mylist:
      if "ControlledFolderAccessAllowedApplications" in pf:
        
        if pf_old != pf:
            
            pfs=pf.replace('{','')
            pfs=pf.replace('}','')
            pfs_old=pf_old.replace('{','')
            pfs_old=pf_old.replace('}','')
            if len(pfs_old) > len (pfs):
                print("na9est")
                pflist = pfs.split(',')
                pflist_old = pfs_old.split(',')            
                for i in range (0,len(pflist)):            
                    if x==0 and pflist_old[i] != pflist[i]:
                        allprot = pflist_old[i]
                        x=1
                    elif x==0:
                        allprot = pflist_old[len(pflist_old)-1]
                notif = "Attention ! l'app suivante n est plus protegée " + allprot
            elif len(pfs_old) < len (pfs):
                print("zedt")
                pflist = pfs.split(',')
                pflist_old = pfs_old.split(',')
                for i in range (0,len(pflist_old)):            
                    if x==0 and pflist_old[i] != pflist[i]:
                        allprot = pflist[i]
                        x=1
                    elif x==0:
                        allprot= pflist[len(pflist)-1]
                notif = "L app suivante est devenu protéger" + allprot     
            print(allprot)
            toaster.show_toast(notif)
            message=allprot
            print("message!! : "+message)
            sock.sendall(str.encode(message))
            pf_old = pf
            x=0"""
    
    pf_old="False"
    
    toaster = ToastNotifier()
    p = subprocess.Popen(["powershell.exe", 
                    "get-MpPreference"], 
                    stdout=subprocess.PIPE)

    output = str(p.stdout.read())
    mylist = output.split('\\r\\n')
    myl = ["UILockdown","AllowDatagramProcessingOnWinServer","DisableArchiveScanning","DisableBehaviorMonitoring","DisableCatchupFullScan","DisableCatchupQuickScan","DisableDatagramProcessing"
        ,"DisableDnsOverTcpParsing","DisableDnsParsing","DisableEmailScanning","DisableHttpParsing","DisableInboundConnectionFiltering","DisableIOAVProtection","DisableRdpParsing"
        ,"DisableRemovableDriveScanning","DisableRestorePoint","DisableScanningMappedNetworkDrivesForFullScan"
        ,"DisableScanningNetworkFiles","DisableScriptScanning","DisableSshParsing","DisableTlsParsing","MeteredConnectionUpdates","ScanOnlyIfIdleEnabled","SignatureDisableUpdateOnStartupWithoutEngine"]
    for pf in mylist:
            for y in myl:
             if y in pf: 
                etat = pf.split(": ")[1]
              
                if etat!= etatmy2_old[myl.index(y)]:
                    if etat=="True":
                        toaster.show_toast("Must Be False",pf)
                        print(pf,'    ==========    ',etat)
                #sock.sendall(str.encode(message))
                message=pf
                #etatmy2_old[myl.index(y)]=etat
                etatmy2_old[myl.index(y)]=etat

    pf_old="True"
    
    
    toaster = ToastNotifier()
    p = subprocess.Popen(["powershell.exe", 
              "get-MpPreference"], 
                        stdout=subprocess.PIPE)

    output = str(p.stdout.read())
    mylist = output.split('\\r\\n')
    myl=["AllowNetworkProtectionDownLevel","AllowNetworkProtectionOnWinServer","DisableCpuThrottleOnIdleScans","EnableDnsSinkhole"
    ,"EnableFileHashComputation"]

    for pf in mylist:
                for y in myl:
                 if y in pf:
                    etat = pf.split(": ")[1]
                    if etat!=etatmyl_old[myl.index(y)]:
                        etatmyl_old[myl.index(y)]=etat
                        if etat=="False":
                         toaster.show_toast("Must Be True",pf)
                         message=pf
                         sock.sendall(str.encode(message))
    pf_old=""
    
    toaster = ToastNotifier()
    p = subprocess.Popen(["powershell.exe", 
                             "get-MpPreference"], 
                             stdout=subprocess.PIPE)

    output = str(p.stdout.read())
    mylist = output.split('\\r\\n')
    myl=["ExclusionPath","ExclusionExtension","ExclusionProcess","ExclusionIpAddress","AttackSurfaceReductionOnlyExclusions"
                        ,"AttackSurfaceReductionRules_Actions","AttackSurfaceReductionRules_Ids","SignatureDefinitionUpdateFileSharesSources"
                        ,"ThreatIDDefaultAction_Ids"]
    myla=["SharedSignaturesPath","ProxyBypass","ProxyPacUrl","ProxyServer"]
    mylp=["SignatureFallbackOrder"]

    for pf in mylist:
                            for y in myl:
                             if y in pf:
                                etat = pf.split(": ")[1]
                                if etat!=etatmyem_old[myl.index(y)]:
                                    etatmyem_old[myl.index(y)]=etat
                                    if etat!="":
                                        toaster.show_toast("Register Must Be Empty",pf)
                                        message=pf
                                        #print("message!! : "+message)
                                        sock.sendall(str.encode(message))
    for pf in mylist:
                    for y in myla:
                        if y in pf:
                            etat = pf.split(": ")[1]
                            if etat!=etatmyajout_old[myla.index(y)]:
                                etatmyajout_old[myla.index(y)]=etat
                                if etat=="False":
                                     toaster.show_toast("Attention Ajout de permission a vérifier",pf)
                                     message=pf
                                     #print("message!! : "+message)
                                     sock.sendall(str.encode(message))
    for pf in mylist:
                    for y in mylp:
                        if y in pf:
                            etat = pf.split(": ")[1]
                            if etat!=etatmyperm_old[mylp.index(y)]:
                                etatmyperm_old[mylp.index(y)]=etat
                                if etat!="MicrosoftUpdateServer|MMPC":
                                    toaster.show_toast("Attention Ajout de permission a vérifier",pf)
                                    message=pf
                                    #print("message!! : "+message)
                                    sock.sendall(str.encode(message))
     
    pf_old=""
    
    toaster = ToastNotifier()
    p = subprocess.Popen(["powershell.exe", 
                                "get-MpPreference"], 
                                stdout=subprocess.PIPE)

    output = str(p.stdout.read())
    mylist = output.split('\\r\\n')
    myl=["RealTimeScanDirection","QuarantinePurgeItemsAfterDelay","EnableControlledFolderAccess","EnableNetworkProtection"]
    myl0=["DisableRealtimeMonitoring"]
    myl8=["RemediationScheduleDay","SignatureScheduleDay"]
    myl35=["SevereThreatDefaultAction","HighThreatDefaultAction","ModerateThreatDefaultAction","LowThreatDefaultAction"]
    myl69=["ThreatIDDefaultAction_Actions"]
    myl1=["UnknownThreatDefaultAction"]
    myl01=["SubmitSamplesConsent","PUAProtection"]
    for pf in mylist:
            for y in myl:
                if y in pf:
                 etat = pf.split(": ")[1]
                 if etat!=etatmy0l_old[myl.index(y)]:
                    etatmy0l_old[myl.index(y)]=etat
                    if etat=="0":
                        toaster.show_toast("Register Must not Be 0",pf)
                        message=pf
                        #print("message!! : "+message)
                        sock.sendall(str.encode(message))
            for y in myl0:
                if y in pf:
                 etat = pf.split(": ")[1]
                 if etat!=etatmyl0_old[myl0.index(y)]:
                    etatmyl0_old[myl0.index(y)]=etat                
                    if etat!="0":
                        toaster.show_toast("Register Must Be 0",pf)
                        message=pf
                        #print("message!! : "+message)
                        sock.sendall(str.encode(message))
                                
            for y in myl8:
                    if y in pf:
                     etat = pf.split(": ")[1]
                     if etat!=etatmyl8_old[myl8.index(y)]:
                         etatmyl8_old[myl8.index(y)]=etat
                         if etat=="8":
                            toaster.show_toast("Register Must not Be 8",pf)
                            message=pf
                            #print("message!! : "+message)
                            sock.sendall(str.encode(message))
            for y in myl35:
                    if y in pf:
                     etat = pf.split(": ")[1]
                     if etat!=etatmyl35_old[myl35.index(y)]:
                         etatmyl35_old[myl35.index(y)]=etat
                         if ((etat=="3")or (etat=="5")):
                                toaster.show_toast("Register Must not Be 3 or 5",pf)
                                message=pf
                                #print("message!! : "+message)
                                sock.sendall(str.encode(message))
            for y in myl69:
                    if y in pf:
                     etat = pf.split(": ")[1]
                     if etat!=etatmyl69_old[myl69.index(y)]:
                         etatmyl69_old[myl69.index(y)]=etat                     
                         if ((etat=="6")or (etat=="9")):
                            toaster.show_toast("Register Must not Be 6 or 9",pf)
                            message=pf
                            print("message!! : "+message)
                            sock.sendall(str.encode(message))
                                    
            for y in myl1:
                    if y in pf:
                     etat = pf.split(": ")[1]
                     if etat!=etatmyl1_old[myl1.index(y)]:
                         etatmyl1_old[myl1.index(y)]=etat                      
                         if etat!="1":
                            toaster.show_toast("Register Must be 1",pf)
                            message=pf
                            print("message!! : "+message)
                            sock.sendall(str.encode(message))
            for y in myl01:
                    if y in pf:
                     etat = pf.split(": ")[1]
                     if etat!=etatmyl01_old[myl01.index(y)]:
                         etatmyl01_old[myl01.index(y)]=etat                         
                         if ((etat=="0")or (etat=="1")):
                            toaster.show_toast("Register Must be 0 or 1",pf)
                            message=pf
                            print("message!! : "+message)
                            sock.sendall(str.encode(message))
    print("fin")
    time.sleep(5)
