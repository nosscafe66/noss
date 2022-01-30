#標準出力のログ
LOGFILE="/tmp/backup-`date +%w`.log"
exec >> "${LOGFILE}"
exec 2>&1

#Ganglia取得情報
CLUSTERID=$(gstat -n | grep "Name:")
HOSTLISTS=($(gstat -a --list | grep "ip"))
Value=(os_name os_release proc_run mem_cached swap_free disk_free cpu_system gexec machine_type pkts_in pkts_out load_one bytes_in swap_total cpu_user load_five disk_total mem_shared proc_total cpu_wio location mem_total boottime cpu_aidle mem_buffers part_max_used cpu_num cpu_speed mem_free load_fifteen cpu_steal cpu_idle cpu_nice bytes_out)
Value_Count=$(echo ${#Value[*]})
HOSTLISTS_Count=$(echo ${#HOSTLISTS[*]})

#引数設定
CLUSTERNAME=$1
LOOPCOUNT=$2
SLEEPTIME=$3
S3OUTPATH=$4

#出力先ディレクトリ設定
DIRNAME=`date '+%T'${CLUSTERNAME}`

#時間ごとにディレクトリ作成
function MakeDir() {
    if [ ! -d ${DIRNAME} ]; then
        mkdir $DIRNAME
    fi
}

#各ホストからメトリクス情報取得
function GetGangliaList() {
    for i in `seq $Value_Count`
        do
        for j in `seq $HOSTLISTS_Count`
            do
            TIME=$(echo `date '+%y/%m/%d %H:%M:%S'`)
            GANGLIAINFO=($(curl "http://${HOSTNAME}/ganglia/api/metrics.php?host=${HOSTLISTS[j-1]}&metric_name=${Value[i-1]}" | jq -r .message >> "./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json"))
            GANGLIAMESSAGE=($(chmod +r ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | cat -e ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | sed -i -e s/\{//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | sed  -i -e s/\}//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | sed  -i -e s/\"//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json))
            GANGLIAMEUNITS=($(chmod +r ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | cat -e ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | sed -i -e s/\{//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | sed  -i -e s/\}//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | sed  -i -e s/\"//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json))
            if grep -q  "Invalid metric request for this host. Please check metric exists." ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json; then 
                cat ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | grep "Invalid metric request for this host. Please check metric exists." > "./${DIRNAME}/ganglia_invalid_log_${HOSTLISTS[j-1]}.txt"
            fi
            metric_value=($(cat ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | grep -v "Invalid metric request for this host. Please check metric exists" |grep "metric_value" | cut -d "," -f 1 | cut -d ":" -f 2))
            units=($(cat ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.json | grep "units" | cut -d "," -f 2))
            echo "${TIME},${HOSTLISTS[j-1]},${Value[i-1]},${metric_value[i-1]},${units[i-1]}" >> ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv
            cat -e ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv | sed -i -e s/\{//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv | sed -i -e s/\}//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv | sed -i -e s/message.metric_value://g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv | sed -i -e s/status://g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv | sed -i -e s/\"//g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv |sed -i -e s/units:/units,/g ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv
        done
    done
    ENDTIME=$(echo `date '+%y/%m/%d %H:%M:%S'`)
    echo "=====================================================${ENDTIME}===========================================================" >> ./${DIRNAME}/ganglia_list_${HOSTLISTS[j-1]}.csv
}

function TransferFile() {
    aws s3 cp $DIRNAME $S3OUTPATH$DIRNAME --recursive
    if [$? -eq 1]; then
        exit 1
    fi
}

#メイン処理
function Main() {
    count=0
    while true;do
        echo $count
        count=`expr $count + 1`
        MakeDir
        GetGangliaList
        time=date;sleep $SLEEPTIME;echo ""
        echo "経過時間: $count expr $time (s)"
        if [ $count -eq $LOOPCOUNT ]; then
            TransferFile
            exit 0
        fi
    done
    exit 0
}
Main
