memfile="/proc/meminfo"

getmeminfo()
{
  a=`more $memfile`
  FREE=`echo "$a"|awk 'NR==2{print $2}'`
  PHYMEM=`echo "$a"|awk 'NR==1{print $2}'`
  ACTIVE=`echo "$a"|awk 'NR==7{print $2}'`
}

while true
do
  getmeminfo
  echo "Total Mem= "$PHYMEM", FREEMEM="$FREE", ACTIVEMEM="$ACTIVE""
  echo $PHYMEM >> log.txt
  echo $FREE >> log.txt
  echo $ACTIVE >> log.txt
  sleep 1
done
