 GROUP=dataIA_P2
 size=Standard_D2s_v3
 localisation=westeurope
 username=greta

 # Creation groupe de ressources
 az group create -l westeurope -n ${GROUP}

#echo $username

for i in 5
do
  echo "Setup VM${i}xxx"
  # Creation adr publique avec DNS
  #az network public-ip create -g $GROUP -n p2-g${i}Ip --dns-name greta-p2-g${i} --allocation-method Static
  # Creation VM
  az vm create -n vm${i} -g dataIA_P2 --data-disk-sizes-gb 100 --size $size --image UbuntuLTS --public-ip-address p2-g${i}Ip --admin-username greta --admin-password GRETAP2-2023!
  # Ouverture des ports
  az vm open-port --port 3306,5432,80,5000,3000 --resource-group dataIA_P2 --name vm$i --priority 140
done

# Si manque de place VM: stopper la VM puis:
#az disk update --resource-group dataIA_P2 -n vm3_disk1_475d7454a4c644c29a63dbfad1f78300 --size-gb 100
